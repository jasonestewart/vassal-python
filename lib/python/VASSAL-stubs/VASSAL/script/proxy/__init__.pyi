import VASSAL.build.module
import VASSAL.counters
import java.awt
import java.util
import typing



class GamePiece:
    def __init__(self, gamePiece: VASSAL.counters.GamePiece): ...
    def getMap(self) -> 'Map': ...
    def getName(self) -> str: ...
    def getParent(self) -> 'Stack': ...
    def getPosition(self) -> java.awt.Point: ...
    def getProperty(self, string: str) -> typing.Any: ...

class Map:
    def __init__(self, map: VASSAL.build.module.Map): ...
    def getName(self) -> str: ...
    def getPieces(self) -> java.util.List[GamePiece]: ...
    def getProperty(self, string: str) -> typing.Any: ...

class Stack(GamePiece):
    def __init__(self, stack: VASSAL.counters.Stack): ...
    def bottomPiece(self) -> GamePiece: ...
    def getParent(self) -> 'Stack': ...
    def getPieceAt(self, int: int) -> GamePiece: ...
    def getPieceCount(self) -> int: ...
    def getPieces(self) -> java.util.List[GamePiece]: ...
    def topPiece(self) -> GamePiece: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.script.proxy")``.

    GamePiece: typing.Type[GamePiece]
    Map: typing.Type[Map]
    Stack: typing.Type[Stack]
