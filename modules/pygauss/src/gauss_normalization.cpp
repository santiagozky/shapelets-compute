#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <pygauss.h>
#include <iostream>
#include <sstream>
#include <iomanip>

#include <utility>

namespace py = pybind11;
namespace gnorm = gauss::normalization;



void pygauss::bindings::gauss_normalization_functions(py::module &m) {

    m.def(
        "decimal_scaling", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::decimalScalingNorm(arr);
        },
        py::arg("array_like").none(false));

    m.def(
        "minmax_norm", 
        [](const py::object& array_like, const double high, const double low) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::maxMinNorm(arr, high, low);
        },
        py::arg("array_like").none(false),
        py::arg("high") = 1.0,
        py::arg("low") = 0.0);

    m.def(
        "mean_norm", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::meanNorm(arr);
        },
        py::arg("array_like").none(false));

    m.def(
        "zscore", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::znorm(arr);
        },
        py::arg("array_like").none(false));        

    m.def(
        "unit_length_norm", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::unitLengthNorm(arr);
        },
        py::arg("array_like").none(false));        

    m.def(
        "median_norm", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::medianNorm(arr);
        },
        py::arg("array_like").none(false));        

    m.def(
        "logistic_norm", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::sigmoidNorm(arr);
        },
        py::arg("array_like").none(false));         

    m.def(
        "tanh_norm", 
        [](const py::object& array_like) {
            auto arr = arraylike::as_array_checked(array_like);
            return gnorm::tanhNorm(arr);
        },
        py::arg("array_like").none(false)); 
}