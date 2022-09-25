import VASSAL
import VASSAL.counters
import VASSAL.tools.filechooser
import VASSAL.tools.imports
import java.awt
import java.io
import java.lang
import java.util
import jpype.protocol
import typing



class ADC2ModuleFileFilter(VASSAL.tools.filechooser.ExtensionFileFilter):
    types: typing.ClassVar[typing.List[str]] = ...
    def __init__(self): ...

class ADC2Utils:
    MODULE_EXTENSION: typing.ClassVar[str] = ...
    MAP_EXTENSION: typing.ClassVar[str] = ...
    SET_EXTENSION: typing.ClassVar[str] = ...
    MODULE_DESCRIPTION: typing.ClassVar[str] = ...
    MAP_DESCRIPTION: typing.ClassVar[str] = ...
    SET_DESCRIPTION: typing.ClassVar[str] = ...
    defaultColorPallet: typing.ClassVar[typing.List[java.awt.Color]] = ...
    @staticmethod
    def getColorFromIndex(int: int) -> java.awt.Color: ...
    class NoMoreBlocksException(java.io.EOFException): ...

class MapBoard(VASSAL.tools.imports.Importer):
    def __init__(self): ...
    def isValidImportFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    def writeToArchive(self) -> None: ...

class MapBoardFileFilter(VASSAL.tools.filechooser.ExtensionFileFilter):
    types: typing.ClassVar[typing.List[str]] = ...
    def __init__(self): ...

class SymbolSet(VASSAL.tools.imports.Importer):
    def __init__(self): ...
    @typing.overload
    def getMaxSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getMaxSize(self, dimension: java.awt.Dimension) -> java.awt.Dimension: ...
    def getModalSize(self) -> java.awt.Dimension: ...
    def isValidImportFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    def writeToArchive(self) -> None: ...

class SymbolSetFileFilter(VASSAL.tools.filechooser.ExtensionFileFilter):
    types: typing.ClassVar[typing.List[str]] = ...
    def __init__(self): ...

