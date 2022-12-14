import VASSAL.build
import VASSAL.build.module
import VASSAL.tools
import VASSAL.tools.io
import java.io
import java.util.zip
import jpype.protocol
import typing



class AbstractMetaData:
    def __init__(self): ...
    @typing.overload
    def copyModuleMetadata(self, archiveWriter: VASSAL.tools.ArchiveWriter) -> None: ...
    @typing.overload
    def copyModuleMetadata(self, fileArchive: VASSAL.tools.io.FileArchive) -> None: ...
    @typing.overload
    def copyModuleMetadata(self, zipWriter: VASSAL.tools.io.ZipWriter) -> None: ...
    def formatLastSaved(self) -> str: ...
    def getDescription(self) -> str: ...
    def getLastSaved(self) -> str: ...
    def getLocalizedDescription(self) -> str: ...
    def getMetaDataVersion(self) -> str: ...
    def getVassalVersion(self) -> str: ...
    def getVersion(self) -> str: ...
    def getZipEntryName(self) -> str: ...
    @typing.overload
    def save(self, archiveWriter: VASSAL.tools.ArchiveWriter) -> None: ...
    @typing.overload
    def save(self, fileArchive: VASSAL.tools.io.FileArchive) -> None: ...
    @typing.overload
    def save(self, zipWriter: VASSAL.tools.io.ZipWriter) -> None: ...
    @typing.overload
    def setDescription(self, attribute: 'AbstractMetaData.Attribute') -> None: ...
    @typing.overload
    def setDescription(self, string: str) -> None: ...
    def setLastSaved(self, string: str) -> None: ...
    def setVassalVersion(self, string: str) -> None: ...
    def setVersion(self, string: str) -> None: ...
    class Attribute: ...

class MetaDataFactory:
    def __init__(self): ...
    @staticmethod
    def buildMetaData(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> AbstractMetaData: ...

class ExtensionMetaData(AbstractMetaData):
    ZIP_ENTRY_NAME: typing.ClassVar[str] = ...
    DATA_VERSION: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, moduleExtension: VASSAL.build.module.ModuleExtension): ...
    @typing.overload
    def __init__(self, zipFile: java.util.zip.ZipFile): ...
    def getMetaDataVersion(self) -> str: ...
    def getModuleName(self) -> str: ...
    def getModuleVersion(self) -> str: ...
    def getZipEntryName(self) -> str: ...
    def read(self, zipFile: java.util.zip.ZipFile) -> None: ...
    @typing.overload
    def save(self, fileArchive: VASSAL.tools.io.FileArchive) -> None: ...
    @typing.overload
    def save(self, archiveWriter: VASSAL.tools.ArchiveWriter) -> None: ...
    @typing.overload
    def save(self, zipWriter: VASSAL.tools.io.ZipWriter) -> None: ...

class ImportMetaData(AbstractMetaData):
    DATA_VERSION: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getMetaDataVersion(self) -> str: ...
    def getZipEntryName(self) -> str: ...

class ModuleMetaData(AbstractMetaData):
    ZIP_ENTRY_NAME: typing.ClassVar[str] = ...
    DATA_VERSION: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, gameModule: VASSAL.build.GameModule): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, zipFile: java.util.zip.ZipFile): ...
    def getLocalizedName(self) -> str: ...
    def getMetaDataVersion(self) -> str: ...
    def getName(self) -> str: ...
    def getZipEntryName(self) -> str: ...
    def read(self, zipFile: java.util.zip.ZipFile) -> None: ...

class SaveMetaData(AbstractMetaData):
    ZIP_ENTRY_NAME: typing.ClassVar[str] = ...
    DATA_VERSION: typing.ClassVar[str] = ...
    PROMPT_LOG_COMMENT: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, zipFile: java.util.zip.ZipFile): ...
    def getMetaDataVersion(self) -> str: ...
    def getModuleData(self) -> ModuleMetaData: ...
    def getModuleName(self) -> str: ...
    def getModuleVersion(self) -> str: ...
    def getZipEntryName(self) -> str: ...
    def read(self, zipFile: java.util.zip.ZipFile) -> None: ...
    @typing.overload
    def save(self, archiveWriter: VASSAL.tools.ArchiveWriter) -> None: ...
    @typing.overload
    def save(self, fileArchive: VASSAL.tools.io.FileArchive) -> None: ...
    @typing.overload
    def save(self, zipWriter: VASSAL.tools.io.ZipWriter) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.build.module.metadata")``.

    AbstractMetaData: typing.Type[AbstractMetaData]
    ExtensionMetaData: typing.Type[ExtensionMetaData]
    ImportMetaData: typing.Type[ImportMetaData]
    MetaDataFactory: typing.Type[MetaDataFactory]
    ModuleMetaData: typing.Type[ModuleMetaData]
    SaveMetaData: typing.Type[SaveMetaData]
