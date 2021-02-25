#include <arrayfire.h>
#include <spdlog/spdlog.h>
#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

#include <af_array/af_array.h>

namespace py = pybind11;
namespace spd = spdlog;

/*

[9 1 1 1]
Negative Indices			   -9  -8  -7  -6  -5  -4  -3  -2  -1
Positive Indices    		    0   1   2   3   4   5   6   7   8

Values in vector			   10  20  30  40  50  60  70  80  90

numpy			arrayfire	   result
-------------	-----------    -----------------------------------
::-1			-1,  0, -1	   90  80  70  60  50  40  30  20  10
-1::-1			-1,  0, -1	   90  80  70  60  50  40  30  20  10
-1:-10:-1		-1, -9, -1	   90  80  70  60  50  40  30  20  10
-1:-9:-1		-1, -8, -1	   90  80  70  60  50  40  30  20
-2:-9:-1		-2, -8, -1	   80  70  60  50  40  30  20
-8:-9:-1		-8, -8, -1	   20
-1:-2:-1        -1, -1, -1     90
-9:-10:-1       -9, -9, -1     10
1:-1			 1, -2,  1     20  30  40  50  60  70  80
::				 0, -1,  1     10  20  30  40  50  60  70  80  90
1:				 1, -1,  1	   20  30  40  50  60  70  80  90
1:5				 1,  4,  1	   20  30  40  50


 */

slice_interpretation interpret_slice(const py::slice &slice) {

    if (slice.is_none())
        throw std::runtime_error("Null value given for slice");

    // default values
    slice_interpretation r = {0, -1, 1};

    auto raw = (PySliceObject *) slice.ptr();
    auto raw_step = py::reinterpret_borrow<py::int_>(raw->step);
    auto raw_start = py::reinterpret_borrow<py::int_>(raw->start);
    auto raw_stop = py::reinterpret_borrow<py::int_>(raw->stop);

    if (!raw_step.is_none()) {
        r.step = raw_step.cast<ssize_t>();
        if (r.step < 0) {
            r.start = -1;
            r.stop = 0;
        }
    }

    if (!raw_start.is_none())
        r.start = raw_start.cast<ssize_t>();

    if (!raw_stop.is_none())
        r.stop = raw_stop.cast<ssize_t>();

    if (r.start >= 0 && r.stop >= 0 && r.stop <= r.start && r.step >= 0) {
        r.start = 1;
        r.stop = 1;
        r.step = 1;
    } else if (r.start < 0 && r.stop < 0 && r.stop >= r.start && r.step <= 0) {
        r.start = -2;
        r.stop = -2;
        r.step = -1;
    }

    if (!raw_stop.is_none())
        r.stop = r.stop + (r.step < 0 ? 1 : -1);

//    if (spd::get_level() == spd::level::level_enum::debug)
//        spd::debug("Transformed {} into {}, {}, {}", py::repr(slice).cast<std::string>(), r.start, r.stop, r.step);

    return r;
}

ParallelFor::ParallelFor(const py::slice &slice) {
    auto r = interpret_slice(slice);
    start = r.start;
    stop = r.stop;
    step = r.step;
}

/**
 * The default status for the batching flag is false
 */
thread_local bool GForStatus::status = false;


