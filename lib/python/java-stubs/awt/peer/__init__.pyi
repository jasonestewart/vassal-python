import java.awt
import java.awt.desktop
import java.awt.event
import java.awt.im
import java.awt.image
import java.io
import java.net
import java.util
import javax.swing
import jpype.protocol
import sun.java2d.pipe
import typing



class ComponentPeer:
    SET_LOCATION: typing.ClassVar[int] = ...
    SET_SIZE: typing.ClassVar[int] = ...
    SET_BOUNDS: typing.ClassVar[int] = ...
    SET_CLIENT_SIZE: typing.ClassVar[int] = ...
    RESET_OPERATION: typing.ClassVar[int] = ...
    NO_EMBEDDED_CHECK: typing.ClassVar[int] = ...
    DEFAULT_OPERATION: typing.ClassVar[int] = ...
    def applyShape(self, region: sun.java2d.pipe.Region) -> None: ...
    def canDetermineObscurity(self) -> bool: ...
    def checkImage(self, image: java.awt.Image, int: int, int2: int, imageObserver: java.awt.image.ImageObserver) -> int: ...
    def coalescePaintEvent(self, paintEvent: java.awt.event.PaintEvent) -> None: ...
    def createBuffers(self, int: int, bufferCapabilities: java.awt.BufferCapabilities) -> None: ...
    @typing.overload
    def createImage(self, int: int, int2: int) -> java.awt.Image: ...
    @typing.overload
    def createImage(self, imageProducer: java.awt.image.ImageProducer) -> java.awt.Image: ...
    def createVolatileImage(self, int: int, int2: int) -> java.awt.image.VolatileImage: ...
    def destroyBuffers(self) -> None: ...
    def dispose(self) -> None: ...
    def flip(self, int: int, int2: int, int3: int, int4: int, flipContents: java.awt.BufferCapabilities.FlipContents) -> None: ...
    def getBackBuffer(self) -> java.awt.Image: ...
    def getColorModel(self) -> java.awt.image.ColorModel: ...
    def getFontMetrics(self, font: java.awt.Font) -> java.awt.FontMetrics: ...
    def getGraphics(self) -> java.awt.Graphics: ...
    def getGraphicsConfiguration(self) -> java.awt.GraphicsConfiguration: ...
    def getLocationOnScreen(self) -> java.awt.Point: ...
    def getMinimumSize(self) -> java.awt.Dimension: ...
    def getPreferredSize(self) -> java.awt.Dimension: ...
    def handleEvent(self, aWTEvent: java.awt.AWTEvent) -> None: ...
    def handlesWheelScrolling(self) -> bool: ...
    def isFocusable(self) -> bool: ...
    def isObscured(self) -> bool: ...
    def isReparentSupported(self) -> bool: ...
    def layout(self) -> None: ...
    def paint(self, graphics: java.awt.Graphics) -> None: ...
    def prepareImage(self, image: java.awt.Image, int: int, int2: int, imageObserver: java.awt.image.ImageObserver) -> bool: ...
    def reparent(self, containerPeer: 'ContainerPeer') -> None: ...
    def requestFocus(self, component: java.awt.Component, boolean: bool, boolean2: bool, long: int, cause: java.awt.event.FocusEvent.Cause) -> bool: ...
    def setBackground(self, color: java.awt.Color) -> None: ...
    def setBounds(self, int: int, int2: int, int3: int, int4: int, int5: int) -> None: ...
    def setEnabled(self, boolean: bool) -> None: ...
    def setFont(self, font: java.awt.Font) -> None: ...
    def setForeground(self, color: java.awt.Color) -> None: ...
    def setVisible(self, boolean: bool) -> None: ...
    def setZOrder(self, componentPeer: 'ComponentPeer') -> None: ...
    def updateCursorImmediately(self) -> None: ...
    def updateGraphicsData(self, graphicsConfiguration: java.awt.GraphicsConfiguration) -> bool: ...

