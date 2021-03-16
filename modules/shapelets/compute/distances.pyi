from . import _pygauss
from .__basic_typing import ArrayLike
from ._array_obj import ShapeletsArray

class DistanceType:
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...
    Euclidian: _pygauss.DistanceType # value = DistanceType.Euclidian
    Hamming: _pygauss.DistanceType # value = DistanceType.Hamming
    Manhattan: _pygauss.DistanceType # value = DistanceType.Manhattan
    Chebyshev: _pygauss.DistanceType # value = DistanceType.Chebyshev
    Minkowshi: _pygauss.DistanceType # value = DistanceType.Minkowshi
    SBD: _pygauss.DistanceType # value = DistanceType.SBD
    DTW: _pygauss.DistanceType # value = DistanceType.DTW
    MPD: _pygauss.DistanceType # value = DistanceType.MPD
    __members__: dict

def pdist(tss: ArrayLike, metric: DistanceType, **kwargs) -> ShapeletsArray: ...
def cdist(xa: ArrayLike, xb: ArrayLike, metric: DistanceType, **kwargs) -> ShapeletsArray:  ...
def euclidian(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def hamming(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def cityblock(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def sbd(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def dtw(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def mpdist(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def chebyshev(a: ArrayLike, b: ArrayLike) -> ShapeletsArray: ...
def minkowshi(a: ArrayLike, b: ArrayLike, p: float) -> ShapeletsArray: ...
