import VASSAL.build
import VASSAL.chat
import VASSAL.command
import VASSAL.configure
import VASSAL.counters
import VASSAL.i18n
import VASSAL.launch
import VASSAL.preferences
import VASSAL.property
import VASSAL.script
import VASSAL.search
import VASSAL.tools
import java.awt
import java.io
import typing



class Info:
    javaBinPath: typing.ClassVar[str] = ...
    @staticmethod
    def getBaseDir() -> java.io.File: ...
    @staticmethod
    def getBinDir() -> java.io.File: ...
    @staticmethod
    def getCacheDir() -> java.io.File: ...
    @staticmethod
    def getConfDir() -> java.io.File: ...
    @staticmethod
    def getDocDir() -> java.io.File: ...
    @staticmethod
    def getErrorLogPath() -> java.io.File: ...
    @staticmethod
    def getHomeDir() -> java.io.File: ...
    @staticmethod
    def getJavaBinPath() -> java.io.File: ...
    @staticmethod
    def getPrefsDir() -> java.io.File: ...
    @staticmethod
    def getReportableVersion() -> str: ...
    @staticmethod
    def getScreenBounds(component: java.awt.Component) -> java.awt.Rectangle: ...
    @staticmethod
    def getTempDir() -> java.io.File: ...
    @staticmethod
    def getVersion() -> str: ...
    @staticmethod
    def hasOldFormat(string: str) -> bool: ...
    @staticmethod
    def isMacOSX() -> bool: ...
    @staticmethod
    def isModuleTooNew(string: str) -> bool: ...
    @staticmethod
    def setConfig(config: VASSAL.launch.Config) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL")``.

    Info: typing.Type[Info]
    build: VASSAL.build.__module_protocol__
    chat: VASSAL.chat.__module_protocol__
    command: VASSAL.command.__module_protocol__
    configure: VASSAL.configure.__module_protocol__
    counters: VASSAL.counters.__module_protocol__
    i18n: VASSAL.i18n.__module_protocol__
    launch: VASSAL.launch.__module_protocol__
    preferences: VASSAL.preferences.__module_protocol__
    property: VASSAL.property.__module_protocol__
    script: VASSAL.script.__module_protocol__
    search: VASSAL.search.__module_protocol__
    tools: VASSAL.tools.__module_protocol__