class ADC2Module(VASSAL.tools.imports.Importer):
    DRAW_ON_TOP_OF_OTHERS: typing.ClassVar[str] = ...
    PIECE: typing.ClassVar[str] = ...
    COMMON_PROPERTIES: typing.ClassVar[str] = ...
    FLAG_BACKGROUND: typing.ClassVar[java.awt.Color] = ...
    FLAG_FOREGROUND: typing.ClassVar[java.awt.Color] = ...
    def __init__(self): ...
    def isValidImportFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    def usePieceValues(self) -> bool: ...
    def writeToArchive(self) -> None: ...
    class CardClass(VASSAL.tools.imports.adc2.ADC2Module.PieceClass):
        def __init__(self, aDC2Module: 'ADC2Module', string: str, int: int, int2: int): ...
        def checkHidden(self, piece: 'ADC2Module.Piece') -> bool: ...
        def getFreeRotatorDecorator(self) -> VASSAL.counters.FreeRotator: ...
        def getHiddenDecorator(self) -> VASSAL.counters.Obscurable: ...
        def getHiddenName(self) -> str: ...
        def getHiddenSymbol(self) -> 'SymbolSet.SymbolData': ...
        def getOwner(self) -> 'ADC2Module.Player': ...
        def getPieceValueMask(self) -> VASSAL.counters.Obscurable: ...
        def getPlayer(self, piece: 'ADC2Module.Piece') -> 'ADC2Module.Player': ...
        def getPropertySheetDecorator(self) -> VASSAL.counters.PropertySheet: ...
    class Cards(VASSAL.tools.imports.adc2.ADC2Module.Pool):
        def getOwner(self) -> 'ADC2Module.Player': ...
        def setOwner(self, int: int) -> None: ...
    class DeckPool(VASSAL.tools.imports.adc2.ADC2Module.Cards): ...
    class FacingDirection(java.lang.Enum['ADC2Module.FacingDirection']):
        FLAT_SIDES: typing.ClassVar['ADC2Module.FacingDirection'] = ...
        VERTEX: typing.ClassVar['ADC2Module.FacingDirection'] = ...
        BOTH: typing.ClassVar['ADC2Module.FacingDirection'] = ...
        NONE: typing.ClassVar['ADC2Module.FacingDirection'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ADC2Module.FacingDirection': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['ADC2Module.FacingDirection']: ...
    class ForcePool(VASSAL.tools.imports.adc2.ADC2Module.Pool): ...
    class HandPool(VASSAL.tools.imports.adc2.ADC2Module.Cards): ...
    class HideState(java.lang.Enum['ADC2Module.HideState']):
        NOT_HIDDEN: typing.ClassVar['ADC2Module.HideState'] = ...
        INFO_HIDDEN: typing.ClassVar['ADC2Module.HideState'] = ...
        HIDDEN: typing.ClassVar['ADC2Module.HideState'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ADC2Module.HideState': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['ADC2Module.HideState']: ...
    class Piece:
        pieceClass: 'ADC2Module.PieceClass' = ...
        hideState: 'ADC2Module.HideState' = ...
        @typing.overload
        def __init__(self, aDC2Module: 'ADC2Module', pieceClass: 'ADC2Module.PieceClass'): ...
        @typing.overload
        def __init__(self, aDC2Module: 'ADC2Module', int: int, string: str, pieceClass: 'ADC2Module.PieceClass', hideState: 'ADC2Module.HideState', int2: int, int3: int): ...
        def drawOnTopOfOthers(self) -> bool: ...
        def equals(self, object: typing.Any) -> bool: ...
        def getClassName(self) -> str: ...
        def getFacingAngle(self) -> float: ...
        def getForcePool(self) -> 'ADC2Module.Pool': ...
        def getPlayer(self) -> 'ADC2Module.Player': ...
        def getUniqueClassName(self) -> str: ...
        def getValue(self, int: int) -> typing.Any: ...
        def hasAttacked(self) -> bool: ...
        def hasDefended(self) -> bool: ...
        def hasMoved(self) -> bool: ...
        def hashCode(self) -> int: ...
        def inForcePool(self) -> bool: ...
        def isCard(self) -> bool: ...
    class PieceClass:
        backReplace: 'ADC2Module.PieceClass' = ...
        CLASS_PROPERTIES: typing.ClassVar[str] = ...
        def __init__(self, aDC2Module: 'ADC2Module', string: str, symbolData: 'SymbolSet.SymbolData', int: int, int2: int, int3: int): ...
        def checkHidden(self, piece: 'ADC2Module.Piece') -> bool: ...
        def getAllowedFacings(self) -> 'ADC2Module.FacingDirection': ...
        def getAttackedEmbellishmentDecorator(self) -> VASSAL.counters.Embellishment: ...
        def getBackFlipClass(self) -> 'ADC2Module.PieceClass': ...
        def getDefendedEmbellishmentDecorator(self) -> VASSAL.counters.Embellishment: ...
        def getDynamicPropertyDecorator(self) -> VASSAL.counters.DynamicProperty: ...
        def getFlipClass(self) -> 'ADC2Module.PieceClass': ...
        def getFreeRotatorDecorator(self) -> VASSAL.counters.FreeRotator: ...
        def getHiddenDecorator(self) -> VASSAL.counters.Decorator: ...
        def getHiddenName(self) -> str: ...
        def getHiddenSymbol(self) -> 'SymbolSet.SymbolData': ...
        def getImageName(self) -> str: ...
        def getMovementMarkableDecorator(self) -> VASSAL.counters.MovementMarkable: ...
        def getNValues(self) -> int: ...
        def getName(self) -> str: ...
        def getOwner(self) -> 'ADC2Module.Player': ...
        def getPieceValueMask(self) -> VASSAL.counters.Obscurable: ...
        def getPlayer(self, piece: 'ADC2Module.Piece') -> 'ADC2Module.Player': ...
        def getPropertySheetDecorator(self) -> VASSAL.counters.PropertySheet: ...
        def getReplaceWithOtherDecorator(self) -> VASSAL.counters.Decorator: ...
        def getReplaceWithPreviousDecorator(self) -> VASSAL.counters.Decorator: ...
        def getUniqueName(self) -> str: ...
        def getUsePrototypeDecorator(self) -> VASSAL.counters.UsePrototype: ...
        def getValue(self, int: int) -> typing.Any: ...
        def getValueAsBoolean(self, int: int) -> bool: ...
        def getValueAsInt(self, int: int) -> int: ...
        def getValueAsString(self, int: int) -> str: ...
    class Player:
        ALL_PLAYERS: typing.ClassVar['ADC2Module.Player'] = ...
        NO_PLAYERS: typing.ClassVar['ADC2Module.Player'] = ...
        UNKNOWN: typing.ClassVar['ADC2Module.Player'] = ...
        def __init__(self, string: str, symbolData: 'SymbolSet.SymbolData', int: int): ...
        def getHiddenSymbol(self) -> 'SymbolSet.SymbolData': ...
        def getName(self) -> str: ...
        def hiddenInForcePools(self) -> bool: ...
        def hiddenWhenPlaced(self) -> bool: ...
        def isAlly(self, player: 'ADC2Module.Player') -> bool: ...
        def isGameMaster(self) -> bool: ...
        def setAlly(self, player: 'ADC2Module.Player') -> None: ...
        def toString(self) -> str: ...
        def useHiddenPieces(self) -> bool: ...
    class Pool:
        name: str = ...
        pieces: java.util.List = ...
    class StateFlag:
        MOVE: typing.ClassVar['ADC2Module.StateFlag'] = ...
        ATTACK: typing.ClassVar['ADC2Module.StateFlag'] = ...
        DEFEND: typing.ClassVar['ADC2Module.StateFlag'] = ...
        INFO: typing.ClassVar['ADC2Module.StateFlag'] = ...
        MARKER: typing.ClassVar['ADC2Module.StateFlag'] = ...
        COMBAT: typing.ClassVar['ADC2Module.StateFlag'] = ...
        def __init__(self, string: str, color: java.awt.Color, color2: java.awt.Color, int: int): ...
        def addStatusDots(self, statusDots: 'ADC2Module.StatusDots') -> None: ...
        def drawFlagImage(self, graphics2D: java.awt.Graphics2D) -> None: ...
        def getStatusIconName(self) -> str: ...
    class StatusDots:
        NOT_USED: typing.ClassVar[int] = ...
        MOVED: typing.ClassVar[int] = ...
        IN_COMBAT: typing.ClassVar[int] = ...
        ATTACKED: typing.ClassVar[int] = ...
        DEFENDED: typing.ClassVar[int] = ...
        CLASS_VALUE: typing.ClassVar[int] = ...
        PIECE_VALUE: typing.ClassVar[int] = ...
        DO_NOT_DRAW: typing.ClassVar[int] = ...
        TOP_LEFT: typing.ClassVar[int] = ...
        TOP_CENTER: typing.ClassVar[int] = ...
        TOP_RIGHT: typing.ClassVar[int] = ...
        CENTER_LEFT: typing.ClassVar[int] = ...
        CENTER_CENTER: typing.ClassVar[int] = ...
        CENTER_RIGHT: typing.ClassVar[int] = ...
        BOTTOM_LEFT: typing.ClassVar[int] = ...
        BOTTOM_CENTER: typing.ClassVar[int] = ...
        BOTTOM_RIGHT: typing.ClassVar[int] = ...
        def getColor(self) -> java.awt.Color: ...
        def getPosition(self) -> int: ...
        def getShow(self) -> int: ...
        def getSize(self) -> int: ...
        def getStatusPropertyName(self) -> str: ...
        def getType(self) -> int: ...
    class ValueType(java.lang.Enum['ADC2Module.ValueType']):
        NOT_USED: typing.ClassVar['ADC2Module.ValueType'] = ...
        NUMERIC: typing.ClassVar['ADC2Module.ValueType'] = ...
        TEXT: typing.ClassVar['ADC2Module.ValueType'] = ...
        YESNO: typing.ClassVar['ADC2Module.ValueType'] = ...
        CARD: typing.ClassVar['ADC2Module.ValueType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ADC2Module.ValueType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['ADC2Module.ValueType']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.imports.adc2")``.

    ADC2Module: typing.Type[ADC2Module]
    ADC2ModuleFileFilter: typing.Type[ADC2ModuleFileFilter]
    ADC2Utils: typing.Type[ADC2Utils]
    MapBoard: typing.Type[MapBoard]
    MapBoardFileFilter: typing.Type[MapBoardFileFilter]
    SymbolSet: typing.Type[SymbolSet]
    SymbolSetFileFilter: typing.Type[SymbolSetFileFilter]
