import typing



_Callback__T = typing.TypeVar('_Callback__T')  # <T>
class Callback(typing.Generic[_Callback__T]):
    def receive(self, t: _Callback__T) -> None: ...

class MemoryUtils:
    @staticmethod
    def getPhysicalMemory() -> int: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

_Pair__A = typing.TypeVar('_Pair__A')  # <A>
_Pair__B = typing.TypeVar('_Pair__B')  # <B>
class Pair(typing.Generic[_Pair__A, _Pair__B]):
    first: typing.Any = ...
    second: typing.Any = ...
    def __init__(self, a: _Pair__A, b: _Pair__B): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    _of__A = typing.TypeVar('_of__A')  # <A>
    _of__B = typing.TypeVar('_of__B')  # <B>
    @staticmethod
    def of(a: _of__A, b: _of__B) -> 'Pair'[_of__A, _of__B]: ...

_Reference__T = typing.TypeVar('_Reference__T')  # <T>
class Reference(typing.Generic[_Reference__T]):
    obj: typing.Any = ...
    def __init__(self, t: _Reference__T): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.lang")``.

    Callback: typing.Type[Callback]
    MemoryUtils: typing.Type[MemoryUtils]
    Pair: typing.Type[Pair]
    Reference: typing.Type[Reference]
