import builtins
import pickle
from typing import Any, Callable, Dict, IO, Iterator, List, Optional, Sequence, \
    Tuple, Type, TypeVar, Union, overload

import numpy as np
import torch.autograd
import torch.backends.cuda
import torch.backends.mkl
import torch.cuda
import torch.distributions
import torch.jit
import torch.multiprocessing
import torch.nn
import torch.nn.functional
import torch.onnx
import torch.optim
import torch.random
import torch.sparse
import torch.testing
import torch.utils.backcompat
from torch._tensor_str import set_printoptions
from torch.random import get_rng_state, initial_seed, manual_seed, set_rng_state
from torch.storage import _StorageBase
from torch.tensor import Tensor as TensorBase
from torch.utils.hooks import RemovableHandle


def load(f: Union[str, IO],
         map_location: Optional[Union[
             Dict[str, str], str, torch.device, Callable[
                 [str, str], str]]] = None,
         pickle_module=pickle, **pickle_load_args): ...


def save(obj: Any, f: Union[str, IO], pickle_module=pickle,
         pickle_protocol=pickle.DEFAULT_PROTOCOL): ...


no_grad: Any = ...
enable_grad: Any = ...
set_grad_enabled: Any = ...


class device:
    def __init__(self, device: Union[builtins.int, builtins.str]): ...


class finfo:

    def __init__(self, type: torch.dtype): ...

    @property
    def bits(self) -> builtins.int: ...

    @property
    def eps(self) -> builtins.float: ...

    @property
    def max(self) -> builtins.float: ...

    @property
    def min(self) -> builtins.float: ...

    @property
    def tiny(self) -> builtins.float: ...


class layout: ...


class dtype: ...


class Generator: ...


class Size(Tuple[builtins.int, ...]):
    def __init__(self, xs: Optional[Sequence[builtins.int]] = None): ...


T = TypeVar('T')
MaybeTuple = Union[T, Tuple[T, ...]]
MaybeList = Union[T, List[T]]


class _float16(dtype): ...


class _float32(dtype): ...


class _float64(dtype): ...


class _uint8(dtype): ...


class _int8(dtype): ...


class _int16(dtype): ...


class _int32(dtype): ...


class _int64(dtype): ...


half = float16 = _float16()
double = float64 = _float64()
short = int16 = _int16()
long = int64 = _int64()
uint8 = _uint8()
float = float32 = _float32()
int = int32 = _int32()


class StorageBase(_StorageBase):
    @classmethod
    def from_buffer(cls, buffer: bytes) -> StorageBase: ...


class ByteStorage(StorageBase): ...


class FloatStorage(StorageBase): ...


class DoubleStorage(StorageBase): ...


class HalfStorage(StorageBase): ...


class IntStorage(StorageBase): ...


class LongStorage(StorageBase): ...


class ShortStorage(StorageBase): ...


class strided(layout): pass


class sparse_coo(layout): pass


# type aliases for use in `Tensor` class, to avoid conflicts with attributes of the same name.
_dtype = dtype
_device = device


