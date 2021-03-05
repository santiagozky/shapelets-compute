from typing import List, Optional, Tuple, Union, Any, Callable
from typing import overload

numeric = Union[int, float, complex]
Shape = Union[int, Tuple[int,...]]
DataType = object
array_like = object  # todo

def abs(a: ShapeletsArray) -> ShapeletsArray: ...
def all_true(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[bool,ShapeletsArray]: ...
def any_true(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[bool,ShapeletsArray]: ...
def arccos(a: ShapeletsArray) -> ShapeletsArray: ...
def arccosh(a: ShapeletsArray) -> ShapeletsArray: ...
def arcsin(a: ShapeletsArray) -> ShapeletsArray: ...
def arcsinh(a: ShapeletsArray) -> ShapeletsArray: ...
def arctan(a: ShapeletsArray) -> ShapeletsArray: ...
def arctanh(a: ShapeletsArray) -> ShapeletsArray: ...
def arg(a: ShapeletsArray) -> ShapeletsArray: ...
def argmax(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[Tuple[int,numeric],Tuple[ShapeletsArray,ShapeletsArray]]: ...
def argmin(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[Tuple[int,numeric],Tuple[ShapeletsArray,ShapeletsArray]]: ...
def array(array_like: object, shape: Optional[Shape] = ..., dtype: Optional[DataType] = ...) -> ShapeletsArray: ...
@overload
def atan2(left: ShapeletsArray, right: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def atan2(left: float, right: ShapeletsArray) -> ShapeletsArray: ...
@overload
def atan2(*args, **kwargs) -> Any: ...
@overload
def batch(arg0: Callable[[], ShapeletsArray]) -> ShapeletsArray: ...
@overload
def batch() -> ScopedBatch: ...
def cast(a: ShapeletsArray, type: DataType) -> ShapeletsArray: ...
def cbrt(a: ShapeletsArray) -> ShapeletsArray: ...
def ceil(a: ShapeletsArray) -> ShapeletsArray: ...
def cholesky(a: ShapeletsArray, is_upper: bool = ...) -> ShapeletsArray: ...
def choleskyInPlace(a: ShapeletsArray, is_upper: bool = ...) -> ShapeletsArray: ...
def clamp(a: ShapeletsArray, lo: Union[ShapeletsArray,float], up: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def complex(left: ShapeletsArray, right: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def complex(left: float, right: ShapeletsArray) -> ShapeletsArray: ...
@overload
def complex(*args, **kwargs) -> Any: ...
def conjg(a: ShapeletsArray) -> ShapeletsArray: ...
def constant(shape: Shape, value: object, dtype: Optional[DataType] = ...) -> ShapeletsArray: ...
def convolve(signal: object, filter: object, mode: ConvMode = ..., domain: ConvDomain = ...) -> ShapeletsArray: ...
def convolve1(signal: ShapeletsArray, filter: ShapeletsArray, mode: ConvMode = ..., domain: ConvDomain = ...) -> ShapeletsArray: ...
def convolve2(signal: ShapeletsArray, filter: ShapeletsArray, mode: ConvMode = ..., domain: ConvDomain = ...) -> ShapeletsArray: ...
def convolve3(signal: ShapeletsArray, filter: ShapeletsArray, mode: ConvMode = ..., domain: ConvDomain = ...) -> ShapeletsArray: ...
def corrcoef(a: ShapeletsArray, b: ShapeletsArray) -> Union[float,complex]: ...
def cos(a: ShapeletsArray) -> ShapeletsArray: ...
def cosh(a: ShapeletsArray) -> ShapeletsArray: ...
def count(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[float,ShapeletsArray]: ...
def covp(a: ShapeletsArray, b: ShapeletsArray) -> ShapeletsArray: ...
def covs(a: ShapeletsArray, b: ShapeletsArray) -> ShapeletsArray: ...
def cumsum(a: ShapeletsArray, dim: int = ...) -> ShapeletsArray: ...
def det(a: ShapeletsArray) -> Union[float,complex]: ...
def device_gc(*args, **kwargs) -> Any: ...
def diag(a: ShapeletsArray, index: int = ..., extract: bool = ...) -> ShapeletsArray: ...
def diff1(a: ShapeletsArray, dim: int) -> ShapeletsArray: ...
def diff2(a: ShapeletsArray, dim: int) -> ShapeletsArray: ...
def dot(lhs: ShapeletsArray, rhs: ShapeletsArray, conj_lhs: bool = ..., conj_rhs: bool = ...) -> ShapeletsArray: ...
def dot_scalar(lhs: ShapeletsArray, rhs: ShapeletsArray, conj_lhs: bool = ..., conj_rhs: bool = ...) -> Union[float,complex]: ...
def empty(shape: Shape, dtype: DataType = ...) -> ShapeletsArray: ...
def enable_manual_eval(arg0: bool) -> None: ...
def erf(a: ShapeletsArray) -> ShapeletsArray: ...
def erfc(a: ShapeletsArray) -> ShapeletsArray: ...
def eval(*args) -> None: ...
def exp(a: ShapeletsArray) -> ShapeletsArray: ...
def expm1(a: ShapeletsArray) -> ShapeletsArray: ...
def factorial(a: ShapeletsArray) -> ShapeletsArray: ...
def fft(signal: ShapeletsArray, odim: Optional[int] = ..., norm: Optional[float] = ...) -> ShapeletsArray: ...
def flat(a: ShapeletsArray) -> ShapeletsArray: ...
def flip(a: ShapeletsArray, dimension: int = ...) -> ShapeletsArray: ...
def floor(a: ShapeletsArray) -> ShapeletsArray: ...
def gemm(a: ShapeletsArray, b: ShapeletsArray, c: Optional[ShapeletsArray] = ..., alpha: float = ..., beta: float = ..., transA: bool = ..., transB: bool = ...) -> ShapeletsArray: ...
def get_available_backends(*args, **kwargs) -> Any: ...
def get_backend(*args, **kwargs) -> Any: ...
def get_device(*args, **kwargs) -> Any: ...
def get_device_memory(dev: Optional[Union[int,DeviceInfo]] = ...) -> DeviceMemory: ...
def get_devices(*args, **kwargs) -> Any: ...
def has_backend(test_backend: Backend) -> int: ...
@overload
def hypot(left: ShapeletsArray, right: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def hypot(left: float, right: ShapeletsArray) -> ShapeletsArray: ...
@overload
def hypot(*args, **kwargs) -> Any: ...
def identity(shape: Shape, dtype: DataType = ...) -> ShapeletsArray: ...
def ifft(signal: ShapeletsArray, odim: Optional[int] = ..., norm: Optional[float] = ...) -> ShapeletsArray: ...
def imag(a: ShapeletsArray) -> ShapeletsArray: ...
def intersect(a: ShapeletsArray, b: ShapeletsArray, is_unique: bool = ...) -> ShapeletsArray: ...
def inverse(a: ShapeletsArray, options: MatrixProperties = ...) -> ShapeletsArray: ...
def iota(shape: Shape, tile: Shape = ..., dtype: DataType = ...) -> ShapeletsArray: ...
def isInf(a: ShapeletsArray) -> ShapeletsArray: ...
def isNaN(a: ShapeletsArray) -> ShapeletsArray: ...
def isZero(a: ShapeletsArray) -> ShapeletsArray: ...
def join(lst: List[ShapeletsArray], dimension: int = ...) -> ShapeletsArray: ...
def lgamma(a: ShapeletsArray) -> ShapeletsArray: ...
def log(a: ShapeletsArray) -> ShapeletsArray: ...
def log10(a: ShapeletsArray) -> ShapeletsArray: ...
def log1p(a: ShapeletsArray) -> ShapeletsArray: ...
def lower(a: ShapeletsArray, unit_diag: bool = ...) -> ShapeletsArray: ...
def lu(a: ShapeletsArray) -> tuple: ...
def luInPlace(a: ShapeletsArray) -> tuple: ...
def manual_eval_enabled(*args, **kwargs) -> Any: ...
def matmul(lhs: ShapeletsArray, rhs: ShapeletsArray, lhs_options: MatrixProperties = ..., rhs_options: MatrixProperties = ...) -> ShapeletsArray: ...
def matmulNT(lhs: ShapeletsArray, rhs: ShapeletsArray) -> ShapeletsArray: ...
def matmulTN(lhs: ShapeletsArray, rhs: ShapeletsArray) -> ShapeletsArray: ...
def matmulTT(lhs: ShapeletsArray, rhs: ShapeletsArray) -> ShapeletsArray: ...
def matmul_chain(*args) -> ShapeletsArray: ...
def matrixprofile(ta: ShapeletsArray, m: int, tb: Optional[ShapeletsArray] = ...) -> MatrixProfile: ...
def matrixprofileLR(ta: ShapeletsArray, m: int) -> dict: ...
def max(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
@overload
def max_of(left: ShapeletsArray, right: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def max_of(left: float, right: ShapeletsArray) -> ShapeletsArray: ...
@overload
def max_of(*args, **kwargs) -> Any: ...
def mean(a: ShapeletsArray, weights: Optional[ShapeletsArray] = ..., dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
def median(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
def min(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
@overload
def min_of(left: ShapeletsArray, right: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def min_of(left: float, right: ShapeletsArray) -> ShapeletsArray: ...
@overload
def min_of(*args, **kwargs) -> Any: ...
def moddims(a: ShapeletsArray, shape: Shape) -> ShapeletsArray: ...
def norm(a: ShapeletsArray, type: NormType = ..., p: float = ..., q: float = ...) -> float: ...
def pad(a: ShapeletsArray, begin: Shape, end: Shape, fill_type: BorderType) -> ShapeletsArray: ...
def parallel_range(arg: Union[int,slice]) -> ParallelFor: ...
def pinverse(a: ShapeletsArray, tol: float = ...) -> ShapeletsArray: ...
def product(a: ShapeletsArray, dim: Optional[int] = ..., nan_value: Optional[float] = ...) -> Union[float,complex,ShapeletsArray]: ...
def qr(a: ShapeletsArray) -> tuple: ...
def qrInPlace(a: ShapeletsArray) -> tuple: ...
def randn(shape: Shape, dtype: DataType = ..., engine: Optional[ShapeletsRandomEngine] = ...) -> ShapeletsArray: ...
def random_engine(type: RandomEngineType = ..., seed: int = ...) -> ShapeletsRandomEngine: ...
def randu(shape: Shape, dtype: DataType = ..., engine: Optional[ShapeletsRandomEngine] = ...) -> ShapeletsArray: ...
def range(shape: Shape, seq_dim: int = ..., dtype: DataType = ...) -> ShapeletsArray: ...
def rank(a: ShapeletsArray, tol: float = ...) -> int: ...
def real(a: ShapeletsArray) -> ShapeletsArray: ...
def reorder(a: ShapeletsArray, x: int, y: int = ..., z: int = ..., w: int = ...) -> ShapeletsArray: ...
def replace(a: ShapeletsArray, keeping_condition: ShapeletsArray, b: Union[float,ShapeletsArray]) -> ShapeletsArray: ...
def replaceInPlace(a: ShapeletsArray, keeping_condition: ShapeletsArray, b: Union[float,ShapeletsArray]) -> None: ...
@overload
def root(left: ShapeletsArray, right: Union[ShapeletsArray,float]) -> ShapeletsArray: ...
@overload
def root(left: float, right: ShapeletsArray) -> ShapeletsArray: ...
@overload
def root(*args, **kwargs) -> Any: ...
def round(a: ShapeletsArray) -> ShapeletsArray: ...
def rsqrt(a: array_like, *, shape: Optional[Shape] = ..., dtype: Optional[DataType] = ...) -> ShapeletsArray: ...
def scan(a: ShapeletsArray, dim: int = ..., op: ScanOp = ..., inclusive_scan: bool = ...) -> ShapeletsArray: ...
def set_backend(arg0: Backend) -> None: ...
def set_device(arg0: Union[int,DeviceInfo]) -> bool: ...
def shift(a: ShapeletsArray, x: int, y: int = ..., z: int = ..., w: int = ...) -> ShapeletsArray: ...
def sign(a: ShapeletsArray) -> ShapeletsArray: ...
def sin(a: ShapeletsArray) -> ShapeletsArray: ...
def sinh(a: ShapeletsArray) -> ShapeletsArray: ...
def sort(a: ShapeletsArray, dim: int = ..., asc: bool = ...) -> ShapeletsArray: ...
def sort_index(a: ShapeletsArray, dim: int = ..., asc: bool = ...) -> tuple: ...
def sqrt(a: array_like, *, shape: Optional[Shape] = ..., dtype: Optional[DataType] = ...) -> ShapeletsArray: ...
def stdev(a: ShapeletsArray, dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
def sum(a: ShapeletsArray, dim: Optional[int] = ..., nan_value: Optional[float] = ...) -> Union[float,complex,ShapeletsArray]: ...
def svd(a: ShapeletsArray) -> tuple: ...
def svdInPlace(a: ShapeletsArray) -> tuple: ...
def sync(dev: Optional[Union[int,DeviceInfo]] = ...) -> None: ...
def tan(a: ShapeletsArray) -> ShapeletsArray: ...
def tanh(a: ShapeletsArray) -> ShapeletsArray: ...
def tgamma(a: ShapeletsArray) -> ShapeletsArray: ...
@overload
def tile(a: ShapeletsArray, x: int, y: int = ..., z: int = ..., w: int = ...) -> ShapeletsArray: ...
@overload
def tile(a: ShapeletsArray, dims: Shape) -> ShapeletsArray: ...
@overload
def tile(*args, **kwargs) -> Any: ...
def topk_max(a: ShapeletsArray, k: int) -> tuple: ...
def topk_min(a: ShapeletsArray, k: int) -> tuple: ...
@overload
def transpose(array_like: object, shape: Optional[Shape] = ..., dtype: Optional[DataType] = ...) -> ShapeletsArray: ...
@overload
def transpose(a: ShapeletsArray, dims: bool = ...) -> ShapeletsArray: ...
@overload
def transpose(*args, **kwargs) -> Any: ...
def transposeInPlace(a: ShapeletsArray, conjugate: bool = ...) -> None: ...
def trunc(a: ShapeletsArray) -> ShapeletsArray: ...
def union(a: ShapeletsArray, b: ShapeletsArray, is_unique: bool = ...) -> ShapeletsArray: ...
def unique(a: ShapeletsArray, is_sorted: bool = ...) -> ShapeletsArray: ...
def upper(a: ShapeletsArray, unit_diag: bool = ...) -> ShapeletsArray: ...
def var_p(a: ShapeletsArray, weights: Optional[ShapeletsArray] = ..., dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
def var_s(a: ShapeletsArray, weights: Optional[ShapeletsArray] = ..., dim: Optional[int] = ...) -> Union[float,complex,ShapeletsArray]: ...
def where(a: ShapeletsArray) -> ShapeletsArray: ...

class Backend:
    CPU: Any = ...
    CUDA: Any = ...
    Default: Any = ...
    OpenCL: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class BorderType:
    ClampEdge: Any = ...
    Periodic: Any = ...
    Symmetric: Any = ...
    Zero: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class ConvDomain:
    Auto: Any = ...
    Frequency: Any = ...
    Spatial: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class ConvMode:
    Default: Any = ...
    Expand: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class DeviceInfo:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def compute(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def isDoubleAvailable(self) -> bool: ...
    @property
    def isHalfAvailable(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def platform(self) -> str: ...

class DeviceMemory:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def buffers(self) -> int: ...
    @property
    def bytes(self) -> int: ...
    @property
    def locked_buffers(self) -> int: ...
    @property
    def locked_bytes(self) -> int: ...

class MatrixProfile:
    def __init__(self, arg0: ShapeletsArray, arg1: ShapeletsArray) -> None: ...
    @property
    def index(self) -> ShapeletsArray: ...
    @index.setter
    def index(self, val: ShapeletsArray) -> None: ...
    @property
    def profile(self) -> ShapeletsArray: ...
    @profile.setter
    def profile(self, val: ShapeletsArray) -> None: ...

class MatrixProperties:
    BlockDiagonal: Any = ...
    Conjugated: Any = ...
    ConjugatedTransposed: Any = ...
    Default: Any = ...
    Lower: Any = ...
    Orthogonal: Any = ...
    PositiveDefinite: Any = ...
    Symmetric: Any = ...
    Transposed: Any = ...
    TriDiagonal: Any = ...
    UnitDiagonal: Any = ...
    Upper: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class NormType:
    Euclid: Any = ...
    LPQ: Any = ...
    Matrix: Any = ...
    MatrixInf: Any = ...
    Singular: Any = ...
    Vector1: Any = ...
    Vector2: Any = ...
    VectorInf: Any = ...
    VectorP: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class ParallelFor:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> ParallelFor: ...
    def __next__(self) -> ParallelFor: ...

class ScanOp:
    Add: Any = ...
    Max: Any = ...
    Min: Any = ...
    Mul: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class ScopedBatch:
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

class ShapeletsArray:
    __hash__: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def astype(self, type: DataType) -> ShapeletsArray: ...
    def display(self, precision: int = ..., transpose: bool = ...) -> None: ...
    def same_as(self, arr_like: object, eps: float = ...) -> bool: ...
    def __add__(self, other: object) -> ShapeletsArray: ...
    def __and__(self, other: object) -> ShapeletsArray: ...
    def __copy__(self) -> ShapeletsArray: ...
    def __deepcopy__(self) -> ShapeletsArray: ...
    def __eq__(self, other: object) -> ShapeletsArray: ...
    def __ge__(self, other: object) -> ShapeletsArray: ...
    def __getitem__(self, selector: object) -> ShapeletsArray: ...
    def __gt__(self, other: object) -> ShapeletsArray: ...
    def __iadd__(self, other: object) -> ShapeletsArray: ...
    def __iand__(self, other: object) -> ShapeletsArray: ...
    def __ilshift__(self, other: object) -> ShapeletsArray: ...
    def __imod__(self, other: object) -> ShapeletsArray: ...
    def __imul__(self, other: object) -> ShapeletsArray: ...
    def __ior__(self, other: object) -> ShapeletsArray: ...
    def __ipow__(self, other: object) -> ShapeletsArray: ...
    def __irshift__(self, other: object) -> ShapeletsArray: ...
    def __isub__(self, other: object) -> ShapeletsArray: ...
    def __itruediv__(self, other: object) -> ShapeletsArray: ...
    def __ixor__(self, other: object) -> ShapeletsArray: ...
    def __le__(self, other: object) -> ShapeletsArray: ...
    def __lshift__(self, other: object) -> ShapeletsArray: ...
    def __lt__(self, other: object) -> ShapeletsArray: ...
    def __mod__(self, other: object) -> ShapeletsArray: ...
    def __mul__(self, other: object) -> ShapeletsArray: ...
    def __ne__(self, other: object) -> ShapeletsArray: ...
    def __neg__(self, other: object) -> ShapeletsArray: ...
    def __or__(self, other: object) -> ShapeletsArray: ...
    def __pow__(self, other: object) -> ShapeletsArray: ...
    def __radd__(self, other: object) -> ShapeletsArray: ...
    def __rand__(self, other: object) -> ShapeletsArray: ...
    def __rlshift__(self, other: object) -> ShapeletsArray: ...
    def __rmod__(self, other: object) -> ShapeletsArray: ...
    def __rmul__(self, other: object) -> ShapeletsArray: ...
    def __ror__(self, other: object) -> ShapeletsArray: ...
    def __rpow__(self, other: object) -> ShapeletsArray: ...
    def __rrshift__(self, other: object) -> ShapeletsArray: ...
    def __rshift__(self, other: object) -> ShapeletsArray: ...
    def __rsub__(self, other: object) -> ShapeletsArray: ...
    def __rtruediv__(self, other: object) -> ShapeletsArray: ...
    def __rxor__(self, other: object) -> ShapeletsArray: ...
    def __setitem__(self, selector: object, value: object) -> ShapeletsArray: ...
    def __sub__(self, other: object) -> ShapeletsArray: ...
    def __truediv__(self, other: object) -> ShapeletsArray: ...
    def __xor__(self, other: object) -> ShapeletsArray: ...
    @property
    def H(self) -> ShapeletsArray: ...
    @property
    def T(self) -> ShapeletsArray: ...
    @property
    def backend(self) -> Backend: ...
    @property
    def dtype(self) -> DataType: ...
    @property
    def is_column(self) -> bool: ...
    @property
    def is_row(self) -> bool: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> Shape: ...
    @property
    def size(self) -> int: ...


class RandomEngineType:
    Default: Any = ...
    Mersenne: Any = ...
    Philox: Any = ...
    Threefry: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class ShapeletsRandomEngine:
    def __init__(self, *args, **kwargs) -> None: ...
