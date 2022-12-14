import VASSAL.build
import typing



class DeckSubFolder(VASSAL.build.AbstractFolder):
    def __init__(self): ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...

class GlobalPropertyFolder(VASSAL.build.AbstractFolder):
    def __init__(self): ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...

class MapSubFolder(VASSAL.build.AbstractFolder):
    def __init__(self): ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...

class ModuleSubFolder(VASSAL.build.AbstractFolder):
    def __init__(self): ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...

class PrototypeFolder(VASSAL.build.AbstractFolder):
    def __init__(self): ...
    def add(self, buildable: VASSAL.build.Buildable) -> None: ...
    def getAllowableConfigureComponents(self) -> typing.List[typing.Type[typing.Any]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.build.module.folder")``.

    DeckSubFolder: typing.Type[DeckSubFolder]
    GlobalPropertyFolder: typing.Type[GlobalPropertyFolder]
    MapSubFolder: typing.Type[MapSubFolder]
    ModuleSubFolder: typing.Type[ModuleSubFolder]
    PrototypeFolder: typing.Type[PrototypeFolder]