class DesktopPeer:
    def addAppEventListener(self, systemEventListener: java.awt.desktop.SystemEventListener) -> None: ...
    def browse(self, uRI: java.net.URI) -> None: ...
    def browseFileDirectory(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    def disableSuddenTermination(self) -> None: ...
    def edit(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    def enableSuddenTermination(self) -> None: ...
    def isSupported(self, action: java.awt.Desktop.Action) -> bool: ...
    def mail(self, uRI: java.net.URI) -> None: ...
    def moveToTrash(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    def open(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    def openHelpViewer(self) -> None: ...
    def removeAppEventListener(self, systemEventListener: java.awt.desktop.SystemEventListener) -> None: ...
    def requestForeground(self, boolean: bool) -> None: ...
    def setAboutHandler(self, aboutHandler: java.awt.desktop.AboutHandler) -> None: ...
    def setDefaultMenuBar(self, jMenuBar: javax.swing.JMenuBar) -> None: ...
    def setOpenFileHandler(self, openFilesHandler: java.awt.desktop.OpenFilesHandler) -> None: ...
    def setOpenURIHandler(self, openURIHandler: java.awt.desktop.OpenURIHandler) -> None: ...
    def setPreferencesHandler(self, preferencesHandler: java.awt.desktop.PreferencesHandler) -> None: ...
    def setPrintFileHandler(self, printFilesHandler: java.awt.desktop.PrintFilesHandler) -> None: ...
    def setQuitHandler(self, quitHandler: java.awt.desktop.QuitHandler) -> None: ...
    def setQuitStrategy(self, quitStrategy: java.awt.desktop.QuitStrategy) -> None: ...

class FontPeer: ...

class KeyboardFocusManagerPeer:
    def clearGlobalFocusOwner(self, window: java.awt.Window) -> None: ...
    def getCurrentFocusOwner(self) -> java.awt.Component: ...
    def getCurrentFocusedWindow(self) -> java.awt.Window: ...
    def setCurrentFocusOwner(self, component: java.awt.Component) -> None: ...
    def setCurrentFocusedWindow(self, window: java.awt.Window) -> None: ...

class MenuComponentPeer:
    def dispose(self) -> None: ...
    def setFont(self, font: java.awt.Font) -> None: ...

class MouseInfoPeer:
    def fillPointWithCoords(self, point: java.awt.Point) -> int: ...
    def isWindowUnderMouse(self, window: java.awt.Window) -> bool: ...

class RobotPeer:
    def getRGBPixel(self, int: int, int2: int) -> int: ...
    def getRGBPixels(self, rectangle: java.awt.Rectangle) -> typing.List[int]: ...
    def keyPress(self, int: int) -> None: ...
    def keyRelease(self, int: int) -> None: ...
    def mouseMove(self, int: int, int2: int) -> None: ...
    def mousePress(self, int: int) -> None: ...
    def mouseRelease(self, int: int) -> None: ...
    def mouseWheel(self, int: int) -> None: ...

class SystemTrayPeer:
    def getTrayIconSize(self) -> java.awt.Dimension: ...

class TaskbarPeer:
    def getIconImage(self) -> java.awt.Image: ...
    def getMenu(self) -> java.awt.PopupMenu: ...
    def isSupported(self, feature: java.awt.Taskbar.Feature) -> bool: ...
    def requestUserAttention(self, boolean: bool, boolean2: bool) -> None: ...
    def requestWindowUserAttention(self, window: java.awt.Window) -> None: ...
    def setIconBadge(self, string: str) -> None: ...
    def setIconImage(self, image: java.awt.Image) -> None: ...
    def setMenu(self, popupMenu: java.awt.PopupMenu) -> None: ...
    def setProgressValue(self, int: int) -> None: ...
    def setWindowIconBadge(self, window: java.awt.Window, image: java.awt.Image) -> None: ...
    def setWindowProgressState(self, window: java.awt.Window, state: java.awt.Taskbar.State) -> None: ...
    def setWindowProgressValue(self, window: java.awt.Window, int: int) -> None: ...

class TrayIconPeer:
    def displayMessage(self, string: str, string2: str, string3: str) -> None: ...
    def dispose(self) -> None: ...
    def setToolTip(self, string: str) -> None: ...
    def showPopupMenu(self, int: int, int2: int) -> None: ...
    def updateImage(self) -> None: ...

class ButtonPeer(ComponentPeer):
    def setLabel(self, string: str) -> None: ...

class CanvasPeer(ComponentPeer):
    def getAppropriateGraphicsConfiguration(self, graphicsConfiguration: java.awt.GraphicsConfiguration) -> java.awt.GraphicsConfiguration: ...

class CheckboxPeer(ComponentPeer):
    def setCheckboxGroup(self, checkboxGroup: java.awt.CheckboxGroup) -> None: ...
    def setLabel(self, string: str) -> None: ...
    def setState(self, boolean: bool) -> None: ...

class ChoicePeer(ComponentPeer):
    def add(self, string: str, int: int) -> None: ...
    def remove(self, int: int) -> None: ...
    def removeAll(self) -> None: ...
    def select(self, int: int) -> None: ...

class ContainerPeer(ComponentPeer):
    def beginLayout(self) -> None: ...
    def beginValidate(self) -> None: ...
    def endLayout(self) -> None: ...
    def endValidate(self) -> None: ...
    def getInsets(self) -> java.awt.Insets: ...

class LabelPeer(ComponentPeer):
    def setAlignment(self, int: int) -> None: ...
    def setText(self, string: str) -> None: ...

class LightweightPeer(ComponentPeer): ...

class ListPeer(ComponentPeer):
    def add(self, string: str, int: int) -> None: ...
    def delItems(self, int: int, int2: int) -> None: ...
    def deselect(self, int: int) -> None: ...
    @typing.overload
    def getMinimumSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getMinimumSize(self, int: int) -> java.awt.Dimension: ...
    @typing.overload
    def getPreferredSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getPreferredSize(self, int: int) -> java.awt.Dimension: ...
    def getSelectedIndexes(self) -> typing.List[int]: ...
    def makeVisible(self, int: int) -> None: ...
    def removeAll(self) -> None: ...
    def select(self, int: int) -> None: ...
    def setMultipleMode(self, boolean: bool) -> None: ...

class MenuBarPeer(MenuComponentPeer):
    def addHelpMenu(self, menu: java.awt.Menu) -> None: ...
    def addMenu(self, menu: java.awt.Menu) -> None: ...
    def delMenu(self, int: int) -> None: ...

class MenuItemPeer(MenuComponentPeer):
    def setEnabled(self, boolean: bool) -> None: ...
    def setLabel(self, string: str) -> None: ...

class ScrollbarPeer(ComponentPeer):
    def setLineIncrement(self, int: int) -> None: ...
    def setPageIncrement(self, int: int) -> None: ...
    def setValues(self, int: int, int2: int, int3: int, int4: int) -> None: ...

class TextComponentPeer(ComponentPeer):
    def getCaretPosition(self) -> int: ...
    def getInputMethodRequests(self) -> java.awt.im.InputMethodRequests: ...
    def getSelectionEnd(self) -> int: ...
    def getSelectionStart(self) -> int: ...
    def getText(self) -> str: ...
    def select(self, int: int, int2: int) -> None: ...
    def setCaretPosition(self, int: int) -> None: ...
    def setEditable(self, boolean: bool) -> None: ...
    def setText(self, string: str) -> None: ...

class CheckboxMenuItemPeer(MenuItemPeer):
    def setState(self, boolean: bool) -> None: ...

class MenuPeer(MenuItemPeer):
    def addItem(self, menuItem: java.awt.MenuItem) -> None: ...
    def addSeparator(self) -> None: ...
    def delItem(self, int: int) -> None: ...

class PanelPeer(ContainerPeer): ...

class ScrollPanePeer(ContainerPeer):
    def childResized(self, int: int, int2: int) -> None: ...
    def getHScrollbarHeight(self) -> int: ...
    def getVScrollbarWidth(self) -> int: ...
    def setScrollPosition(self, int: int, int2: int) -> None: ...
    def setUnitIncrement(self, adjustable: java.awt.Adjustable, int: int) -> None: ...
    def setValue(self, adjustable: java.awt.Adjustable, int: int) -> None: ...

class TextAreaPeer(TextComponentPeer):
    @typing.overload
    def getMinimumSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getMinimumSize(self, int: int, int2: int) -> java.awt.Dimension: ...
    @typing.overload
    def getPreferredSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getPreferredSize(self, int: int, int2: int) -> java.awt.Dimension: ...
    def insert(self, string: str, int: int) -> None: ...
    def replaceRange(self, string: str, int: int, int2: int) -> None: ...

class TextFieldPeer(TextComponentPeer):
    @typing.overload
    def getMinimumSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getMinimumSize(self, int: int) -> java.awt.Dimension: ...
    @typing.overload
    def getPreferredSize(self) -> java.awt.Dimension: ...
    @typing.overload
    def getPreferredSize(self, int: int) -> java.awt.Dimension: ...
    def setEchoChar(self, char: str) -> None: ...

class WindowPeer(ContainerPeer):
    def repositionSecurityWarning(self) -> None: ...
    def setModalBlocked(self, dialog: java.awt.Dialog, boolean: bool) -> None: ...
    def setOpacity(self, float: float) -> None: ...
    def setOpaque(self, boolean: bool) -> None: ...
    def toBack(self) -> None: ...
    def toFront(self) -> None: ...
    def updateAlwaysOnTopState(self) -> None: ...
    def updateFocusableWindowState(self) -> None: ...
    def updateIconImages(self) -> None: ...
    def updateMinimumSize(self) -> None: ...
    def updateWindow(self) -> None: ...

class DialogPeer(WindowPeer):
    def blockWindows(self, list: java.util.List[java.awt.Window]) -> None: ...
    def setResizable(self, boolean: bool) -> None: ...
    def setTitle(self, string: str) -> None: ...

class FramePeer(WindowPeer):
    def emulateActivation(self, boolean: bool) -> None: ...
    def getBoundsPrivate(self) -> java.awt.Rectangle: ...
    def getState(self) -> int: ...
    def setBoundsPrivate(self, int: int, int2: int, int3: int, int4: int) -> None: ...
    def setMaximizedBounds(self, rectangle: java.awt.Rectangle) -> None: ...
    def setMenuBar(self, menuBar: java.awt.MenuBar) -> None: ...
    def setResizable(self, boolean: bool) -> None: ...
    def setState(self, int: int) -> None: ...
    def setTitle(self, string: str) -> None: ...

class PopupMenuPeer(MenuPeer):
    def show(self, event: java.awt.Event) -> None: ...

class FileDialogPeer(DialogPeer):
    def setDirectory(self, string: str) -> None: ...
    def setFile(self, string: str) -> None: ...
    def setFilenameFilter(self, filenameFilter: typing.Union[java.io.FilenameFilter, typing.Callable]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.peer")``.

    ButtonPeer: typing.Type[ButtonPeer]
    CanvasPeer: typing.Type[CanvasPeer]
    CheckboxMenuItemPeer: typing.Type[CheckboxMenuItemPeer]
    CheckboxPeer: typing.Type[CheckboxPeer]
    ChoicePeer: typing.Type[ChoicePeer]
    ComponentPeer: typing.Type[ComponentPeer]
    ContainerPeer: typing.Type[ContainerPeer]
    DesktopPeer: typing.Type[DesktopPeer]
    DialogPeer: typing.Type[DialogPeer]
    FileDialogPeer: typing.Type[FileDialogPeer]
    FontPeer: typing.Type[FontPeer]
    FramePeer: typing.Type[FramePeer]
    KeyboardFocusManagerPeer: typing.Type[KeyboardFocusManagerPeer]
    LabelPeer: typing.Type[LabelPeer]
    LightweightPeer: typing.Type[LightweightPeer]
    ListPeer: typing.Type[ListPeer]
    MenuBarPeer: typing.Type[MenuBarPeer]
    MenuComponentPeer: typing.Type[MenuComponentPeer]
    MenuItemPeer: typing.Type[MenuItemPeer]
    MenuPeer: typing.Type[MenuPeer]
    MouseInfoPeer: typing.Type[MouseInfoPeer]
    PanelPeer: typing.Type[PanelPeer]
    PopupMenuPeer: typing.Type[PopupMenuPeer]
    RobotPeer: typing.Type[RobotPeer]
    ScrollPanePeer: typing.Type[ScrollPanePeer]
    ScrollbarPeer: typing.Type[ScrollbarPeer]
    SystemTrayPeer: typing.Type[SystemTrayPeer]
    TaskbarPeer: typing.Type[TaskbarPeer]
    TextAreaPeer: typing.Type[TextAreaPeer]
    TextComponentPeer: typing.Type[TextComponentPeer]
    TextFieldPeer: typing.Type[TextFieldPeer]
    TrayIconPeer: typing.Type[TrayIconPeer]
    WindowPeer: typing.Type[WindowPeer]
