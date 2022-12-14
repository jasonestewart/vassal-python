import VASSAL.build
import VASSAL.build.module
import VASSAL.build.module.documentation
import VASSAL.build.module.map.boardPicker
import VASSAL.build.module.map.boardPicker.board.mapgrid
import VASSAL.configure
import VASSAL.tools.imageop
import VASSAL.tools.opcache
import java.awt
import java.awt.dnd
import java.awt.event
import java.awt.geom
import java.awt.image
import java.lang
import java.util
import javax.swing
import org.w3c.dom
import typing



class GridEditor(javax.swing.JDialog, java.awt.event.MouseListener, java.awt.event.KeyListener):
    def __init__(self, editableGrid: 'GridEditor.EditableGrid'): ...
    def calculate(self) -> None: ...
    def keyPressed(self, keyEvent: java.awt.event.KeyEvent) -> None: ...
    def keyReleased(self, keyEvent: java.awt.event.KeyEvent) -> None: ...
    def keyTyped(self, keyEvent: java.awt.event.KeyEvent) -> None: ...
    def mouseClicked(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseEntered(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseExited(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mousePressed(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def mouseReleased(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
    def rebuild(self) -> None: ...
    class EditableGrid:
        def getContainer(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridContainer: ...
        def getDx(self) -> float: ...
        def getDy(self) -> float: ...
        def getGridName(self) -> str: ...
        def getGridNumbering(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering: ...
        def getOrigin(self) -> java.awt.Point: ...
        def isSideways(self) -> bool: ...
        def isVisible(self) -> bool: ...
        def setDx(self, double: float) -> None: ...
        def setDy(self, double: float) -> None: ...
        def setOrigin(self, point: java.awt.Point) -> None: ...
        def setSideways(self, boolean: bool) -> None: ...
        def setVisible(self, boolean: bool) -> None: ...

class GridOp(VASSAL.tools.imageop.AbstractTiledOpImpl):
    def __init__(self, imageOp: VASSAL.tools.imageop.ImageOp, mapGrid: 'MapGrid', double: float, boolean: bool, renderingHints: java.awt.RenderingHints): ...
    def equals(self, object: typing.Any) -> bool: ...
    def eval(self) -> java.awt.image.BufferedImage: ...
    def getGrid(self) -> 'MapGrid': ...
    def getHints(self) -> java.awt.RenderingHints: ...
    def getReversed(self) -> bool: ...
    def getScale(self) -> float: ...
    def getSources(self) -> java.util.List[VASSAL.tools.opcache.Op[typing.Any]]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class MapGrid:
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def getGridNumbering(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering: ...
    def getLocation(self, string: str) -> java.awt.Point: ...
    def isLocationRestricted(self, point: java.awt.Point) -> bool: ...
    def isVisible(self) -> bool: ...
    def localizedLocationName(self, point: java.awt.Point) -> str: ...
    def locationName(self, point: java.awt.Point) -> str: ...
    def range(self, point: java.awt.Point, point2: java.awt.Point) -> int: ...
    def snapTo(self, point: java.awt.Point) -> java.awt.Point: ...
    class BadCoords(java.lang.Exception):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, string: str): ...

class Region(VASSAL.build.AbstractConfigurable):
    NAME: typing.ClassVar[str] = ...
    X: typing.ClassVar[str] = ...
    Y: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, region: 'Region'): ...
    @typing.overload
    def __init__(self, point: java.awt.Point): ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def contains(self, point: java.awt.Point) -> bool: ...
    @typing.overload
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    @typing.overload
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool, int: int, int2: int) -> None: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeDescriptions(self) -> typing.List[str]: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    def getBoard(self) -> VASSAL.build.module.map.boardPicker.Board: ...
    @staticmethod
    def getConfigureTypeName() -> str: ...
    def getHelpFile(self) -> VASSAL.build.module.documentation.HelpFile: ...
    def getLocalizedName(self) -> str: ...
    def getName(self) -> str: ...
    def getOrigin(self) -> java.awt.Point: ...
    def getSelectionRect(self) -> java.awt.Rectangle: ...
    def isSelected(self) -> bool: ...
    def localizedLocationName(self) -> str: ...
    def locationName(self) -> str: ...
    def move(self, int: int, int2: int, jComponent: javax.swing.JComponent) -> None: ...
    def moveOrigin(self, int: int, int2: int) -> None: ...
    def removeFrom(self, buildable: VASSAL.build.Buildable) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setOrigin(self, point: java.awt.Point) -> None: ...
    def setSelected(self, boolean: bool) -> None: ...

class SolidColorOp(VASSAL.tools.imageop.AbstractTiledOpImpl):
    def __init__(self, color: java.awt.Color, int: int, int2: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def eval(self) -> java.awt.image.BufferedImage: ...
    def getColor(self) -> java.awt.Color: ...
    def getSources(self) -> java.util.List[VASSAL.tools.opcache.Op[typing.Any]]: ...
    @typing.overload
    def getTileOp(self, int: int, int2: int) -> VASSAL.tools.imageop.ImageOp: ...
    @typing.overload
    def getTileOp(self, point: java.awt.Point) -> VASSAL.tools.imageop.ImageOp: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class GeometricGrid(MapGrid):
    def getGridShape(self, point: java.awt.Point, int: int) -> java.awt.geom.Area: ...

class RegionGrid(VASSAL.build.AbstractConfigurable, MapGrid, VASSAL.configure.ConfigureTree.Mutable):
    SNAPTO: typing.ClassVar[str] = ...
    VISIBLE: typing.ClassVar[str] = ...
    FONT_SIZE: typing.ClassVar[str] = ...
    def __init__(self): ...
    def addRegion(self, region: Region) -> None: ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def configureRegions(self) -> None: ...
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def findRegion(self, string: str) -> Region: ...
    def forceDraw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeDescriptions(self) -> typing.List[str]: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    def getAttributeVisibility(self, string: str) -> VASSAL.configure.VisibilityCondition: ...
    def getBoard(self) -> VASSAL.build.module.map.boardPicker.Board: ...
    def getConfigureName(self) -> str: ...
    @staticmethod
    def getConfigureTypeName() -> str: ...
    def getConfigurer(self) -> VASSAL.configure.Configurer: ...
    def getFontSize(self) -> int: ...
    def getGridNumbering(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering: ...
    def getHelpFile(self) -> VASSAL.build.module.documentation.HelpFile: ...
    def getLocation(self, string: str) -> java.awt.Point: ...
    def getRegion(self, point: java.awt.Point) -> Region: ...
    def isLocationRestricted(self, point: java.awt.Point) -> bool: ...
    def isVisible(self) -> bool: ...
    def localizedLocationName(self, point: java.awt.Point) -> str: ...
    def locationName(self, point: java.awt.Point) -> str: ...
    def range(self, point: java.awt.Point, point2: java.awt.Point) -> int: ...
    def removeAllRegions(self) -> None: ...
    def removeFrom(self, buildable: VASSAL.build.Buildable) -> None: ...
    def removeRegion(self, region: Region) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setGridNumbering(self, gridNumbering: VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering) -> None: ...
    def setVisible(self, boolean: bool) -> None: ...
    def snapTo(self, point: java.awt.Point) -> java.awt.Point: ...
    def unSelect(self, region: Region) -> None: ...
    def unSelectAll(self) -> None: ...
    class Config(javax.swing.JFrame, java.awt.event.MouseListener, java.awt.event.MouseMotionListener, java.awt.event.ActionListener, java.awt.event.KeyListener):
        def __init__(self, regionGrid: 'RegionGrid'): ...
        def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
        def getSelectedBox(self) -> java.awt.Rectangle: ...
        def getSelectionRect(self) -> java.awt.Rectangle: ...
        def init(self) -> None: ...
        def keyPressed(self, keyEvent: java.awt.event.KeyEvent) -> None: ...
        def keyReleased(self, keyEvent: java.awt.event.KeyEvent) -> None: ...
        def keyTyped(self, keyEvent: java.awt.event.KeyEvent) -> None: ...
        def mouseClicked(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def mouseDragged(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def mouseEntered(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def mouseExited(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def mouseMoved(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def mousePressed(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def mouseReleased(self, mouseEvent: java.awt.event.MouseEvent) -> None: ...
        def restore(self) -> None: ...
        def save(self) -> None: ...
        class View(javax.swing.JPanel, java.awt.dnd.DropTargetListener, java.awt.dnd.DragGestureListener, java.awt.dnd.DragSourceListener, java.awt.dnd.DragSourceMotionListener):
            def __init__(self, board: VASSAL.build.module.map.boardPicker.Board, regionGrid: 'RegionGrid', config: 'RegionGrid.Config'): ...
            def dragDropEnd(self, dragSourceDropEvent: java.awt.dnd.DragSourceDropEvent) -> None: ...
            @typing.overload
            def dragEnter(self, dragSourceDragEvent: java.awt.dnd.DragSourceDragEvent) -> None: ...
            @typing.overload
            def dragEnter(self, dropTargetDragEvent: java.awt.dnd.DropTargetDragEvent) -> None: ...
            @typing.overload
            def dragExit(self, dragSourceEvent: java.awt.dnd.DragSourceEvent) -> None: ...
            @typing.overload
            def dragExit(self, dropTargetEvent: java.awt.dnd.DropTargetEvent) -> None: ...
            def dragGestureRecognized(self, dragGestureEvent: java.awt.dnd.DragGestureEvent) -> None: ...
            def dragMouseMoved(self, dragSourceDragEvent: java.awt.dnd.DragSourceDragEvent) -> None: ...
            @typing.overload
            def dragOver(self, dragSourceDragEvent: java.awt.dnd.DragSourceDragEvent) -> None: ...
            @typing.overload
            def dragOver(self, dropTargetDragEvent: java.awt.dnd.DropTargetDragEvent) -> None: ...
            def drop(self, dropTargetDropEvent: java.awt.dnd.DropTargetDropEvent) -> None: ...
            @typing.overload
            def dropActionChanged(self, dragSourceDragEvent: java.awt.dnd.DragSourceDragEvent) -> None: ...
            @typing.overload
            def dropActionChanged(self, dropTargetDragEvent: java.awt.dnd.DropTargetDragEvent) -> None: ...
            def getPreferredSize(self) -> java.awt.Dimension: ...
            def paint(self, graphics: java.awt.Graphics) -> None: ...
            def update(self, graphics: java.awt.Graphics) -> None: ...

class HexGrid(VASSAL.build.AbstractConfigurable, GeometricGrid, GridEditor.EditableGrid):
    X0: typing.ClassVar[str] = ...
    Y0: typing.ClassVar[str] = ...
    DY: typing.ClassVar[str] = ...
    DX: typing.ClassVar[str] = ...
    VISIBLE: typing.ClassVar[str] = ...
    DOTS_VISIBLE: typing.ClassVar[str] = ...
    CORNERS: typing.ClassVar[str] = ...
    EDGES: typing.ClassVar[str] = ...
    SIDEWAYS: typing.ClassVar[str] = ...
    COLOR: typing.ClassVar[str] = ...
    SNAP_SCALE: typing.ClassVar[str] = ...
    SNAP_TO: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, double: float, double2: float, boolean: bool): ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def editGrid(self) -> None: ...
    def forceDraw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeDescriptions(self) -> typing.List[str]: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    def getAttributeVisibility(self, string: str) -> VASSAL.configure.VisibilityCondition: ...
    def getConfigureName(self) -> str: ...
    @staticmethod
    def getConfigureTypeName() -> str: ...
    def getConfigurer(self) -> VASSAL.configure.Configurer: ...
    def getContainer(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridContainer: ...
    def getDx(self) -> float: ...
    def getDy(self) -> float: ...
    def getGridName(self) -> str: ...
    def getGridNumbering(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering: ...
    def getGridShape(self, point: java.awt.Point, int: int) -> java.awt.geom.Area: ...
    def getHelpFile(self) -> VASSAL.build.module.documentation.HelpFile: ...
    def getHexSize(self) -> float: ...
    def getHexWidth(self) -> float: ...
    def getLocation(self, string: str) -> java.awt.Point: ...
    def getOrigin(self) -> java.awt.Point: ...
    def getSnapScale(self) -> int: ...
    def isCornersLegal(self) -> bool: ...
    def isEdgesLegal(self) -> bool: ...
    def isLocationRestricted(self, point: java.awt.Point) -> bool: ...
    def isSideways(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def localizedLocationName(self, point: java.awt.Point) -> str: ...
    def locationName(self, point: java.awt.Point) -> str: ...
    def range(self, point: java.awt.Point, point2: java.awt.Point) -> int: ...
    def removeFrom(self, buildable: VASSAL.build.Buildable) -> None: ...
    def rotate(self, point: java.awt.Point) -> None: ...
    def rotateIfSideways(self, point: java.awt.Point) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setCornersLegal(self, boolean: bool) -> None: ...
    def setDx(self, double: float) -> None: ...
    def setDy(self, double: float) -> None: ...
    def setEdgesLegal(self, boolean: bool) -> None: ...
    def setGridNumbering(self, gridNumbering: VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering) -> None: ...
    def setHexSize(self, double: float) -> None: ...
    def setHexWidth(self, double: float) -> None: ...
    def setOrigin(self, point: java.awt.Point) -> None: ...
    def setSideways(self, boolean: bool) -> None: ...
    def setSnapScale(self, int: int) -> None: ...
    def setVisible(self, boolean: bool) -> None: ...
    def snapTo(self, point: java.awt.Point) -> java.awt.Point: ...
    def snapToHex(self, point: java.awt.Point) -> java.awt.Point: ...
    def snapToHexSide(self, point: java.awt.Point) -> java.awt.Point: ...
    def snapToHexVertex(self, point: java.awt.Point) -> java.awt.Point: ...
    class HexGridEditor(GridEditor):
        def __init__(self, editableGrid: GridEditor.EditableGrid): ...
        def calculate(self) -> None: ...

class SquareGrid(VASSAL.build.AbstractConfigurable, GeometricGrid, GridEditor.EditableGrid):
    DX: typing.ClassVar[str] = ...
    DY: typing.ClassVar[str] = ...
    X0: typing.ClassVar[str] = ...
    Y0: typing.ClassVar[str] = ...
    VISIBLE: typing.ClassVar[str] = ...
    CORNERS: typing.ClassVar[str] = ...
    EDGES: typing.ClassVar[str] = ...
    COLOR: typing.ClassVar[str] = ...
    DOTS_VISIBLE: typing.ClassVar[str] = ...
    RANGE: typing.ClassVar[str] = ...
    RANGE_MANHATTAN: typing.ClassVar[str] = ...
    RANGE_METRIC: typing.ClassVar[str] = ...
    SNAP_TO: typing.ClassVar[str] = ...
    def __init__(self): ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def editGrid(self) -> None: ...
    def forceDraw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeDescriptions(self) -> typing.List[str]: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    def getAttributeVisibility(self, string: str) -> VASSAL.configure.VisibilityCondition: ...
    def getConfigureName(self) -> str: ...
    @staticmethod
    def getConfigureTypeName() -> str: ...
    def getConfigurer(self) -> VASSAL.configure.Configurer: ...
    def getContainer(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridContainer: ...
    def getDx(self) -> float: ...
    def getDy(self) -> float: ...
    def getGridName(self) -> str: ...
    def getGridNumbering(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering: ...
    def getGridShape(self, point: java.awt.Point, int: int) -> java.awt.geom.Area: ...
    def getHelpFile(self) -> VASSAL.build.module.documentation.HelpFile: ...
    def getLocation(self, string: str) -> java.awt.Point: ...
    def getOrigin(self) -> java.awt.Point: ...
    def getSingleSquareShape(self, int: int, int2: int) -> java.awt.geom.Area: ...
    def getSnapScale(self) -> int: ...
    def isLocationRestricted(self, point: java.awt.Point) -> bool: ...
    def isSideways(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def localizedLocationName(self, point: java.awt.Point) -> str: ...
    def locationName(self, point: java.awt.Point) -> str: ...
    def range(self, point: java.awt.Point, point2: java.awt.Point) -> int: ...
    def removeFrom(self, buildable: VASSAL.build.Buildable) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setDx(self, double: float) -> None: ...
    def setDy(self, double: float) -> None: ...
    def setGridNumbering(self, gridNumbering: VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering) -> None: ...
    def setOrigin(self, point: java.awt.Point) -> None: ...
    def setSideways(self, boolean: bool) -> None: ...
    def setSnapScale(self, int: int) -> None: ...
    def setVisible(self, boolean: bool) -> None: ...
    def snapTo(self, point: java.awt.Point) -> java.awt.Point: ...
    class RangeOptions(VASSAL.configure.StringEnum):
        def __init__(self): ...
        def getValidValues(self, autoConfigurable: VASSAL.build.AutoConfigurable) -> typing.List[str]: ...
    class SquareGridEditor(GridEditor):
        def __init__(self, editableGrid: GridEditor.EditableGrid): ...
        def calculate(self) -> None: ...

class ZonedGrid(VASSAL.build.AbstractConfigurable, GeometricGrid, VASSAL.build.module.map.boardPicker.board.mapgrid.GridContainer):
    def __init__(self): ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def addZone(self, zone: VASSAL.build.module.map.boardPicker.board.mapgrid.Zone) -> None: ...
    def build(self, element: org.w3c.dom.Element) -> None: ...
    def contains(self, point: java.awt.Point) -> bool: ...
    def draw(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle, rectangle2: java.awt.Rectangle, double: float, boolean: bool) -> None: ...
    @typing.overload
    def findZone(self, point: java.awt.Point) -> VASSAL.build.module.map.boardPicker.board.mapgrid.Zone: ...
    @typing.overload
    def findZone(self, string: str) -> VASSAL.build.module.map.boardPicker.board.mapgrid.Zone: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeDescriptions(self) -> typing.List[str]: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    def getBackgroundGrid(self) -> MapGrid: ...
    def getBoard(self) -> VASSAL.build.module.map.boardPicker.Board: ...
    @staticmethod
    def getConfigureTypeName() -> str: ...
    def getConfigurer(self) -> VASSAL.configure.Configurer: ...
    def getContainer(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridContainer: ...
    def getGridNumbering(self) -> VASSAL.build.module.map.boardPicker.board.mapgrid.GridNumbering: ...
    def getGridShape(self, point: java.awt.Point, int: int) -> java.awt.geom.Area: ...
    def getHelpFile(self) -> VASSAL.build.module.documentation.HelpFile: ...
    def getLocation(self, string: str) -> java.awt.Point: ...
    def getMap(self) -> VASSAL.build.module.Map: ...
    def getSize(self) -> java.awt.Dimension: ...
    def getZoneHighlight(self, string: str) -> VASSAL.build.module.map.boardPicker.board.mapgrid.ZoneHighlight: ...
    def getZones(self) -> java.util.Iterator[VASSAL.build.module.map.boardPicker.board.mapgrid.Zone]: ...
    def isLocationRestricted(self, point: java.awt.Point) -> bool: ...
    def isVisible(self) -> bool: ...
    def localizedLocationName(self, point: java.awt.Point) -> str: ...
    def locationName(self, point: java.awt.Point) -> str: ...
    def range(self, point: java.awt.Point, point2: java.awt.Point) -> int: ...
    def removeFrom(self, buildable: VASSAL.build.Buildable) -> None: ...
    def removeGrid(self, mapGrid: MapGrid) -> None: ...
    def removeZone(self, zone: VASSAL.build.module.map.boardPicker.board.mapgrid.Zone) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setBackgroundGrid(self, mapGrid: MapGrid) -> None: ...
    def setGrid(self, mapGrid: MapGrid) -> None: ...
    def setZoneHighlighter(self, zonedGridHighlighter: VASSAL.build.module.map.boardPicker.board.mapgrid.ZonedGridHighlighter) -> None: ...
    def snapTo(self, point: java.awt.Point) -> java.awt.Point: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.build.module.map.boardPicker.board")``.

    GeometricGrid: typing.Type[GeometricGrid]
    GridEditor: typing.Type[GridEditor]
    GridOp: typing.Type[GridOp]
    HexGrid: typing.Type[HexGrid]
    MapGrid: typing.Type[MapGrid]
    Region: typing.Type[Region]
    RegionGrid: typing.Type[RegionGrid]
    SolidColorOp: typing.Type[SolidColorOp]
    SquareGrid: typing.Type[SquareGrid]
    ZonedGrid: typing.Type[ZonedGrid]
    mapgrid: VASSAL.build.module.map.boardPicker.board.mapgrid.__module_protocol__
