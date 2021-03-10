from typing import Optional
from . import ArrayLike, DataTypeLike, ShapeLike, ShapeletsArray, _pygauss;

class RandomEngineType():
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str:...
    Default: _pygauss.RandomEngineType # value = <RandomEngineType.Default: 100>
    Mersenne: _pygauss.RandomEngineType # value = <RandomEngineType.Mersenne: 300>
    Philox: _pygauss.RandomEngineType # value = <RandomEngineType.Default: 100>
    Threefry: _pygauss.RandomEngineType # value = <RandomEngineType.Threefry: 200>
    __members__: dict # value = {'Default': <RandomEngineType.Default: 100>, 'Mersenne': <RandomEngineType.Mersenne: 300>, 'Threefry': <RandomEngineType.Threefry: 200>, 'Philox': <RandomEngineType.Default: 100>}

class ShapeletsRandomEngine():
    def beta(self, a: float, b: float, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def chisquare(self, df: float, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def exponential(self, scale: float = 1.0, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def gamma(self, alpha: float, scale: float = 1.0, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def logistic(self, loc: float = 0.0, scale: float = 1.0, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def lognormal(self, mean: float = 0.0, sigma: float = 1.0, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def multivariate_normal(self, mean: object, cov: object, samples: int, dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def normal(self, loc: float = 0.0, scale: float = 1.0, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def standard_normal(self, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def uniform(self, low: float = 0.0, high: float = 1.0, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def wald(self, mean: float, scale: float, shape: ShapeLike = (1, 1), dtype: DataTypeLike = 'float32') -> ShapeletsArray: ...
    def permutation(self, x: ArrayLike, axis = 0) -> ShapeletsArray: ...

def default_rng(type: RandomEngineType = RandomEngineType.Default, seed: int = 0) -> ShapeletsRandomEngine:...
def randn(shape: ShapeLike, dtype: DataTypeLike = 'float32', engine: Optional[ShapeletsRandomEngine] = None) -> ShapeletsArray:...
def random(shape: ShapeLike, dtype: DataTypeLike = 'float32', engine: Optional[ShapeletsRandomEngine] = None) -> ShapeletsArray:...
def randint(low: int, high: Optional[int] = None, shape: ShapeLike = (1,1), dtype: DataTypeLike = 'float32', engine: Optional[ShapeletsRandomEngine] = None) -> ShapeletsArray:...
def permutation(x: ArrayLike, axis = 0, engine: Optional[ShapeletsRandomEngine] = None) -> ShapeletsArray:...
