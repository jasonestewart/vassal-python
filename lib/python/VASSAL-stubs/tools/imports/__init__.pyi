import VASSAL.build.module.metadata
import VASSAL.launch
import VASSAL.tools.filechooser
import VASSAL.tools.imports.adc2
import java.awt
import java.awt.event
import java.io
import jpype.protocol
import typing



class FileFormatException(java.io.IOException):
    def __init__(self, string: str): ...

class ImportAction(VASSAL.launch.EditModuleAction):
    def __init__(self, component: java.awt.Component): ...
    @staticmethod
    def buildMetaData(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> VASSAL.build.module.metadata.AbstractMetaData: ...
    def getCaseInsensitiveFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], file2: typing.Union[java.io.File, jpype.protocol.SupportsPath], boolean: bool, fileFilter: VASSAL.tools.filechooser.FileFilter) -> java.io.File: ...
    @staticmethod
    def getFileChooser(component: java.awt.Component) -> VASSAL.tools.filechooser.FileChooser: ...
    @staticmethod
    def getImporterClass(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> typing.Type[typing.Any]: ...
    def loadModule(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    def performAction(self, actionEvent: java.awt.event.ActionEvent) -> None: ...

class Importer:
    def __init__(self): ...
    @staticmethod
    def forceExtension(string: str, string2: str) -> str: ...
    @staticmethod
    def getExtension(string: str) -> str: ...
    @staticmethod
    def getFileName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getUniqueImageFileName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getUniqueImageFileName(string: str, string2: str) -> str: ...
    def importFile(self, importAction: ImportAction, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    def isValidImportFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    @typing.overload
    @staticmethod
    def readNullTerminatedString(inputStream: java.io.InputStream) -> str: ...
    @typing.overload
    @staticmethod
    def readNullTerminatedString(inputStream: java.io.InputStream, int: int) -> str: ...
    @staticmethod
    def readWindowsFileName(inputStream: java.io.InputStream) -> str: ...
    @staticmethod
    def stripExtension(string: str) -> str: ...
    def writeToArchive(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.imports")``.

    FileFormatException: typing.Type[FileFormatException]
    ImportAction: typing.Type[ImportAction]
    Importer: typing.Type[Importer]
    adc2: VASSAL.tools.imports.adc2.__module_protocol__