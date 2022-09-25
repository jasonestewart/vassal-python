import VASSAL.build
import VASSAL.build.module.documentation
import VASSAL.configure
import java.awt.image
import java.beans
import java.util
import javax.swing
import typing



class IconFactory:
    def __init__(self): ...
    @staticmethod
    def addIconFamily(iconFamily: 'IconFamily') -> None: ...
    @staticmethod
    def getIcon(string: str, int: int) -> javax.swing.Icon: ...
    @staticmethod
    def getIconFamily(string: str) -> 'IconFamily': ...
    @staticmethod
    def getIconFamilyNames() -> java.util.List[str]: ...
    @staticmethod
    def getImage(string: str, int: int) -> java.awt.image.BufferedImage: ...
    @staticmethod
    def removeIconFamily(iconFamily: 'IconFamily') -> None: ...
    @staticmethod
    def renameIconFamily(string: str, iconFamily: 'IconFamily') -> None: ...

class IconFamily(VASSAL.build.AbstractConfigurable):
    SCALABLE_ICON: typing.ClassVar[str] = ...
    ICON0: typing.ClassVar[str] = ...
    ICON1: typing.ClassVar[str] = ...
    ICON2: typing.ClassVar[str] = ...
    ICON3: typing.ClassVar[str] = ...
    XSMALL: typing.ClassVar[int] = ...
    SMALL: typing.ClassVar[int] = ...
    MEDIUM: typing.ClassVar[int] = ...
    LARGE: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, stringArray: typing.List[str]): ...
    def addPropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeDescriptions(self) -> typing.List[str]: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    @staticmethod
    def getConfigureTypeName() -> str: ...
    def getConfigurer(self) -> VASSAL.configure.Configurer: ...
    def getHelpFile(self) -> VASSAL.build.module.documentation.HelpFile: ...
    def getIcon(self, int: int) -> javax.swing.Icon: ...
    @staticmethod
    def getIconHeight(int: int) -> int: ...
    @staticmethod
    def getIconSize(string: str) -> int: ...
    @staticmethod
    def getIconSizeNames() -> typing.List[str]: ...
    def getImage(self, int: int) -> java.awt.image.BufferedImage: ...
    def getName(self) -> str: ...
    def getRawIcon(self, int: int) -> javax.swing.Icon: ...
    def getScalableIcon(self) -> javax.swing.Icon: ...
    def isLegacy(self) -> bool: ...
    def removeFrom(self, buildable: VASSAL.build.Buildable) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setConfigureName(self, string: str) -> None: ...
    def setScalableIconPath(self, string: str) -> None: ...
    def setSizeIconPath(self, int: int, string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.icon")``.

    IconFactory: typing.Type[IconFactory]
    IconFamily: typing.Type[IconFamily]