std::tuple<af::dim4, af_index_t *> build_index(const py::object &selector, const af::dim4 &arr_dim) {
    if (selector.is_none())
        throw std::runtime_error("No selector");

    af_index_t *afIndex = nullptr;
    check_af_error(af_create_indexers(&afIndex));

    auto result_dim = af::dim4(arr_dim);

    if (py::isinstance<py::ellipsis>(selector)) {
        // the user has done something like array[...]
        // which should result in a select all operation.
        spd::debug("Selector was ...; returning without further indexing");
        return {result_dim, afIndex};
    }

    // Homogenize the input knowing that at max there are 4 dimensions
    // and remove single item cases and / or ellipsis in tuples
    std::vector<std::optional<py::object>> items(4, std::nullopt);

    if (!py::isinstance<py::tuple>(selector)) {
        // we are dealing with a single entry,
        // which is not an ellipsis
        items[0] = std::move(selector);
    } else {
        auto tuple = py::cast<py::tuple>(selector);
        auto tuple_size = tuple.size();

        if (tuple_size == 0)
            // ensure we detect arr[()]
            throw std::runtime_error("Empty tuple is not a valid indexer");

        if (tuple_size > 4)
            throw std::runtime_error("Up to four dimensions are supported.  If more dimensions are required, "
                                     "cast to numpy using either a memoryview object or np.array(obj)");
        size_t i = 0; // tuple item
        size_t d = 0; // current dimension
        while (i < tuple_size) {
            auto item = py::cast<py::object>(tuple[i]);
            if (py::isinstance<py::ellipsis>(item))
                // if it is an ellipsis, calculate how many dimensions
                // are we skipping based on the size of the tuple,
                // the current position within the tuple and the
                // total number of indexable dimensions
                //
                d = arr_dim.ndims() - tuple_size + i + 1;
            else {
                // store for further processing
                items[d] = std::move(item);
                d += 1;
            }
            i += 1;
        }
    }

    // right now we have an object per dimension or empty option
    // it should be as simple as process each one of them:
    for (auto i=0; i<4; i++) {
        auto item_op = items[i];
        if (!item_op.has_value())
            continue;

        auto item = item_op.value();

        if (item.is_none())
            continue;

        if (py::isinstance<py::int_>(item)) {
            auto v = py::cast<int>(item);
            spd::debug("Found a integer at pos {} interpreted as {}, {}, {}", i, v, v, 1);
            check_af_error(af_set_seq_param_indexer(afIndex, v, v, 1, i, false));
            spd::debug("Resulting dimension at pos {} is 1", i);
            result_dim[i] = 1;
            continue;
        }

        if (py::isinstance<py::slice>(item)) {
            auto[start, stop, step] = interpret_slice(py::cast<py::slice>(item));
            spd::debug("Found a slice at pos {} interpreted as {}, {}, {}", i, start, stop, step);
            check_af_error(af_set_seq_param_indexer(afIndex, start, stop, step, i, false));
            auto v1 = start < 0 ? arr_dim[i] + start : start;
            auto v2 = stop < 0 ? arr_dim[i] + stop : stop;
            auto span = (long) abs(v1-v2) + 1;
            auto int_div = div(span, abs(step));
            auto len = int_div.quot + (int_div.rem != 0 ? 1 : 0);
            result_dim[i] = (dim_t) len;
            spd::debug("Resulting dimension at pos {} is {} (Original was {})", i, result_dim[i], arr_dim[i]);
            continue;
        }

        if (py::isinstance<ParallelFor>(item)) {
            auto pf = py::cast<ParallelFor>(item);
            auto start = pf.getStart();
            auto stop = pf.getStop();
            auto step = pf.getStep();
            check_af_error(af_set_seq_param_indexer(afIndex, start, stop, step, i, true));
            auto v1 = start < 0 ? arr_dim[i] + start : start;
            auto v2 = stop < 0 ? arr_dim[i] + stop : stop;
            auto span = (long) abs(v1-v2) + 1;
            auto int_div = div(span, abs(step));
            auto len = int_div.quot + (int_div.rem != 0 ? 1 : 0);
            result_dim[i] = (dim_t) len;
            continue;
        }

        if (py::isinstance<af::array>(item)) {
            auto ind_arr = py::cast<af::array>(item);
            af_array out;
            if (ind_arr.type() == af::dtype::b8)
                check_af_error(af_where(&out, ind_arr.get()));
            else
                out = ind_arr.get();

            // store the number of elements as the dimension size
            check_af_error(af_get_elements(&result_dim[i], out));
            check_af_error(af_set_array_indexer(afIndex, out, i));
            continue;
        }

        throw std::runtime_error("Unable to process index expression");
    }
    spd::debug("Indexing calculations ended.");
    if (afIndex == nullptr)
        spd::debug("ARSE");

    return {result_dim, afIndex};
}