class Tensor(TensorBase):
    dtype: _dtype
    device: _device

    @overload
    def __init__(self, *size: builtins.int): ...

    @overload
    def __init__(self, elems: list): ...

    @overload
    def __init__(self, storage: _StorageBase): ...

    def __add__(self, other) -> Tensor: ...

    def __radd__(self, other) -> Tensor: ...

    def __iadd__(self, other) -> Tensor: ...

    def __sub__(self, other) -> Tensor: ...

    def __rsub__(self, other) -> Tensor: ...

    def __isub__(self, other) -> Tensor: ...

    def __mul__(self, other) -> Tensor: ...

    def __rmul__(self, other) -> Tensor: ...

    def __imul__(self, other) -> Tensor: ...

    def __rdiv__(self, other) -> Tensor: ...

    def __idiv__(self, other) -> Tensor: ...

    def __truediv__(self, other) -> Tensor: ...

    def __rtruediv__(self, other) -> Tensor: ...  # type: ignore

    def __itruediv__(self, other) -> Tensor: ...

    def __pow__(self, power, modulo=None) -> Tensor: ...

    def __rpow__(self, other) -> Tensor: ...

    def __mod__(self, other) -> Tensor: ...

    def __rmod__(self, other) -> Tensor: ...

    def __imod__(self, other) -> Tensor: ...

    def __matmul__(self, other) -> Tensor: ...

    def __rmatmul__(self, other) -> Tensor: ...

    def __imatmul__(self, other) -> Tensor: ...

    def __neg__(self) -> Tensor: ...

    def __eq__(self, other) -> ByteTensor: ...

    def __ne__(self, other) -> ByteTensor: ...

    def __lt__(self, other) -> ByteTensor: ...

    def __le__(self, other) -> ByteTensor: ...

    def __gt__(self, other) -> ByteTensor: ...

    def __ge__(self, other) -> ByteTensor: ...

    def __and__(self, other) -> ByteTensor: ...

    def __iand__(self, other) -> ByteTensor: ...

    def __rand__(self, other) -> ByteTensor: ...

    def __or__(self, other) -> ByteTensor: ...

    def __ior__(self, other) -> ByteTensor: ...

    def __ror__(self, other) -> ByteTensor: ...

    def __invert__(self) -> ByteTensor: ...

    def __xor__(self, other) -> ByteTensor: ...

    def __ixor__(self, other) -> ByteTensor: ...

    def __rxor__(self, other) -> ByteTensor: ...

    def __len__(self) -> builtins.int: ...

    def __iter__(self) -> Iterator[Tensor]: ...

    def __abs__(self) -> Tensor: ...

    def __reversed__(self) -> Tensor: ...

    def __getitem__(self, *item) -> Tensor: ...

    def abs(self) -> Tensor: ...

    def abs_(self) -> Tensor: ...

    def acos(self) -> Tensor: ...

    def acos_(self) -> Tensor: ...

    @overload
    def add(self, alpha: builtins.float, other: Tensor) -> Tensor: ...

    @overload
    def add(self, other: Tensor, *, alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def add_(self, alpha: builtins.float, other: Tensor) -> Tensor: ...

    @overload
    def add_(self, other: Tensor, *, alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addbmm(self, beta: builtins.float, alpha: builtins.float,
               batch1: Tensor, batch2: Tensor) -> Tensor: ...

    @overload
    def addbmm(self, beta: builtins.float, batch1: Tensor,
               batch2: Tensor) -> Tensor: ...

    @overload
    def addbmm(self, batch1: Tensor, batch2: Tensor, *,
               beta: builtins.float = 1,
               alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addbmm_(self, beta: builtins.float, alpha: builtins.float,
                batch1: Tensor, batch2: Tensor) -> Tensor: ...

    @overload
    def addbmm_(self, beta: builtins.float, batch1: Tensor,
                batch2: Tensor) -> Tensor: ...

    @overload
    def addbmm_(self, batch1: Tensor, batch2: Tensor, *,
                beta: builtins.float = 1,
                alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addcdiv(self, value: builtins.float, tensor1: Tensor,
                tensor2: Tensor) -> Tensor: ...

    @overload
    def addcdiv(self, tensor1: Tensor, tensor2: Tensor, *,
                value: builtins.float = 1) -> Tensor: ...

    @overload
    def addcdiv_(self, value: builtins.float, tensor1: Tensor,
                 tensor2: Tensor) -> Tensor: ...

    @overload
    def addcdiv_(self, tensor1: Tensor, tensor2: Tensor, *,
                 value: builtins.float = 1) -> Tensor: ...

    @overload
    def addcmul(self, value: builtins.float, tensor1: Tensor,
                tensor2: Tensor) -> Tensor: ...

    @overload
    def addcmul(self, tensor1: Tensor, tensor2: Tensor, *,
                value: builtins.float = 1) -> Tensor: ...

    @overload
    def addcmul_(self, value: builtins.float, tensor1: Tensor,
                 tensor2: Tensor) -> Tensor: ...

    @overload
    def addcmul_(self, tensor1: Tensor, tensor2: Tensor, *,
                 value: builtins.float = 1) -> Tensor: ...

    @overload
    def addmm(self, beta: builtins.float, alpha: builtins.float, mat1: Tensor,
              mat2: Tensor) -> Tensor: ...

    @overload
    def addmm(self, beta: builtins.float, mat1: Tensor,
              mat2: Tensor) -> Tensor: ...

    @overload
    def addmm(self, mat1: Tensor, mat2: Tensor, *, beta: builtins.float = 1,
              alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addmm_(self, beta: builtins.float, alpha: builtins.float, mat1: Tensor,
               mat2: Tensor) -> Tensor: ...

    @overload
    def addmm_(self, beta: builtins.float, mat1: Tensor,
               mat2: Tensor) -> Tensor: ...

    @overload
    def addmm_(self, mat1: Tensor, mat2: Tensor, *, beta: builtins.float = 1,
               alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addmv(self, beta: builtins.float, alpha: builtins.float, mat: Tensor,
              vec: Tensor) -> Tensor: ...

    @overload
    def addmv(self, beta: builtins.float, mat: Tensor,
              vec: Tensor) -> Tensor: ...

    @overload
    def addmv(self, mat: Tensor, vec: Tensor, *, beta: builtins.float = 1,
              alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addmv_(self, beta: builtins.float, alpha: builtins.float, mat: Tensor,
               vec: Tensor) -> Tensor: ...

    @overload
    def addmv_(self, beta: builtins.float, mat: Tensor,
               vec: Tensor) -> Tensor: ...

    @overload
    def addmv_(self, mat: Tensor, vec: Tensor, *, beta: builtins.float = 1,
               alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addr(self, beta: builtins.float, alpha: builtins.float, vec1: Tensor,
             vec2: Tensor) -> Tensor: ...

    @overload
    def addr(self, beta: builtins.float, vec1: Tensor,
             vec2: Tensor) -> Tensor: ...

    @overload
    def addr(self, vec1: Tensor, vec2: Tensor, *, beta: builtins.float = 1,
             alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def addr_(self, beta: builtins.float, alpha: builtins.float, vec1: Tensor,
              vec2: Tensor) -> Tensor: ...

    @overload
    def addr_(self, beta: builtins.float, vec1: Tensor,
              vec2: Tensor) -> Tensor: ...

    @overload
    def addr_(self, vec1: Tensor, vec2: Tensor, *, beta: builtins.float = 1,
              alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def all(self) -> Tensor: ...

    @overload
    def all(self, dim: builtins.int, keepdim: bool = False) -> Tensor: ...

    def allclose(self, other: Tensor, rtol: builtins.float = 1e-05,
                 atol: builtins.float = 1e-08,
                 equal_nan: bool = False) -> bool: ...

    @overload
    def any(self) -> Tensor: ...

    @overload
    def any(self, dim: builtins.int, keepdim: bool = False) -> Tensor: ...

    @overload
    def argmax(self) -> LongTensor: ...

    @overload
    def argmax(self, dim: builtins.int,
               keepdim: bool = False) -> LongTensor: ...

    @overload
    def argmin(self) -> LongTensor: ...

    @overload
    def argmin(self, dim: builtins.int,
               keepdim: bool = False) -> LongTensor: ...

    def argsort(self, dim: builtins.int = -1,
                descending: bool = False) -> LongTensor: ...

    @overload
    def as_strided(self, size: MaybeTuple[builtins.int],
                   stride: MaybeTuple[builtins.int]) -> Tensor: ...

    @overload
    def as_strided(self, size: MaybeTuple[builtins.int],
                   stride: MaybeTuple[builtins.int],
                   storage_offset: Optional[builtins.int] = None) -> Tensor: ...

    @overload
    def as_strided_(self, size: MaybeTuple[builtins.int],
                    stride: MaybeTuple[builtins.int]) -> Tensor: ...

    @overload
    def as_strided_(self, size: MaybeTuple[builtins.int],
                    stride: MaybeTuple[builtins.int],
                    storage_offset: Optional[
                        builtins.int] = None) -> Tensor: ...

    def asin(self) -> Tensor: ...

    def asin_(self) -> Tensor: ...

    def atan(self) -> Tensor: ...

    def atan2(self, other: Tensor) -> Tensor: ...

    def atan2_(self, other: Tensor) -> Tensor: ...

    def atan_(self) -> Tensor: ...

    def backward(self, gradient: Optional[Tensor] = None,
                 retain_graph: Optional[bool] = None,
                 create_graph: bool = False): ...

    @overload
    def baddbmm(self, beta: builtins.float, alpha: builtins.float,
                batch1: Tensor, batch2: Tensor) -> Tensor: ...

    @overload
    def baddbmm(self, beta: builtins.float, batch1: Tensor,
                batch2: Tensor) -> Tensor: ...

    @overload
    def baddbmm(self, batch1: Tensor, batch2: Tensor, *,
                beta: builtins.float = 1,
                alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def baddbmm_(self, beta: builtins.float, alpha: builtins.float,
                 batch1: Tensor, batch2: Tensor) -> Tensor: ...

    @overload
    def baddbmm_(self, beta: builtins.float, batch1: Tensor,
                 batch2: Tensor) -> Tensor: ...

    @overload
    def baddbmm_(self, batch1: Tensor, batch2: Tensor, *,
                 beta: builtins.float = 1,
                 alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def bernoulli(self, *, generator: Optional[Generator] = None) -> Tensor: ...

    @overload
    def bernoulli(self, p: builtins.float, *,
                  generator: Optional[Generator] = None) -> Tensor: ...

    @overload
    def bernoulli_(self, p: Tensor, *,
                   generator: Optional[Generator] = None) -> Tensor: ...

    @overload
    def bernoulli_(self, p: builtins.float = 0.5, *,
                   generator: Optional[Generator] = None) -> Tensor: ...

    def bincount(self, weights: Optional[Tensor] = None,
                 minlength: builtins.int = 0) -> Tensor: ...

    def bmm(self, mat2: Tensor) -> Tensor: ...

    def btrifact(self, info: Optional[IntTensor] = None,  # type: ignore
                 pivot: bool = True) -> Tuple[Tensor, IntTensor]: ...

    def btrifact_with_info(self, *, pivot: bool = True) -> Tuple[
        Tensor, IntTensor, IntTensor]: ...  # type: ignore

    def btrisolve(self, LU_data: Tensor, LU_pivots: Tensor) -> Tensor: ...

    def cauchy_(self, median: builtins.float = 0, sigma: builtins.float = 1, *,
                generator: Optional[Generator] = None) -> Tensor: ...

    def ceil(self) -> Tensor: ...

    def ceil_(self) -> Tensor: ...

    def chunk(self, chunks: builtins.int, dim: builtins.int = 0) -> MaybeTuple[
        Tensor]: ...

    def clamp(self, min: Optional[builtins.float] = None,
              max: Optional[builtins.float] = None) -> Tensor: ...

    def clamp_(self, min: Optional[builtins.float] = None,
               max: Optional[builtins.float] = None) -> Tensor: ...

    def clamp_max(self, max: builtins.float) -> Tensor: ...

    def clamp_max_(self, max: builtins.float) -> Tensor: ...

    def clamp_min(self, min: builtins.float) -> Tensor: ...

    def clamp_min_(self, min: builtins.float) -> Tensor: ...

    def clone(self) -> Tensor: ...

    def coalesce(self) -> Tensor: ...

    def contiguous(self) -> Tensor: ...

    def cos(self) -> Tensor: ...

    def cos_(self) -> Tensor: ...

    def cosh(self) -> Tensor: ...

    def cosh_(self) -> Tensor: ...

    def cross(self, other: Tensor, dim: builtins.int = -1) -> Tensor: ...

    def cumprod(self, dim: builtins.int, *,
                dtype: Optional[_dtype] = None) -> Tensor: ...

    def cumsum(self, dim: builtins.int, *,
               dtype: Optional[_dtype] = None) -> Tensor: ...

    def data_ptr(self) -> builtins.int: ...

    def det(self) -> Tensor: ...

    def detach(self) -> Tensor: ...

    def detach_(self) -> Tensor: ...

    def diag(self, diagonal: builtins.int = 0) -> Tensor: ...

    def diagflat(self, offset: builtins.int = 0) -> Tensor: ...

    def diagonal(self, offset: builtins.int = 0, dim1: builtins.int = 0,
                 dim2: builtins.int = 1) -> Tensor: ...

    def digamma(self) -> Tensor: ...

    def digamma_(self) -> Tensor: ...

    def dim(self) -> builtins.int: ...

    def dist(self, other: Tensor, p: builtins.float = 2) -> Tensor: ...

    def div(self, other: Union[builtins.float, Tensor]) -> Tensor: ...

    def div_(self, other: Union[builtins.float, Tensor]) -> Tensor: ...

    def dot(self, tensor: Tensor) -> Tensor: ...

    def double(self) -> DoubleTensor: ...

    def eig(self, eigenvectors: bool = False) -> Tuple[Tensor, Tensor]: ...

    @overload
    def eq(self, other: Tensor) -> Tensor: ...

    @overload
    def eq(self, other: builtins.float) -> Tensor: ...

    @overload
    def eq_(self, other: Tensor) -> Tensor: ...

    @overload
    def eq_(self, other: builtins.float) -> Tensor: ...

    def equal(self, other: Tensor) -> bool: ...

    def erf(self) -> Tensor: ...

    def erf_(self) -> Tensor: ...

    def erfc(self) -> Tensor: ...

    def erfc_(self) -> Tensor: ...

    def erfinv(self) -> Tensor: ...

    def erfinv_(self) -> Tensor: ...

    def exp(self) -> Tensor: ...

    def exp_(self) -> Tensor: ...

    @overload
    def expand(self, *size: builtins.int, implicit: bool = False) -> Tensor: ...

    @overload
    def expand(self, size: MaybeTuple[builtins.int],
               implicit: bool = False) -> Tensor: ...

    def expand_as(self, other: Tensor) -> Tensor: ...

    def expm1(self) -> Tensor: ...

    def expm1_(self) -> Tensor: ...

    def exponential_(self, lambd: builtins.float = 1, *,
                     generator: Optional[Generator] = None) -> Tensor: ...

    def fft(self, signal_ndim: builtins.int,
            normalized: bool = False) -> Tensor: ...

    @overload
    def fill_(self, value: Tensor) -> Tensor: ...

    @overload
    def fill_(self, value: builtins.float) -> Tensor: ...

    def flatten(self, start_dim: builtins.int = 0,
                end_dim: builtins.int = -1) -> Tensor: ...

    def flip(self, dims: MaybeTuple[builtins.int]) -> Tensor: ...

    def float(self) -> FloatTensor: ...

    def floor(self) -> Tensor: ...

    def floor_(self) -> Tensor: ...

    @overload
    def fmod(self, other: Tensor) -> Tensor: ...

    @overload
    def fmod(self, other: builtins.float) -> Tensor: ...

    @overload
    def fmod_(self, other: Tensor) -> Tensor: ...

    @overload
    def fmod_(self, other: builtins.float) -> Tensor: ...

    def frac(self) -> Tensor: ...

    def frac_(self) -> Tensor: ...

    def gather(self, dim: builtins.int, index: Tensor) -> Tensor: ...

    @overload
    def ge(self, other: Tensor) -> Tensor: ...

    @overload
    def ge(self, other: builtins.float) -> Tensor: ...

    @overload
    def ge_(self, other: Tensor) -> Tensor: ...

    @overload
    def ge_(self, other: builtins.float) -> Tensor: ...

    def gels(self, A: Tensor) -> Tuple[Tensor, Tensor]: ...

    def geometric_(self, p: builtins.float, *,
                   generator: Optional[Generator] = None) -> Tensor: ...

    def geqrf(self) -> Tuple[Tensor, Tensor]: ...

    def ger(self, vec2: Tensor) -> Tensor: ...

    def gesv(self, A: Tensor) -> Tuple[Tensor, Tensor]: ...

    def get_device(self) -> builtins.int: ...

    @overload
    def gt(self, other: Tensor) -> Tensor: ...

    @overload
    def gt(self, other: builtins.float) -> Tensor: ...

    @overload
    def gt_(self, other: Tensor) -> Tensor: ...

    @overload
    def gt_(self, other: builtins.float) -> Tensor: ...

    def half(self) -> HalfTensor: ...

    def hardshrink(self, lambd: builtins.float = 0.5) -> Tensor: ...

    def histc(self, bins: builtins.int = 100, min: builtins.float = 0,
              max: builtins.float = 0) -> Tensor: ...

    def ifft(self, signal_ndim: builtins.int,
             normalized: bool = False) -> Tensor: ...

    def index_add(self, dim: builtins.int, index: Tensor,
                  source: Tensor) -> Tensor: ...

    def index_add_(self, dim: builtins.int, index: Tensor,
                   source: Tensor) -> Tensor: ...

    def index_copy(self, dim: builtins.int, index: Tensor,
                   source: Tensor) -> Tensor: ...

    def index_copy_(self, dim: builtins.int, index: Tensor,
                    source: Tensor) -> Tensor: ...

    def index_fill(self, dim: builtins.int, index: Tensor,
                   value: Union[Tensor, builtins.float]) -> Tensor: ...

    def index_fill_(self, dim: builtins.int, index: Tensor,
                    value: Union[Tensor, builtins.float]) -> Tensor: ...

    def index_put(self, indices: MaybeTuple[Tensor],
                  values: Tensor) -> Tensor: ...

    def index_put_(self, indices: MaybeTuple[Tensor],
                   values: Tensor) -> Tensor: ...

    def index_select(self, dim: builtins.int, index: Tensor) -> Tensor: ...

    def int(self) -> IntTensor: ...

    def inverse(self) -> Tensor: ...

    def irfft(self, signal_ndim: builtins.int, normalized: bool = False,
              onesided: bool = True,
              signal_sizes: Optional[
                  MaybeTuple[builtins.int]] = None) -> Tensor: ...

    def is_coalesced(self) -> bool: ...

    def is_complex(self) -> bool: ...

    def is_contiguous(self) -> bool: ...

    def is_distributed(self) -> bool: ...

    def is_floating_point(self) -> bool: ...

    def is_nonzero(self) -> bool: ...

    def is_pinned(self) -> bool: ...

    def is_same_size(self, other: Tensor) -> bool: ...

    def is_set_to(self, tensor: Tensor) -> bool: ...

    def is_shared(self) -> bool: ...

    def is_signed(self) -> bool: ...

    def isclose(self, other: Tensor, rtol: builtins.float = 1e-05,
                atol: builtins.float = 1e-08,
                equal_nan: bool = False) -> Tensor: ...

    def kthvalue(self, k: builtins.int, dim: builtins.int = -1,
                 keepdim: bool = False) -> Tuple[Tensor, Tensor]: ...

    @overload
    def le(self, other: Tensor) -> Tensor: ...

    @overload
    def le(self, other: builtins.float) -> Tensor: ...

    @overload
    def le_(self, other: Tensor) -> Tensor: ...

    @overload
    def le_(self, other: builtins.float) -> Tensor: ...

    def lerp(self, end: Tensor, weight: builtins.float) -> Tensor: ...

    def lerp_(self, end: Tensor, weight: builtins.float) -> Tensor: ...

    def lgamma(self) -> Tensor: ...

    def lgamma_(self) -> Tensor: ...

    def log(self) -> Tensor: ...

    def log10(self) -> Tensor: ...

    def log10_(self) -> Tensor: ...

    def log1p(self) -> Tensor: ...

    def log1p_(self) -> Tensor: ...

    def log2(self) -> Tensor: ...

    def log2_(self) -> Tensor: ...

    def log_(self) -> Tensor: ...

    def log_normal_(self, mean: builtins.float = 1, std: builtins.float = 2, *,
                    generator: Optional[Generator] = None) -> Tensor: ...

    def log_softmax(self, dim: builtins.int) -> Tensor: ...

    def logdet(self) -> Tensor: ...

    def logsumexp(self, dim: builtins.int, keepdim: bool = False) -> Tensor: ...

    def long(self) -> LongTensor: ...

    @overload
    def lt(self, other: Tensor) -> Tensor: ...

    @overload
    def lt(self, other: builtins.float) -> Tensor: ...

    @overload
    def lt_(self, other: Tensor) -> Tensor: ...

    @overload
    def lt_(self, other: builtins.float) -> Tensor: ...

    def masked_fill(self, mask: Tensor,
                    value: Union[builtins.float, Tensor]) -> Tensor: ...

    def masked_fill_(self, mask: Tensor,
                     value: Union[builtins.float, Tensor]) -> Tensor: ...

    def masked_scatter(self, mask: Tensor, source: Tensor) -> Tensor: ...

    def masked_scatter_(self, mask: Tensor, source: Tensor) -> Tensor: ...

    def masked_select(self, mask: Tensor) -> Tensor: ...

    def matmul(self, other: Tensor) -> Tensor: ...

    def matrix_power(self, n: builtins.int) -> Tensor: ...

    @overload
    def max(self) -> Tensor: ...

    @overload
    def max(self, other: Tensor) -> Tensor: ...

    @overload
    def max(self, dim: builtins.int, keepdim: bool = False) -> Tuple[
        Tensor, Tensor]: ...

    @overload
    def mean(self) -> Tensor: ...

    @overload
    def mean(self, *, dtype: _dtype) -> Tensor: ...

    @overload
    def mean(self, dim: builtins.int, *, dtype: _dtype) -> Tensor: ...

    @overload
    def mean(self, dim: builtins.int, keepdim: bool, *,
             dtype: _dtype) -> Tensor: ...

    @overload
    def mean(self, dim: builtins.int, keepdim: bool = False) -> Tensor: ...

    @overload
    def median(self) -> Tensor: ...

    @overload
    def median(self, dim: builtins.int, keepdim: bool = False) -> Tuple[
        Tensor, Tensor]: ...

    @overload
    def min(self) -> Tensor: ...

    @overload
    def min(self, other: Tensor) -> Tensor: ...

    @overload
    def min(self, dim: builtins.int, keepdim: bool = False) -> Tuple[
        Tensor, Tensor]: ...

    def mm(self, mat2: Tensor) -> Tensor: ...

    def mode(self, dim: builtins.int = -1, keepdim: bool = False) -> Tuple[
        Tensor, Tensor]: ...

    def mul(self, other: Union[builtins.float, Tensor]) -> Tensor: ...

    def mul_(self, other: Union[builtins.float, Tensor]) -> Tensor: ...

    def multinomial(self, num_samples: builtins.int, replacement: bool = False,
                    *,
                    generator: Optional[Generator] = None) -> Tensor: ...

    def mv(self, vec: Tensor) -> Tensor: ...

    def mvlgamma(self, p: builtins.int) -> Tensor: ...

    def mvlgamma_(self, p: builtins.int) -> Tensor: ...

    def narrow(self, dim: builtins.int, start: builtins.int,
               length: builtins.int) -> Tensor: ...

    @overload
    def ne(self, other: Tensor) -> Tensor: ...

    @overload
    def ne(self, other: builtins.float) -> Tensor: ...

    @overload
    def ne_(self, other: Tensor) -> Tensor: ...

    @overload
    def ne_(self, other: builtins.float) -> Tensor: ...

    def neg(self) -> Tensor: ...

    def neg_(self) -> Tensor: ...

    def new_tensor(self, data, dtype: Optional[_dtype] = None,
                   device: Union[_device, str, None] = None,
                   requires_grad: bool = False) -> Tensor: ...

    def new_full(self, size: MaybeTuple[builtins.int],
                 fill_value: builtins.float, dtype: Optional[_dtype] = None,
                 device: Union[_device, str, None] = None,
                 requires_grad: bool = False) -> Tensor: ...

    @overload
    def new_empty(self, size: MaybeTuple[builtins.int],
                  dtype: Optional[_dtype] = None,
                  device: Union[_device, str, None] = None,
                  requires_grad: bool = False) -> Tensor: ...

    @overload
    def new_empty(self, *size: builtins.int, dtype: Optional[_dtype] = None,
                  device: Union[_device, str, None] = None,
                  requires_grad: bool = False) -> Tensor: ...

    @overload
    def new_ones(self, size: MaybeTuple[builtins.int],
                 dtype: Optional[_dtype] = None,
                 device: Union[_device, str, None] = None,
                 requires_grad: bool = False) -> Tensor: ...

    @overload
    def new_ones(self, *size: builtins.int, dtype: Optional[_dtype] = None,
                 device: Union[_device, str, None] = None,
                 requires_grad: bool = False) -> Tensor: ...

    @overload
    def new_zeros(self, size: MaybeTuple[builtins.int],
                  dtype: Optional[_dtype] = None,
                  device: Union[_device, str, None] = None,
                  requires_grad: bool = False) -> Tensor: ...

    @overload
    def new_zeros(self, *size: builtins.int, dtype: Optional[_dtype] = None,
                  device: Union[_device, str, None] = None,
                  requires_grad: bool = False) -> Tensor: ...

    def nonzero(self) -> Tensor: ...

    def norm(self, p: Union[builtins.float, str, None] = 'fro',
             dim: Optional[builtins.int] = None,  # type: ignore
             keepdim: bool = False) -> Tensor: ...

    def normal_(self, mean: builtins.float = 0, std: builtins.float = 1, *,
                generator: Optional[Generator] = None) -> Tensor: ...

    def numel(self) -> builtins.int: ...

    def orgqr(self, input2: Tensor) -> Tensor: ...

    def ormqr(self, input2: Tensor, input3: Tensor, left: bool = True,
              transpose: bool = False) -> Tensor: ...

    @overload
    def permute(self, *dims: builtins.int) -> Tensor: ...

    @overload
    def permute(self, dims: MaybeTuple[builtins.int]) -> Tensor: ...

    def pin_memory(self) -> Tensor: ...

    def pinverse(self, rcond: builtins.float = 1e-15) -> Tensor: ...

    def polygamma(self, n: builtins.int, ) -> Tensor: ...

    def polygamma_(self, n: builtins.int) -> Tensor: ...

    def potrf(self, upper: bool = True) -> Tensor: ...

    def potri(self, upper: bool = True) -> Tensor: ...

    def potrs(self, input2: Tensor, upper: bool = True) -> Tensor: ...

    @overload
    def pow(self, exponent: Tensor) -> Tensor: ...

    @overload
    def pow(self, exponent: builtins.float) -> Tensor: ...

    @overload
    def pow_(self, exponent: Tensor) -> Tensor: ...

    @overload
    def pow_(self, exponent: builtins.float) -> Tensor: ...

    def prelu(self, weight: Tensor) -> Tensor: ...

    @overload
    def prod(self) -> Tensor: ...

    @overload
    def prod(self, *, dtype: _dtype) -> Tensor: ...

    @overload
    def prod(self, dim: builtins.int, *, dtype: _dtype) -> Tensor: ...

    @overload
    def prod(self, dim: builtins.int, keepdim: bool, *,
             dtype: _dtype) -> Tensor: ...

    @overload
    def prod(self, dim: builtins.int, keepdim: bool = False) -> Tensor: ...

    def pstrf(self, upper: bool = True, tol: builtins.float = -1) -> Tuple[
        Tensor, Tensor]: ...

    def put_(self, index: Tensor, source: Tensor,
             accumulate: bool = False) -> Tensor: ...

    def qr(self) -> Tuple[Tensor, Tensor]: ...

    @overload
    def random_(self, *, generator: Optional[Generator] = None) -> Tensor: ...

    @overload
    def random_(self, from_: builtins.int, to: builtins.int, *,
                generator: Optional[Generator] = None) -> Tensor: ...

    @overload
    def random_(self, to: builtins.int, *,
                generator: Optional[Generator] = None) -> Tensor: ...

    def reciprocal(self) -> Tensor: ...

    def reciprocal_(self) -> Tensor: ...

    def register_hook(self, hook: Callable[
        [Tensor], Optional[Tensor]]) -> RemovableHandle: ...

    def relu(self) -> Tensor: ...

    def relu_(self) -> Tensor: ...

    @overload
    def remainder(self, other: Tensor) -> Tensor: ...

    @overload
    def remainder(self, other: builtins.float) -> Tensor: ...

    @overload
    def remainder_(self, other: Tensor) -> Tensor: ...

    @overload
    def remainder_(self, other: builtins.float) -> Tensor: ...

    def renorm(self, p: builtins.float, dim: builtins.int,
               maxnorm: builtins.float) -> Tensor: ...

    def renorm_(self, p: builtins.float, dim: builtins.int,
                maxnorm: builtins.float) -> Tensor: ...

    @overload
    def repeat(self, *repeats: builtins.int) -> Tensor: ...

    @overload
    def repeat(self, repeats: Tuple[builtins.int, ...]) -> Tensor: ...

    @overload
    def reshape(self, *shape: builtins.int) -> Tensor: ...

    @overload
    def reshape(self, shape: Tuple[builtins.int, ...]) -> Tensor: ...

    def reshape_as(self, other: Tensor) -> Tensor: ...

    def resize_(self, *size: builtins.int) -> Tensor: ...

    def resize_as_(self, the_template: Tensor) -> Tensor: ...

    def retain_grad(self) -> None: ...

    def rfft(self, signal_ndim: builtins.int, normalized: bool = False,
             onesided: bool = True) -> Tensor: ...

    def round(self) -> Tensor: ...

    def round_(self) -> Tensor: ...

    def rsqrt(self) -> Tensor: ...

    def rsqrt_(self) -> Tensor: ...

    def scatter(self, dim: builtins.int, index: LongTensor,
                value: Union[Tensor, builtins.float]) -> Tensor: ...

    def scatter_(self, dim: builtins.int, index: LongTensor,
                 value: Union[Tensor, builtins.float]) -> Tensor: ...

    def scatter_add(self, dim: builtins.int, index: LongTensor,
                    src: Tensor) -> Tensor: ...

    def scatter_add_(self, dim: builtins.int, index: LongTensor,
                     src: Tensor) -> Tensor: ...

    def select(self, dim: builtins.int, index: builtins.int) -> Tensor: ...

    @overload
    def set_(self) -> Tensor: ...

    @overload
    def set_(self, source: Union[Tensor, _StorageBase]) -> Tensor: ...

    @overload
    def set_(self, source: _StorageBase, storage_offset: builtins.int,
             size: MaybeTuple[builtins.int],
             stride: Optional[MaybeTuple[builtins.int]] = None) -> Tensor: ...

    def share_memory_(self) -> Tensor: ...

    @property
    def shape(self) -> Size: ...

    def sigmoid(self) -> Tensor: ...

    def sigmoid_(self) -> Tensor: ...

    def sign(self) -> Tensor: ...

    def sign_(self) -> Tensor: ...

    def sin(self) -> Tensor: ...

    def sin_(self) -> Tensor: ...

    def sinh(self) -> Tensor: ...

    def sinh_(self) -> Tensor: ...

    @overload
    def size(self) -> Size: ...

    @overload
    def size(self, dim: builtins.int) -> builtins.int: ...

    def slogdet(self) -> Tuple[Tensor, Tensor]: ...

    def smm(self, mat2: Tensor) -> Tensor: ...

    def softmax(self, dim: builtins.int) -> Tensor: ...

    def sort(self, dim: builtins.int = -1, descending: bool = False) -> Tuple[
        Tensor, Tensor]: ...

    def sparse_mask(self, mask: Tensor) -> Tensor: ...

    def sparse_resize_(self, size: MaybeTuple[builtins.int],
                       sparseDims: builtins.int,
                       denseDims: builtins.int) -> Tensor: ...

    def sparse_resize_and_clear_(self, size: MaybeTuple[builtins.int],
                                 sparseDims: builtins.int,
                                 denseDims: builtins.int) -> Tensor: ...

    def split(tensor: Tensor, split_size_or_sections: MaybeList[builtins.int],
              dim: builtins.int = 0) -> Tuple[Tensor, ...]: ...

    def sqrt(self) -> Tensor: ...

    def sqrt_(self) -> Tensor: ...

    @overload
    def squeeze(self) -> Tensor: ...

    @overload
    def squeeze(self, dim: builtins.int) -> Tensor: ...

    @overload
    def squeeze_(self) -> Tensor: ...

    @overload
    def squeeze_(self, dim: builtins.int) -> Tensor: ...

    @overload
    def sspaddmm(self, beta: builtins.float, alpha: builtins.float,
                 mat1: Tensor, mat2: Tensor) -> Tensor: ...

    @overload
    def sspaddmm(self, beta: builtins.float, mat1: Tensor,
                 mat2: Tensor) -> Tensor: ...

    @overload
    def sspaddmm(self, mat1: Tensor, mat2: Tensor, *, beta: builtins.float = 1,
                 alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def std(self, unbiased: bool = True) -> Tensor: ...

    @overload
    def std(self, dim: builtins.int, unbiased: bool = True,
            keepdim: bool = False) -> Tensor: ...

    def stft(self, n_fft: builtins.int,
             hop_length: Optional[builtins.int] = None,
             win_length: Optional[builtins.int] = None,
             window: Optional[Tensor] = None, center: bool = True,
             pad_mode: str = 'reflect', normalized: bool = False,
             onesided: bool = True) -> Tensor: ...

    def storage_offset(self) -> builtins.int: ...

    @overload
    def sub(self, alpha: builtins.float, other: Tensor) -> Tensor: ...

    @overload
    def sub(self, other: Tensor, *, alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def sub_(self, alpha: builtins.float, other: Tensor) -> Tensor: ...

    @overload
    def sub_(self, other: Tensor, *, alpha: builtins.float = 1) -> Tensor: ...

    @overload
    def sum(self) -> Tensor: ...

    @overload
    def sum(self, *, dtype: _dtype) -> Tensor: ...

    @overload
    def sum(self, dim: MaybeTuple[builtins.int], *,
            dtype: _dtype) -> Tensor: ...

    @overload
    def sum(self, dim: MaybeTuple[builtins.int], keepdim: bool, *,
            dtype: _dtype) -> Tensor: ...

    @overload
    def sum(self, dim: MaybeTuple[builtins.int],
            keepdim: bool = False) -> Tensor: ...

    def svd(self, some: bool = True) -> Tuple[Tensor, Tensor, Tensor]: ...

    def symeig(self, eigenvectors: bool = False, upper: bool = True) -> Tuple[
        Tensor, Tensor]: ...

    def t(self) -> Tensor: ...

    def t_(self) -> Tensor: ...

    def take(self, index: Tensor) -> Tensor: ...

    def tan(self) -> Tensor: ...

    def tan_(self) -> Tensor: ...

    def tanh(self) -> Tensor: ...

    def tanh_(self) -> Tensor: ...

    @overload
    def to(self, dtype: _dtype) -> Tensor: ...

    @overload
    def to(self, device: Union[_device, str]) -> Tensor: ...

    @overload
    def to(self, device: Union[_device, str, None] = None,
           dtype: Optional[_dtype] = None,
           non_blocking: bool = False) -> Tensor: ...

    @overload
    def to(self, other: Tensor, non_blocking: bool = False) -> Tensor: ...

    def to_dense(self) -> Tensor: ...

    def topk(self, k: builtins.int, dim: builtins.int = -1,
             largest: bool = True, sorted: bool = True) -> Tuple[
        Tensor, Tensor]: ...

    def trace(self) -> Tensor: ...

    def transpose(self, dim0: builtins.int, dim1: builtins.int) -> Tensor: ...

    def transpose_(self, dim0: builtins.int, dim1: builtins.int) -> Tensor: ...

    def tril(self, diagonal: builtins.int = 0) -> Tensor: ...

    def tril_(self, diagonal: builtins.int = 0) -> Tensor: ...

    def triu(self, diagonal: builtins.int = 0) -> Tensor: ...

    def triu_(self, diagonal: builtins.int = 0) -> Tensor: ...

    def trtrs(self, A: Tensor, upper: bool = True, transpose: bool = False,
              unitriangular: bool = False) -> Tuple[Tensor, Tensor]: ...

    def trunc(self) -> Tensor: ...

    def trunc_(self) -> Tensor: ...

    def type(self, dtype: _dtype) -> Tensor: ...

    def type_as(self, other: Tensor) -> Tensor: ...

    def unbind(self, dim: builtins.int = 0) -> MaybeTuple[Tensor]: ...

    def unfold(self, dimension: builtins.int, size: builtins.int,
               step: builtins.int) -> Tensor: ...

    def uniform_(self, from_: builtins.float = 0, to: builtins.float = 1, *,
                 generator: Optional[Generator] = None) -> Tensor: ...

    def unsqueeze(self, dim: builtins.int) -> Tensor: ...

    def unsqueeze_(self, dim: builtins.int) -> Tensor: ...

    @overload
    def var(self, unbiased: bool = True) -> Tensor: ...

    @overload
    def var(self, dim: builtins.int, unbiased: bool = True,
            keepdim: bool = False) -> Tensor: ...

    @overload
    def view(self, *size: builtins.int) -> Tensor: ...

    @overload
    def view(self, size: MaybeTuple[builtins.int]) -> Tensor: ...

    def view_as(self, other: Tensor) -> Tensor: ...

    def where(self, condition: Tensor, other: Tensor) -> Tensor: ...

    def zero_(self) -> Tensor: ...


FloatTensor = Tensor


class DoubleTensor(Tensor): ...


class HalfTensor(Tensor): ...


class ByteTensor(Tensor): ...


class ShortTensor(Tensor): ...


class IntTensor(Tensor): ...


class LongTensor(Tensor): ...


def tensor(data, dtype: Optional[dtype] = None,
           device: Union[device, str, None] = None,
           requires_grad: bool = False) -> Tensor: ...


def abs(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def abs_(input: Tensor) -> Tensor: ...


def acos(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def acos_(input: Tensor) -> Tensor: ...


def adaptive_avg_pool1d(input: Tensor,
                        output_size: MaybeTuple[builtins.int]) -> Tensor: ...


def adaptive_max_pool1d(input: Tensor, output_size: MaybeTuple[builtins.int]) -> \
Tuple[Tensor, Tensor]: ...


@overload
def add(input: Tensor, alpha: builtins.float, other: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def add(input: Tensor, other: Tensor, *, alpha: builtins.float = 1,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addbmm(beta: builtins.float, self: Tensor, alpha: builtins.float,
           batch1: Tensor, batch2: Tensor, *,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addbmm(beta: builtins.float, self: Tensor, batch1: Tensor, batch2: Tensor,
           *,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addbmm(input: Tensor, batch1: Tensor, batch2: Tensor, *,
           beta: builtins.float = 1, alpha: builtins.float = 1,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addcdiv(input: Tensor, value: builtins.float, tensor1: Tensor,
            tensor2: Tensor, *,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addcdiv(input: Tensor, tensor1: Tensor, tensor2: Tensor, *,
            value: builtins.float = 1,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addcmul(input: Tensor, value: builtins.float, tensor1: Tensor,
            tensor2: Tensor, *,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addcmul(input: Tensor, tensor1: Tensor, tensor2: Tensor, *,
            value: builtins.float = 1,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmm(beta: builtins.float, self: Tensor, alpha: builtins.float,
          mat1: Tensor, mat2: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmm(beta: builtins.float, self: Tensor, mat1: Tensor, mat2: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmm(input: Tensor, mat1: Tensor, mat2: Tensor, *,
          beta: builtins.float = 1, alpha: builtins.float = 1,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmv(beta: builtins.float, self: Tensor, alpha: builtins.float,
          mat: Tensor, vec: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmv(beta: builtins.float, self: Tensor, mat: Tensor, vec: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmv(input: Tensor, mat: Tensor, vec: Tensor, *, beta: builtins.float = 1,
          alpha: builtins.float = 1,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addmv_(beta: builtins.float, self: Tensor, alpha: builtins.float,
           mat: Tensor, vec: Tensor) -> Tensor: ...


@overload
def addmv_(beta: builtins.float, self: Tensor, mat: Tensor,
           vec: Tensor) -> Tensor: ...


@overload
def addmv_(input: Tensor, mat: Tensor, vec: Tensor, *, beta: builtins.float = 1,
           alpha: builtins.float = 1) -> Tensor: ...


@overload
def addr(beta: builtins.float, self: Tensor, alpha: builtins.float,
         vec1: Tensor, vec2: Tensor, *,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addr(beta: builtins.float, self: Tensor, vec1: Tensor, vec2: Tensor, *,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def addr(input: Tensor, vec1: Tensor, vec2: Tensor, *, beta: builtins.float = 1,
         alpha: builtins.float = 1,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def all(input: Tensor) -> Tensor: ...


@overload
def all(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def allclose(input: Tensor, other: Tensor, rtol: builtins.float = 1e-05,
             atol: builtins.float = 1e-08,
             equal_nan: bool = False) -> bool: ...


def alpha_dropout(input: Tensor, p: builtins.float, train: bool) -> Tensor: ...


def alpha_dropout_(input: Tensor, p: builtins.float, train: bool) -> Tensor: ...


@overload
def any(input: Tensor) -> Tensor: ...


@overload
def any(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def arange(start: Union[builtins.int, builtins.float],
           end: Union[builtins.int, builtins.float],
           step: Union[builtins.int, builtins.float] = 1,
           out: Optional[Tensor] = None,
           dtype: Optional[dtype] = None, layout: Type[layout] = strided,
           device: Union[device, str, None] = None,
           requires_grad: bool = False) -> Tensor: ...


@overload
def arange(end: Union[builtins.int, builtins.float],
           step: Union[builtins.int, builtins.float] = 1,
           out: Optional[Tensor] = None, dtype: Optional[dtype] = None,
           layout: Type[layout] = strided,
           device: Union[_device, str, None] = None,
           requires_grad: bool = False) -> Tensor: ...


@overload
def argmax(input: Tensor) -> LongTensor: ...


@overload
def argmax(input: Tensor, dim: builtins.int,
           keepdim: bool = False) -> LongTensor: ...


@overload
def argmin(input: Tensor) -> LongTensor: ...


@overload
def argmin(input: Tensor, dim: builtins.int,
           keepdim: bool = False) -> LongTensor: ...


@overload
def as_strided(input: Tensor, size: MaybeTuple[builtins.int],
               stride: MaybeTuple[builtins.int]) -> Tensor: ...


@overload
def as_strided(input: Tensor, size: MaybeTuple[builtins.int],
               stride: MaybeTuple[builtins.int],
               storage_offset: Optional[builtins.int] = None) -> Tensor: ...


@overload
def as_strided_(input: Tensor, size: MaybeTuple[builtins.int],
                stride: MaybeTuple[builtins.int]) -> Tensor: ...


@overload
def as_strided_(input: Tensor, size: MaybeTuple[builtins.int],
                stride: MaybeTuple[builtins.int],
                storage_offset: Optional[builtins.int] = None) -> Tensor: ...


def asin(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def asin_(input: Tensor) -> Tensor: ...


def atan(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def atan2(input: Tensor, other: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def atan_(input: Tensor) -> Tensor: ...


def avg_pool1d(input: Tensor, kernel_size: Optional[MaybeTuple[builtins.int]],
               stride: Optional[MaybeTuple[builtins.int]] = None,
               padding: Optional[MaybeTuple[builtins.int]] = 0,
               ceil_mode: bool = False,
               count_include_pad: bool = True) -> Tensor: ...


@overload
def baddbmm(beta: builtins.float, self: Tensor, alpha: builtins.float,
            batch1: Tensor, batch2: Tensor, *,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def baddbmm(beta: builtins.float, self: Tensor, batch1: Tensor, batch2: Tensor,
            *,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def baddbmm(input: Tensor, batch1: Tensor, batch2: Tensor, *,
            beta: builtins.float = 1, alpha: builtins.float = 1,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def bartlett_window(window_length: builtins.int, *,
                    dtype: Optional[dtype] = None,
                    layout: Type[layout] = strided,
                    device: Union[device, str, None] = None,
                    requires_grad: bool = False) -> Tensor: ...


@overload
def bartlett_window(window_length: builtins.int, periodic: bool, *,
                    dtype: Optional[dtype] = None,
                    layout: Type[layout] = strided,
                    device: Union[device, str, None] = None,
                    requires_grad: bool = False) -> Tensor: ...


def batch_norm(input: Tensor, weight: Optional[Tensor], bias: Optional[Tensor],
               running_mean: Optional[Tensor],
               running_var: Optional[Tensor], training: bool,
               momentum: builtins.float, eps: builtins.float,
               cudnn_enabled: bool) -> Tensor: ...


def bernoulli(input: Tensor, *, generator: Optional[Generator] = None,
              out: Optional[Tensor] = None) -> Tensor: ...


def bilinear(input1: Tensor, input2: Tensor, weight: Tensor,
             bias: Optional[Tensor]) -> Tensor: ...


def bincount(input: Tensor, weights: Optional[Tensor] = None,
             minlength: builtins.int = 0) -> Tensor: ...


@overload
def blackman_window(window_length: builtins.int, *,
                    dtype: Optional[dtype] = None,
                    layout: Type[layout] = strided,
                    device: Union[device, str, None] = None,
                    requires_grad: bool = False) -> Tensor: ...


@overload
def blackman_window(window_length: builtins.int, periodic: bool, *,
                    dtype: Optional[dtype] = None,
                    layout: Type[layout] = strided,
                    device: Union[device, str, None] = None,
                    requires_grad: bool = False) -> Tensor: ...


def bmm(input: Tensor, mat2: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def broadcast_tensors(tensors: Sequence[Tensor]) -> MaybeTuple[Tensor]: ...


def btrifact(input: Tensor, *, pivot: bool = True,
             out: Optional[Tuple[Tensor, IntTensor]]) \
        -> Tuple[Tensor, IntTensor]: ...


def btrifact_with_info(input: Tensor, *, pivot: bool = True,
                       out: Optional[Tuple[Tensor, IntTensor, IntTensor]]) -> \
Tuple[Tensor, IntTensor, IntTensor]: ...


def btrisolve(input: Tensor, LU_data: Tensor, LU_pivots: Tensor, *,
              out: Optional[Tensor] = None) -> Tensor: ...


def cat(tensors: Sequence[Tensor], dim: builtins.int = 0, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def ceil(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def ceil_(input: Tensor) -> Tensor: ...


def celu(input: Tensor, alpha: builtins.float = 1.0) -> Tensor: ...


def celu_(input: Tensor, alpha: builtins.float = 1.0) -> Tensor: ...


def chunk(input: Tensor, chunks: builtins.int, dim: builtins.int = 0) -> \
MaybeTuple[Tensor]: ...


def clamp(input: Tensor, min: Optional[builtins.float] = None,
          max: Optional[builtins.float] = None, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def clamp_(input: Tensor, min: Optional[builtins.float] = None,
           max: Optional[builtins.float] = None) -> Tensor: ...


def clamp_max(input: Tensor, max: builtins.float, *,
              out: Optional[Tensor] = None) -> Tensor: ...


def clamp_max_(input: Tensor, max: builtins.float) -> Tensor: ...


def clamp_min(input: Tensor, min: builtins.float, *,
              out: Optional[Tensor] = None) -> Tensor: ...


def clamp_min_(input: Tensor, min: builtins.float) -> Tensor: ...


def clone(input: Tensor) -> Tensor: ...


def conv1d(input: Tensor, weight: Tensor, bias: Optional[Tensor] = None,
           stride: MaybeTuple[builtins.int] = 1,
           padding: MaybeTuple[builtins.int] = 0,
           dilation: MaybeTuple[builtins.int] = 1,
           groups: builtins.int = 1) -> Tensor: ...


def conv2d(input: Tensor, weight: Tensor, bias: Optional[Tensor] = None,
           stride: MaybeTuple[builtins.int] = 1,
           padding: MaybeTuple[builtins.int] = 0,
           dilation: MaybeTuple[builtins.int] = 1,
           groups: builtins.int = 1) -> Tensor: ...


def conv3d(input: Tensor, weight: Tensor, bias: Optional[Tensor] = None,
           stride: MaybeTuple[builtins.int] = 1,
           padding: MaybeTuple[builtins.int] = 0,
           dilation: MaybeTuple[builtins.int] = 1,
           groups: builtins.int = 1) -> Tensor: ...


def conv_tbc(input: Tensor, weight: Tensor, bias: Tensor,
             pad: builtins.int = 0) -> Tensor: ...


def conv_transpose1d(input: Tensor, weight: Tensor,
                     bias: Optional[Tensor] = None,
                     stride: MaybeTuple[builtins.int] = 1,
                     padding: MaybeTuple[builtins.int] = 0,
                     output_padding: MaybeTuple[builtins.int] = 0,
                     groups: builtins.int = 1,
                     dilation: MaybeTuple[builtins.int] = 1) -> Tensor: ...


def conv_transpose2d(input: Tensor, weight: Tensor,
                     bias: Optional[Tensor] = None,
                     stride: MaybeTuple[builtins.int] = 1,
                     padding: MaybeTuple[builtins.int] = 0,
                     output_padding: MaybeTuple[builtins.int] = 0,
                     groups: builtins.int = 1,
                     dilation: MaybeTuple[builtins.int] = 1) -> Tensor: ...


def conv_transpose3d(input: Tensor, weight: Tensor,
                     bias: Optional[Tensor] = None,
                     stride: MaybeTuple[builtins.int] = 1,
                     padding: MaybeTuple[builtins.int] = 0,
                     output_padding: MaybeTuple[builtins.int] = 0,
                     groups: builtins.int = 1,
                     dilation: MaybeTuple[builtins.int] = 1) -> Tensor: ...


def convolution(input: Tensor, weight: Tensor, bias: Optional[Tensor],
                stride: MaybeTuple[builtins.int],
                padding: MaybeTuple[builtins.int],
                dilation: MaybeTuple[builtins.int], transposed: bool,
                output_padding: MaybeTuple[builtins.int],
                groups: builtins.int) -> Tensor: ...


def cos(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def cos_(input: Tensor) -> Tensor: ...


def cosh(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def cosh_(input: Tensor) -> Tensor: ...


def cosine_embedding_loss(input1: Tensor, input2: Tensor, target: Tensor,
                          margin: builtins.float = 0.0,
                          reduction: str = 'elementwise_mean') -> Tensor: ...


def cross(input: Tensor, other: Tensor, dim: builtins.int = -1, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def ctc_loss(log_probs: Tensor, targets: Tensor,
             input_lengths: MaybeTuple[builtins.int],
             target_lengths: MaybeTuple[builtins.int], blank: builtins.int = 0,
             reduction: str = 'elementwise_mean') -> Tensor: ...


@overload
def ctc_loss(log_probs: Tensor, targets: Tensor, input_lengths: Tensor,
             target_lengths: Tensor, blank: builtins.int = 0,
             reduction: str = 'elementwise_mean') -> Tensor: ...


def cudnn_affine_grid_generator(theta: Tensor, N: builtins.int, C: builtins.int,
                                H: builtins.int,
                                W: builtins.int) -> Tensor: ...


def cudnn_batch_norm(input: Tensor, weight: Tensor, bias: Optional[Tensor],
                     running_mean: Optional[Tensor],
                     running_var: Optional[Tensor], training: bool,
                     exponential_average_factor: builtins.float,
                     epsilon: builtins.float) -> Tuple[
    Tensor, Tensor, Tensor]: ...


def cudnn_convolution(input: Tensor, weight: Tensor, bias: Optional[Tensor],
                      padding: MaybeTuple[builtins.int],
                      stride: MaybeTuple[builtins.int],
                      dilation: MaybeTuple[builtins.int], groups: builtins.int,
                      benchmark: bool, deterministic: bool) -> Tensor: ...


def cudnn_convolution_transpose(input: Tensor, weight: Tensor,
                                bias: Optional[Tensor],
                                padding: MaybeTuple[builtins.int],
                                output_padding: MaybeTuple[builtins.int],
                                stride: MaybeTuple[builtins.int],
                                dilation: MaybeTuple[builtins.int],
                                groups: builtins.int, benchmark: bool,
                                deterministic: bool) -> Tensor: ...


def cudnn_grid_sampler(input: Tensor, grid: Tensor) -> Tensor: ...


def cudnn_is_acceptable(input: Tensor) -> bool: ...


@overload
def cumprod(input: Tensor, dim: builtins.int, *,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def cumprod(input: Tensor, dim: builtins.int, *, dtype: _dtype,
            out: Optional[Tensor] = None) -> Tensor: ...


@overload
def cumsum(input: Tensor, dim: builtins.int, *,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def cumsum(input: Tensor, dim: builtins.int, *, dtype: _dtype,
           out: Optional[Tensor] = None) -> Tensor: ...


def det(input: Tensor) -> Tensor: ...


def detach(input: Tensor) -> Tensor: ...


def detach_(input: Tensor) -> Tensor: ...


def diag(input: Tensor, diagonal: builtins.int = 0, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def diagflat(input: Tensor, offset: builtins.int = 0) -> Tensor: ...


def diagonal(input: Tensor, offset: builtins.int = 0, dim1: builtins.int = 0,
             dim2: builtins.int = 1) -> Tensor: ...


def digamma(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def dist(input: Tensor, other: Tensor, p: builtins.float = 2) -> Tensor: ...


def div(input: Tensor, other: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def dot(input: Tensor, tensor: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def dropout(input: Tensor, p: builtins.float, train: bool) -> Tensor: ...


def dropout_(input: Tensor, p: builtins.float, train: bool) -> Tensor: ...


def eig(input: Tensor, eigenvectors: bool = False, *,
        out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def einsum(equation: str, tensors: Sequence[Tensor]) -> Tensor: ...


def embedding(weight: Tensor, indices: LongTensor,
              padding_idx: builtins.int = -1, scale_grad_by_freq: bool = False,
              sparse: bool = False) -> Tensor: ...


def embedding_bag(weight: Tensor, indices: LongTensor, offsets: Tensor,
                  scale_grad_by_freq: bool = False,
                  mode: builtins.int = 0, sparse: bool = False) -> Tuple[
    Tensor, Tensor, Tensor, Tensor]: ...


def embedding_renorm_(input: Tensor, indices: LongTensor,
                      max_norm: builtins.float,
                      norm_type: builtins.float) -> Tensor: ...


@overload
def empty(size: MaybeTuple[builtins.int], out: Optional[Tensor] = None,
          dtype: Optional[dtype] = None,
          layout: Type[layout] = strided,
          device: Union[device, str, None] = None,
          requires_grad: bool = False) -> Tensor: ...


@overload
def empty(*size: builtins.int, out: Optional[Tensor] = None,
          dtype: Optional[dtype] = None,
          layout: Type[layout] = strided,
          device: Union[device, str, None] = None,
          requires_grad: bool = False) -> Tensor: ...


def empty_like(input: Tensor, *, dtype: Optional[dtype] = None,
               layout: Optional[Type[layout]] = None,
               device: Union[device, str, None] = None,
               requires_grad: bool = False) -> Tensor: ...


def empty_strided(size: MaybeTuple[builtins.int],
                  stride: MaybeTuple[builtins.int], *,
                  dtype: Optional[dtype] = None,
                  layout: Type[layout] = strided,
                  device: Union[device, str, None] = None,
                  requires_grad: bool = False) -> Tensor: ...


@overload
def eq(input: Tensor, other: Tensor, *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def eq(input: Tensor, other: Union[builtins.int, builtins.float], *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


def equal(input: Tensor, other: Tensor) -> bool: ...


def erf(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def erf_(input: Tensor) -> Tensor: ...


def erfc(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def erfc_(input: Tensor) -> Tensor: ...


def erfinv(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def exp(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def exp_(input: Tensor) -> Tensor: ...


def expm1(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def expm1_(input: Tensor) -> Tensor: ...


@overload
def eye(n: builtins.int, *, out: Optional[Tensor] = None,
        dtype: Optional[dtype] = None, layout: Type[layout] = strided,
        device: Union[device, str, None] = None,
        requires_grad: bool = False) -> Tensor: ...


@overload
def eye(n: builtins.int, m: builtins.int, *, out: Optional[Tensor] = None,
        dtype: Optional[dtype] = None,
        layout: Type[layout] = strided, device: Union[device, str, None] = None,
        requires_grad: bool = False) -> Tensor: ...


def feature_alpha_dropout(input: Tensor, p: builtins.float,
                          train: bool) -> Tensor: ...


def feature_alpha_dropout_(input: Tensor, p: builtins.float,
                           train: bool) -> Tensor: ...


def feature_dropout(input: Tensor, p: builtins.float,
                    train: bool) -> Tensor: ...


def feature_dropout_(input: Tensor, p: builtins.float,
                     train: bool) -> Tensor: ...


def fft(input: Tensor, signal_ndim: builtins.int,
        normalized: bool = False) -> Tensor: ...


@overload
def fill_(input: Tensor, value: Tensor) -> Tensor: ...


@overload
def fill_(input: Tensor, value: builtins.float) -> Tensor: ...


def flatten(input: Tensor, start_dim: builtins.int = 0,
            end_dim: builtins.int = -1) -> Tensor: ...


def flip(input: Tensor, dims: MaybeTuple[builtins.int]) -> Tensor: ...


def floor(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def floor_(input: Tensor) -> Tensor: ...


@overload
def fmod(input: Tensor, other: Tensor, *,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def fmod(input: Tensor, other: builtins.float, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def frac(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


@overload
def frobenius_norm(input: Tensor) -> Tensor: ...


@overload
def frobenius_norm(input: Tensor, dim: MaybeTuple[builtins.int],
                   keepdim: bool = False, *,
                   out: Optional[Tensor] = None) -> Tensor: ...


def full(size: MaybeTuple[builtins.int], fill_value: builtins.float, *,
         out: Optional[Tensor] = None,
         dtype: Optional[dtype] = None, layout: Type[layout] = strided,
         device: Union[device, str, None] = None,
         requires_grad: bool = False) -> Tensor: ...


def full_like(input: Tensor, fill_value: builtins.float, *,
              dtype: Optional[dtype] = None,
              layout: Optional[Type[layout]] = None,
              device: Union[device, str, None] = None,
              requires_grad: bool = False) -> Tensor: ...


def gather(input: Tensor, dim: builtins.int, index: Tensor, *,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def ge(input: Tensor, other: Tensor, *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def ge(input: Tensor, other: Union[builtins.int, builtins.float], *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


def gels(input: Tensor, A: Tensor, *,
         out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def geqrf(input: Tensor, *, out: Optional[Tuple[Tensor, Tensor]] = None) -> \
Tuple[Tensor, Tensor]: ...


def ger(input: Tensor, vec2: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def gesv(input: Tensor, A: Tensor, *,
         out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def get_device(input: Tensor) -> builtins.int: ...


def grid_sampler(input: Tensor, grid: Tensor, interpolation_mode: builtins.int,
                 padding_mode: builtins.int) -> Tensor: ...


def grid_sampler_2d(input: Tensor, grid: Tensor,
                    interpolation_mode: builtins.int,
                    padding_mode: builtins.int) -> Tensor: ...


def grid_sampler_3d(input: Tensor, grid: Tensor,
                    interpolation_mode: builtins.int,
                    padding_mode: builtins.int) -> Tensor: ...


def group_norm(input: Tensor, num_groups: builtins.int,
               weight: Optional[Tensor] = None, bias: Optional[Tensor] = None,
               eps: builtins.float = 1e-05,
               cudnn_enabled: bool = True) -> Tensor: ...


@overload
def gru(data: Tensor, batch_sizes: Tensor, hx: Tensor,
        params: MaybeTuple[Tensor], has_biases: bool,
        num_layers: builtins.int, dropout: builtins.float, train: bool,
        bidirectional: bool) -> Tuple[Tensor, Tensor]: ...


@overload
def gru(input: Tensor, hx: Tensor, params: MaybeTuple[Tensor], has_biases: bool,
        num_layers: builtins.int,
        dropout: builtins.float, train: bool, bidirectional: bool,
        batch_first: bool) -> Tuple[Tensor, Tensor]: ...


def gru_cell(input: Tensor, hx: Tensor, w_ih: Tensor, w_hh: Tensor,
             b_ih: Optional[Tensor] = None,
             b_hh: Optional[Tensor] = None) -> Tensor: ...


@overload
def gt(input: Tensor, other: Tensor, *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def gt(input: Tensor, other: Union[builtins.int, builtins.float], *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def hamming_window(window_length: builtins.int, *,
                   dtype: Optional[dtype] = None,
                   layout: Type[layout] = strided,
                   device: Union[device, str, None] = None,
                   requires_grad: bool = False) -> Tensor: ...


@overload
def hamming_window(window_length: builtins.int, periodic: bool, *,
                   dtype: Optional[dtype] = None,
                   layout: Type[layout] = strided,
                   device: Union[device, str, None] = None,
                   requires_grad: bool = False) -> Tensor: ...


@overload
def hamming_window(window_length: builtins.int, periodic: bool,
                   alpha: builtins.float, *, dtype: Optional[dtype] = None,
                   layout: Type[layout] = strided,
                   device: Union[device, str, None] = None,
                   requires_grad: bool = False) -> Tensor: ...


@overload
def hamming_window(window_length: builtins.int, periodic: bool,
                   alpha: builtins.float, beta: builtins.float, *,
                   dtype: Optional[dtype] = None,
                   layout: Type[layout] = strided,
                   device: Union[device, str, None] = None,
                   requires_grad: bool = False) -> Tensor: ...


@overload
def hann_window(window_length: builtins.int, *, dtype: Optional[dtype] = None,
                layout: Type[layout] = strided,
                device: Union[device, str, None] = None,
                requires_grad: bool = False) -> Tensor: ...


@overload
def hann_window(window_length: builtins.int, periodic: bool, *,
                dtype: Optional[dtype] = None,
                layout: Type[layout] = strided,
                device: Union[device, str, None] = None,
                requires_grad: bool = False) -> Tensor: ...


def hardshrink(input: Tensor, lambd: builtins.float = 0.5) -> Tensor: ...


def hinge_embedding_loss(input: Tensor, target: Tensor,
                         margin: builtins.float = 1.0,
                         reduction: str = 'elementwise_mean') -> Tensor: ...


def histc(input: Tensor, bins: builtins.int = 100, min: builtins.float = 0,
          max: builtins.float = 0, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def hspmm(mat1: Tensor, mat2: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def ifft(input: Tensor, signal_ndim: builtins.int,
         normalized: bool = False) -> Tensor: ...


def index_put(input: Tensor, indices: Sequence[LongTensor],
              values: Tensor) -> Tensor: ...


def index_put_(input: Tensor, indices: Sequence[LongTensor],
               values: Tensor) -> Tensor: ...


def index_select(input: Tensor, dim: builtins.int, index: LongTensor, *,
                 out: Optional[Tensor] = None) -> Tensor: ...


def instance_norm(input: Tensor, weight: Optional[Tensor],
                  bias: Optional[Tensor], running_mean: Optional[Tensor],
                  running_var: Optional[Tensor], use_input_stats: bool,
                  momentum: builtins.float, eps: builtins.float,
                  cudnn_enabled: bool) -> Tensor: ...


def inverse(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def irfft(input: Tensor, signal_ndim: builtins.int, normalized: bool = False,
          onesided: bool = True,
          signal_sizes: Optional[
              MaybeTuple[builtins.int]] = None) -> Tensor: ...


def is_complex(input: Tensor) -> bool: ...


def is_distributed(input: Tensor) -> bool: ...


def is_floating_point(input: Tensor) -> bool: ...


def is_nonzero(input: Tensor) -> bool: ...


def is_same_size(input: Tensor, other: Tensor) -> bool: ...


def is_signed(input: Tensor) -> bool: ...


def is_tensor(input) -> bool: ...


def isclose(input: Tensor, other: Tensor, rtol: builtins.float = 1e-05,
            atol: builtins.float = 1e-08,
            equal_nan: bool = False) -> Tensor: ...


def kl_div(input: Tensor, target: Tensor,
           reduction: str = 'elementwise_mean') -> Tensor: ...


def kthvalue(input: Tensor, k: builtins.int, dim: builtins.int = -1,
             keepdim: bool = False, *,
             out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def layer_norm(input: Tensor, normalized_shape: MaybeTuple[builtins.int],
               weight: Optional[Tensor] = None,
               bias: Optional[Tensor] = None, eps: builtins.float = 1e-05,
               cudnn_enable: bool = True) -> Tensor: ...


@overload
def le(input: Tensor, other: Tensor, *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def le(input: Tensor, other: Union[builtins.int, builtins.float], *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


def lerp(input: Tensor, end: Tensor, weight: builtins.float, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def lgamma(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


@overload
def linspace(start: builtins.float, end: builtins.float, *,
             out: Optional[Tensor] = None, dtype: Optional[dtype] = None,
             layout: Type[layout] = strided,
             device: Union[device, str, None] = None,
             requires_grad: bool = False) -> Tensor: ...


@overload
def linspace(start: builtins.float, end: builtins.float, steps: builtins.int, *,
             out: Optional[Tensor] = None,
             dtype: Optional[dtype] = None, layout: Type[layout] = strided,
             device: Union[device, str, None] = None,
             requires_grad: bool = False) -> Tensor: ...


def log(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def log10(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def log10_(input: Tensor) -> Tensor: ...


def log1p(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def log1p_(input: Tensor) -> Tensor: ...


def log2(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def log2_(input: Tensor) -> Tensor: ...


def log_(input: Tensor) -> Tensor: ...


def log_softmax(input: Tensor, dim: builtins.int) -> Tensor: ...


def log_softmax_backward_data(grad_output: Tensor, output: Tensor,
                              dim: builtins.int, self: Tensor) -> Tensor: ...


def logdet(input: Tensor) -> Tensor: ...


@overload
def logspace(start: builtins.float, end: builtins.float, *,
             out: Optional[Tensor] = None, dtype: Optional[dtype] = None,
             layout: Type[layout] = strided,
             device: Union[device, str, None] = None,
             requires_grad: bool = False) -> Tensor: ...


@overload
def logspace(start: builtins.float, end: builtins.float, steps: builtins.int, *,
             out: Optional[Tensor] = None,
             dtype: Optional[dtype] = None, layout: Type[layout] = strided,
             device: Union[device, str, None] = None,
             requires_grad: bool = False) -> Tensor: ...


def logsumexp(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
              out: Optional[Tensor] = None) -> Tensor: ...


@overload
def lstm(data: Tensor, batch_sizes: Tensor, hx: MaybeTuple[Tensor],
         params: MaybeTuple[Tensor], has_biases: bool,
         num_layers: builtins.int, dropout: builtins.float, train: bool,
         bidirectional: bool) -> Tuple[Tensor, Tensor, Tensor]: ...


@overload
def lstm(input: Tensor, hx: MaybeTuple[Tensor], params: MaybeTuple[Tensor],
         has_biases: bool, num_layers: builtins.int,
         dropout: builtins.float, train: bool, bidirectional: bool,
         batch_first: bool) -> Tuple[Tensor, Tensor, Tensor]: ...


def lstm_cell(input: Tensor, hx: MaybeTuple[Tensor], w_ih: Tensor, w_hh: Tensor,
              b_ih: Optional[Tensor] = None,
              b_hh: Optional[Tensor] = None) -> Tuple[Tensor, Tensor]: ...


@overload
def lt(input: Tensor, other: Tensor, *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def lt(input: Tensor, other: Union[builtins.int, builtins.float], *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


def margin_ranking_loss(input1: Tensor, input2: Tensor, target: Tensor,
                        margin: builtins.float = 0.0,
                        reduction: str = 'elementwise_mean') -> Tensor: ...


def masked_select(input: Tensor, mask: Tensor, *,
                  out: Optional[Tensor] = None) -> Tensor: ...


def matmul(input: Tensor, other: Tensor, *,
           out: Optional[Tensor] = None) -> Tensor: ...


def matrix_power(input: Tensor, n: builtins.int) -> Tensor: ...


@overload
def matrix_rank(input: Tensor, symmetric: bool = False) -> Tensor: ...


@overload
def matrix_rank(input: Tensor, tol: builtins.float,
                symmetric: bool = False) -> Tensor: ...


@overload
def max(input: Tensor) -> Tensor: ...


@overload
def max(input: Tensor, other: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def max(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
        out: Optional[Tuple[Tensor, LongTensor]] = None) -> Tuple[
    Tensor, LongTensor]: ...


def max_pool1d_with_indices(input: Tensor,
                            kernel_size: MaybeTuple[builtins.int],
                            stride: Optional[MaybeTuple[builtins.int]] = None,
                            padding: MaybeTuple[builtins.int] = 0,
                            dilation: MaybeTuple[builtins.int] = 1,
                            ceil_mode: bool = False) -> Tuple[
    Tensor, Tensor]: ...


@overload
def mean(input: Tensor) -> Tensor: ...


@overload
def mean(input: Tensor, *, dtype: _dtype) -> Tensor: ...


@overload
def mean(input: Tensor, dim: builtins.int, *, dtype: _dtype,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def mean(input: Tensor, dim: builtins.int, keepdim: bool, *, dtype: _dtype,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def mean(input: Tensor, dim: MaybeTuple[builtins.int], keepdim: bool = False, *,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def median(input: Tensor) -> Tensor: ...


@overload
def median(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
           out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def meshgrid(tensors: Sequence[Tensor]) -> MaybeTuple[Tensor]: ...


@overload
def min(input: Tensor) -> Tensor: ...


@overload
def min(input: Tensor, other: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def min(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
        out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def miopen_batch_norm(input: Tensor, weight: Tensor, bias: Optional[Tensor],
                      running_mean: Optional[Tensor],
                      running_var: Optional[Tensor], training: bool,
                      exponential_average_factor: builtins.float,
                      epsilon: builtins.float) -> Tuple[
    Tensor, Tensor, Tensor]: ...


def miopen_convolution(input: Tensor, weight: Tensor, bias: Optional[Tensor],
                       padding: MaybeTuple[builtins.int],
                       stride: MaybeTuple[builtins.int],
                       dilation: MaybeTuple[builtins.int], groups: builtins.int,
                       benchmark: bool, deterministic: bool) -> Tensor: ...


def miopen_convolution_transpose(input: Tensor, weight: Tensor,
                                 bias: Optional[Tensor],
                                 padding: MaybeTuple[builtins.int],
                                 output_padding: MaybeTuple[builtins.int],
                                 stride: MaybeTuple[builtins.int],
                                 dilation: MaybeTuple[builtins.int],
                                 groups: builtins.int, benchmark: bool,
                                 deterministic: bool) -> Tensor: ...


def mkldnn_convolution(input: Tensor, weight: Tensor, bias: Optional[Tensor],
                       padding: MaybeTuple[builtins.int],
                       stride: MaybeTuple[builtins.int],
                       dilation: MaybeTuple[builtins.int],
                       groups: builtins.int) -> Tensor: ...


def mkldnn_convolution_backward_weights(weight_size: MaybeTuple[builtins.int],
                                        grad_output: Tensor, self: Tensor,
                                        padding: MaybeTuple[builtins.int],
                                        stride: MaybeTuple[builtins.int],
                                        dilation: MaybeTuple[builtins.int],
                                        groups: builtins.int,
                                        bias_defined: bool) -> Tuple[
    Tensor, Tensor]: ...


def mm(input: Tensor, mat2: Tensor, *,
       out: Optional[Tensor] = None) -> Tensor: ...


def mode(input: Tensor, dim: builtins.int = -1, keepdim: bool = False, *,
         out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def mul(input: Tensor, other: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def multinomial(input: Tensor, num_samples: builtins.int,
                replacement: bool = False, *,
                generator: Optional[Generator] = None,
                out: Optional[Tensor] = None) -> Tensor: ...


def mv(input: Tensor, vec: Tensor, *,
       out: Optional[Tensor] = None) -> Tensor: ...


def mvlgamma(input: Tensor, p: builtins.int) -> Tensor: ...


def narrow(input: Tensor, dim: builtins.int, start: builtins.int,
           length: builtins.int) -> Tensor: ...


def native_clone(input: Tensor) -> Tensor: ...


def native_get_device(input: Tensor) -> builtins.int: ...


def native_norm(input: Tensor, p: builtins.float = 2) -> Tensor: ...


def native_pow(input: Tensor, exponent: builtins.float, *,
               out: Optional[Tensor] = None) -> Tensor: ...


def native_resize_as_(input: Tensor, the_template: Tensor) -> Tensor: ...


def native_zero_(input: Tensor) -> Tensor: ...


@overload
def ne(input: Tensor, other: Tensor, *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


@overload
def ne(input: Tensor, other: Union[builtins.int, builtins.float], *,
       out: Optional[ByteTensor] = None) -> ByteTensor: ...


def neg(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def nonzero(input: Tensor, *,
            out: Optional[LongTensor] = None) -> LongTensor: ...


def norm(input: Tensor, p: Union[builtins.float, str, None] = 'fro',
         dim: Optional[builtins.int] = None,
         keepdim: bool = False, *, out: Optional[Tensor] = None) -> Tensor: ...


def norm_except_dim(v: Tensor, pow: builtins.int = 2,
                    dim: builtins.int = 0) -> Tensor: ...


@overload
def normal(mean: Tensor, std: Tensor, *, generator: Optional[Generator] = None,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def normal(mean: Tensor, std: builtins.float = 1, *,
           generator: Optional[Generator] = None,
           out: Optional[Tensor] = None) -> Tensor: ...


@overload
def normal(mean: builtins.float, std: Tensor, *,
           generator: Optional[Generator] = None,
           out: Optional[Tensor] = None) -> Tensor: ...


def nuclear_norm(input: Tensor, keepdim: bool = False, *,
                 out: Optional[Tensor] = None) -> Tensor: ...


def numel(input: Tensor) -> builtins.int: ...


@overload
def ones(size: MaybeTuple[builtins.int], out: Optional[Tensor] = None,
         dtype: Optional[dtype] = None,
         layout: Type[layout] = strided,
         device: Union[device, str, None] = None,
         requires_grad: bool = False) -> Tensor: ...


@overload
def ones(*size: builtins.int, out: Optional[Tensor] = None,
         dtype: Optional[dtype] = None,
         layout: Type[layout] = strided,
         device: Union[device, str, None] = None,
         requires_grad: bool = False) -> Tensor: ...


def ones_like(input: Tensor, *, dtype: Optional[dtype] = None,
              layout: Optional[Type[layout]] = None,
              device: Union[device, str, None] = None,
              requires_grad: bool = False) -> Tensor: ...


def orgqr(input: Tensor, input2: Tensor, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def ormqr(input: Tensor, input2: Tensor, input3: Tensor, left: bool = True,
          transpose: bool = False, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def pairwise_distance(x1: Tensor, x2: Tensor, p: builtins.float = 2,
                      eps: builtins.float = 1e-06,
                      keepdim: bool = False) -> Tensor: ...


def pdist(input: Tensor, p: builtins.float = 2) -> Tensor: ...


def pin_memory(input: Tensor) -> Tensor: ...


def pinverse(input: Tensor, rcond: builtins.float = 1e-15) -> Tensor: ...


def pixel_shuffle(input: Tensor, upscale_factor: builtins.int) -> Tensor: ...


def poisson(input: Tensor, generator: Optional[Generator] = None) -> Tensor: ...


def polygamma(n: builtins.int, self: Tensor, *,
              out: Optional[Tensor] = None) -> Tensor: ...


def potrf(input: Tensor, upper: bool = True, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def potri(input: Tensor, upper: bool = True, *,
          out: Optional[Tensor] = None) -> Tensor: ...


def potrs(input: Tensor, input2: Tensor, upper: bool = True, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def pow(input: Tensor, exponent: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def pow(input: Tensor, exponent: builtins.float, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def prelu(input: Tensor, weight: Tensor) -> Tensor: ...


@overload
def prod(input: Tensor) -> Tensor: ...


@overload
def prod(input: Tensor, *, dtype: _dtype) -> Tensor: ...


@overload
def prod(input: Tensor, dim: builtins.int, *, dtype: _dtype,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def prod(input: Tensor, dim: builtins.int, keepdim: bool, *, dtype: _dtype,
         out: Optional[Tensor] = None) -> Tensor: ...


@overload
def prod(input: Tensor, dim: builtins.int, keepdim: bool = False, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def pstrf(input: Tensor, upper: bool = True, tol: builtins.float = -1, *,
          out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def qr(input: Tensor, *, out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


@overload
def rand(*size: builtins.int, generator: Optional[Generator] = None,
         out: Optional[Tensor] = None,
         dtype: Optional[dtype] = None, layout: Type[layout] = strided,
         device: Union[device, str, None] = None,
         requires_grad: bool = False) -> Tensor: ...


@overload
def rand(sizes: Tuple[builtins.int, ...], generator: Optional[Generator] = None,
         out: Optional[Tensor] = None,
         dtype: Optional[dtype] = None, layout: Type[layout] = strided,
         device: Union[device, str, None] = None,
         requires_grad: bool = False) -> Tensor: ...


def rand_like(input: Tensor, *, dtype: Optional[dtype] = None,
              layout: Optional[Type[layout]] = None,
              device: Union[device, str, None] = None,
              requires_grad: bool = False) -> Tensor: ...


@overload
def randint_like(input: Tensor, high: builtins.int, *,
                 dtype: Optional[dtype] = None,
                 layout: Optional[Type[layout]] = None,
                 device: Union[device, str, None] = None,
                 requires_grad: bool = False) -> LongTensor: ...


@overload
def randint_like(input: Tensor, low: builtins.int, high: builtins.int, *,
                 dtype: Optional[dtype] = None,
                 layout: Optional[Type[layout]] = None,
                 device: Union[device, str, None] = None,
                 requires_grad: bool = False) -> LongTensor: ...


@overload
def randint(high: builtins.int, size: MaybeTuple[builtins.int], *,
            dtype: Optional[dtype] = None,
            layout: Optional[Type[layout]] = None,
            device: Union[device, str, None] = None,
            requires_grad: bool = False) -> LongTensor: ...


@overload
def randint(low: builtins.int, high: builtins.int,
            size: MaybeTuple[builtins.int], *, dtype: Optional[dtype] = None,
            layout: Optional[Type[layout]] = None,
            device: Union[device, str, None] = None,
            requires_grad: bool = False) -> LongTensor: ...


@overload
def randn(*size: builtins.int, generator: Optional[Generator] = None,
          out: Optional[Tensor] = None,
          dtype: Optional[dtype] = None, layout: Type[layout] = strided,
          device: Union[device, str, None] = None,
          requires_grad: bool = False) -> Tensor: ...


@overload
def randn(sizes: Tuple[builtins.int, ...],
          generator: Optional[Generator] = None, out: Optional[Tensor] = None,
          dtype: Optional[dtype] = None, layout: Type[layout] = strided,
          device: Union[device, str, None] = None,
          requires_grad: bool = False) -> Tensor: ...


def randn_like(input: Tensor, *, dtype: Optional[dtype] = None,
               layout: Optional[Type[layout]] = None,
               device: Union[device, str, None] = None,
               requires_grad: bool = False) -> Tensor: ...


@overload
def randperm(n: builtins.int, *, generator: Generator,
             out: Optional[Tensor] = None, dtype: _dtype = int64,
             layout: Type[layout] = strided,
             device: Union[device, str, None] = None,
             requires_grad: bool = False) -> Tensor: ...


@overload
def randperm(n: builtins.int, *, out: Optional[Tensor] = None,
             dtype: _dtype = int64, layout: Type[layout] = strided,
             device: Union[device, str, None] = None,
             requires_grad: bool = False) -> Tensor: ...


def raw_copy_sparse_(input: Tensor, src: Tensor) -> Tensor: ...


def reciprocal(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def relu(input: Tensor) -> Tensor: ...


def relu_(input: Tensor) -> Tensor: ...


@overload
def remainder(input: Tensor, other: Tensor, *,
              out: Optional[Tensor] = None) -> Tensor: ...


@overload
def remainder(input: Tensor, other: builtins.float, *,
              out: Optional[Tensor] = None) -> Tensor: ...


def renorm(input: Tensor, p: builtins.float, dim: builtins.int,
           maxnorm: builtins.float, *,
           out: Optional[Tensor] = None) -> Tensor: ...


def reshape(input: Tensor, shape: MaybeTuple[builtins.int]) -> Tensor: ...


def resize_as_(input: Tensor, the_template: Tensor) -> Tensor: ...


def rfft(input: Tensor, signal_ndim: builtins.int, normalized: bool = False,
         onesided: bool = True) -> Tensor: ...


@overload
def rnn_relu(data: Tensor, batch_sizes: Tensor, hx: Tensor,
             params: MaybeTuple[Tensor], has_biases: bool,
             num_layers: builtins.int, dropout: builtins.float, train: bool,
             bidirectional: bool) -> Tuple[Tensor, Tensor]: ...


@overload
def rnn_relu(input: Tensor, hx: Tensor, params: MaybeTuple[Tensor],
             has_biases: bool, num_layers: builtins.int,
             dropout: builtins.float, train: bool, bidirectional: bool,
             batch_first: bool) -> Tuple[Tensor, Tensor]: ...


def rnn_relu_cell(input: Tensor, hx: Tensor, w_ih: Tensor, w_hh: Tensor,
                  b_ih: Optional[Tensor] = None,
                  b_hh: Optional[Tensor] = None) -> Tensor: ...


@overload
def rnn_tanh(data: Tensor, batch_sizes: Tensor, hx: Tensor,
             params: MaybeTuple[Tensor], has_biases: bool,
             num_layers: builtins.int, dropout: builtins.float, train: bool,
             bidirectional: bool) -> Tuple[Tensor, Tensor]: ...


@overload
def rnn_tanh(input: Tensor, hx: Tensor, params: MaybeTuple[Tensor],
             has_biases: bool, num_layers: builtins.int,
             dropout: builtins.float, train: bool, bidirectional: bool,
             batch_first: bool) -> Tuple[Tensor, Tensor]: ...


def rnn_tanh_cell(input: Tensor, hx: Tensor, w_ih: Tensor, w_hh: Tensor,
                  b_ih: Optional[Tensor] = None,
                  b_hh: Optional[Tensor] = None) -> Tensor: ...


def round(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def round_(input: Tensor) -> Tensor: ...


def rrelu(input: Tensor, lower: builtins.float = 0.125,
          upper: builtins.float = 0.3333333333333333,
          training: bool = False,
          generator: Optional[Generator] = None) -> Tensor: ...


def rrelu_(input: Tensor, lower: builtins.float = 0.125,
           upper: builtins.float = 0.3333333333333333,
           training: bool = False,
           generator: Optional[Generator] = None) -> Tensor: ...


def rsqrt(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def rsqrt_(input: Tensor) -> Tensor: ...


def s_native_addmm(input: Tensor, mat1: Tensor, mat2: Tensor, *,
                   beta: builtins.float = 1, alpha: builtins.float = 1,
                   out: Optional[Tensor] = None) -> Tensor: ...


def s_native_addmm_(input: Tensor, mat1: Tensor, mat2: Tensor, *,
                    beta: builtins.float = 1,
                    alpha: builtins.float = 1) -> Tensor: ...


def select(input: Tensor, dim: builtins.int, index: builtins.int) -> Tensor: ...


def selu(input: Tensor) -> Tensor: ...


def selu_(input: Tensor) -> Tensor: ...


def sigmoid(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def sigmoid_(input: Tensor) -> Tensor: ...


def sign(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def sin(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def sin_(input: Tensor) -> Tensor: ...


def sinh(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def sinh_(input: Tensor) -> Tensor: ...


def slogdet(input: Tensor) -> Tuple[Tensor, Tensor]: ...


def smm(input: Tensor, mat2: Tensor) -> Tensor: ...


def softmax(input: Tensor, dim: builtins.int) -> Tensor: ...


def softmax_backward_data(grad_output: Tensor, output: Tensor,
                          dim: builtins.int, self: Tensor) -> Tensor: ...


def sort(input: Tensor, dim: builtins.int = -1, descending: bool = False, *,
         out: Optional[Tuple[Tensor, LongTensor]] = None) -> Tuple[
    Tensor, LongTensor]: ...


def split(input: Tensor, split_size_or_sections: MaybeList[builtins.int],
          dim: builtins.int = 0) -> Tuple[Tensor, ...]: ...


def sqrt(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def sqrt_(input: Tensor) -> Tensor: ...


@overload
def squeeze(input: Tensor) -> Tensor: ...


@overload
def squeeze(input: Tensor, dim: builtins.int) -> Tensor: ...


@overload
def sspaddmm(beta: builtins.float, self: Tensor, alpha: builtins.float,
             mat1: Tensor, mat2: Tensor) -> Tensor: ...


@overload
def sspaddmm(beta: builtins.float, self: Tensor, mat1: Tensor,
             mat2: Tensor) -> Tensor: ...


@overload
def sspaddmm(input: Tensor, mat1: Tensor, mat2: Tensor, *,
             beta: builtins.float = 1, alpha: builtins.float = 1,
             out: Optional[Tensor] = None) -> Tensor: ...


def stack(tensors: Sequence[Tensor], dim: builtins.int = 0, *,
          out: Optional[Tensor] = None) -> Tensor: ...


@overload
def std(input: Tensor, unbiased: bool = True) -> Tensor: ...


@overload
def std(input: Tensor, dim: MaybeTuple[builtins.int], unbiased: bool = True,
        keepdim: bool = False, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def stft(input: Tensor, n_fft: builtins.int,
         hop_length: Optional[builtins.int] = None,
         win_length: Optional[builtins.int] = None,
         window: Optional[Tensor] = None, normalized: bool = False,
         onesided: bool = True) -> Tensor: ...


@overload
def sub(input: Tensor, alpha: builtins.float, other: Tensor, *,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def sub(input: Tensor, other: Tensor, *, alpha: builtins.float = 1,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def sum(input: Tensor) -> Tensor: ...


@overload
def sum(input: Tensor, *, dtype: _dtype) -> Tensor: ...


@overload
def sum(input: Tensor, dim: MaybeTuple[builtins.int], *, dtype: _dtype,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def sum(input: Tensor, dim: MaybeTuple[builtins.int], keepdim: bool, *,
        dtype: _dtype,
        out: Optional[Tensor] = None) -> Tensor: ...


@overload
def sum(input: Tensor, dim: MaybeTuple[builtins.int], keepdim: bool = False, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def svd(input: Tensor, some: bool = True, *,
        out: Optional[Tuple[Tensor, Tensor, Tensor]]) -> Tuple[
    Tensor, Tensor, Tensor]: ...


def symeig(input: Tensor, eigenvectors: bool = False, upper: bool = True, *,
           out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def t(input: Tensor) -> Tensor: ...


def take(input: Tensor, index: LongTensor, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def tan(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def tan_(input: Tensor) -> Tensor: ...


def tanh(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def tanh_(input: Tensor) -> Tensor: ...


def tensordot(input: Tensor, other: Tensor, dims_self: MaybeTuple[builtins.int],
              dims_other: MaybeTuple[builtins.int]) -> Tensor: ...


def th_addmm(input: Tensor, mat1: Tensor, mat2: Tensor, *,
             beta: builtins.float = 1, alpha: builtins.float = 1,
             out: Optional[Tensor] = None) -> Tensor: ...


def th_addmm_(input: Tensor, mat1: Tensor, mat2: Tensor, *,
              beta: builtins.float = 1,
              alpha: builtins.float = 1) -> Tensor: ...


def th_clone(input: Tensor) -> Tensor: ...


def th_norm(input: Tensor, p: builtins.float = 2) -> Tensor: ...


def th_pow(input: Tensor, exponent: builtins.float, *,
           out: Optional[Tensor] = None) -> Tensor: ...


def th_resize_as_(input: Tensor, the_template: Tensor) -> Tensor: ...


def th_zero_(input: Tensor) -> Tensor: ...


def topk(input: Tensor, k: builtins.int, dim: builtins.int = -1,
         largest: bool = True, sorted: bool = True, *,
         out: Optional[Tuple[Tensor, LongTensor]] = None) -> Tuple[
    Tensor, LongTensor]: ...


def trace(input: Tensor) -> Tensor: ...


def transpose(input: Tensor, dim0: builtins.int,
              dim1: builtins.int) -> Tensor: ...


def tril(input: Tensor, diagonal: builtins.int = 0, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def triplet_margin_loss(anchor: Tensor, positive: Tensor, negative: Tensor,
                        margin: builtins.float = 1.0,
                        p: builtins.float = 2, eps: builtins.float = 1e-06,
                        swap: bool = False,
                        reduction: str = 'elementwise_mean') -> Tensor: ...


def triu(input: Tensor, diagonal: builtins.int = 0, *,
         out: Optional[Tensor] = None) -> Tensor: ...


def trtrs(input: Tensor, A: Tensor, upper: bool = True, transpose: bool = False,
          unitriangular: bool = False, *,
          out: Optional[Tuple[Tensor, Tensor]] = None) -> Tuple[
    Tensor, Tensor]: ...


def trunc(input: Tensor, *, out: Optional[Tensor] = None) -> Tensor: ...


def trunc_(input: Tensor) -> Tensor: ...


def unbind(input: Tensor, dim: builtins.int = 0) -> MaybeTuple[Tensor]: ...


def unsqueeze(input: Tensor, dim: builtins.int) -> Tensor: ...


@overload
def var(input: Tensor, unbiased: bool = True) -> Tensor: ...


@overload
def var(input: Tensor, dim: builtins.int, unbiased: bool = True,
        keepdim: bool = False, *,
        out: Optional[Tensor] = None) -> Tensor: ...


def where(condition: ByteTensor, self: Tensor, other: Tensor) -> Tensor: ...


def zero_(input: Tensor) -> Tensor: ...


@overload
def zeros(size: MaybeTuple[builtins.int], out: Optional[Tensor] = None,
          dtype: Optional[dtype] = None,
          layout: Type[layout] = strided,
          device: Union[device, str, None] = None,
          requires_grad: bool = False) -> Tensor: ...


@overload
def zeros(*size: builtins.int, out: Optional[Tensor] = None,
          dtype: Optional[dtype] = None,
          layout: Type[layout] = strided,
          device: Union[device, str, None] = None,
          requires_grad: bool = False) -> Tensor: ...


def zeros_like(input: Tensor, *, dtype: Optional[dtype] = None,
               layout: Optional[Type[layout]] = None,
               device: Union[device, str, None] = None,
               requires_grad: bool = False) -> Tensor: ...


def from_numpy(data: np.ndarray) -> Tensor: ...


def as_tensor(data: np.ndarray, dtype: Optional[dtype] = None,
              device: Union[device, str, None] = None) -> Tensor: ...
