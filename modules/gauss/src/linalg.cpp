#include <gauss/linalg.h>

af::array gauss::linalg::lls(const af::array &A, const af::array &b) {
    af::array U;
    af::array S;
    af::array VT;

    af::svd(U, S, VT, A);

    S = af::diag(S, 0, false);

    af::array S_dagger = (S != 0).as(S.type()) * af::inverse(S);

    long missingRows = static_cast<long>(A.dims(1) - S.dims(0));
    long missingColumns = static_cast<long>(A.dims(0) - S.dims(0));
    af::array toPadRows = af::constant(0, missingRows, A.dims(0), A.type());
    af::array toPadColumns = af::constant(0, A.dims(1), missingColumns, A.type());

    S_dagger = af::join(0, S_dagger, toPadRows);
    S_dagger = af::join(1, S_dagger, toPadColumns);

    af::array V = af::transpose(VT);
    af::array UT = af::transpose(U);
    af::array x = af::matmul(V, S_dagger, UT, b);

    return x;
}
