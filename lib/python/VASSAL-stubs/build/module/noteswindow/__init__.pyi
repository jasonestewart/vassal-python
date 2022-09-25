import VASSAL.build.module
import VASSAL.command
import java.awt
import java.text
import java.util
import javax.swing
import typing



class AddSecretNoteCommand(VASSAL.command.Command):
    def __init__(self, interface: typing.Union['AddSecretNoteCommand.Interface', typing.Callable], secretNote: 'SecretNote'): ...
    def getNote(self) -> 'SecretNote': ...
    class Interface:
        def addSecretNote(self, secretNote: 'SecretNote') -> None: ...

class PrivateText:
    def __init__(self, string: str, string2: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getOwner(self) -> str: ...
    def getText(self) -> str: ...
    def hashCode(self) -> int: ...

class SecretNote:
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, boolean: bool, date: java.util.Date, string4: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDate(self) -> java.util.Date: ...
    def getHandle(self) -> str: ...
    def getName(self) -> str: ...
    def getOwner(self) -> str: ...
    def getText(self) -> str: ...
    def hashCode(self) -> int: ...
    def isHidden(self) -> bool: ...

class SetPrivateTextCommand(VASSAL.command.Command):
    def __init__(self, interface: typing.Union['SetPrivateTextCommand.Interface', typing.Callable], privateText: PrivateText): ...
    def getPrivateText(self) -> PrivateText: ...
    class Interface:
        def addPrivateText(self, privateText: PrivateText) -> None: ...

class PrivateNotesController(VASSAL.build.module.GameComponent, VASSAL.command.CommandEncoder, SetPrivateTextCommand.Interface):
    COMMAND_PREFIX: typing.ClassVar[str] = ...
    def __init__(self): ...
    def addPrivateText(self, privateText: PrivateText) -> None: ...
    def captureState(self) -> None: ...
    def decode(self, string: str) -> VASSAL.command.Command: ...
    def encode(self, command: VASSAL.command.Command) -> str: ...
    def getControls(self) -> java.awt.Component: ...
    def getRestoreCommand(self) -> VASSAL.command.Command: ...
    def restoreState(self) -> None: ...
    def save(self) -> VASSAL.command.Command: ...
    def setup(self, boolean: bool) -> None: ...

class SecretNotesController(VASSAL.build.module.GameComponent, VASSAL.command.CommandEncoder, AddSecretNoteCommand.Interface):
    COMMAND_PREFIX: typing.ClassVar[str] = ...
    COL_HANDLE: typing.ClassVar[int] = ...
    COL_DTM: typing.ClassVar[int] = ...
    COL_NAME: typing.ClassVar[int] = ...
    COL_REVEALED: typing.ClassVar[int] = ...
    INTERNAL_DATE_FORMATTER: typing.ClassVar[java.text.DateFormat] = ...
    LOCAL_DATE_FORMATTER: typing.ClassVar[java.text.DateFormat] = ...
    def __init__(self): ...
    def addSecretNote(self, secretNote: SecretNote) -> None: ...
    def captureState(self) -> None: ...
    def decode(self, string: str) -> VASSAL.command.Command: ...
    def encode(self, command: VASSAL.command.Command) -> str: ...
    def getControls(self) -> javax.swing.JComponent: ...
    def getNoteForName(self, string: str) -> SecretNote: ...
    def getRestoreCommand(self) -> VASSAL.command.Command: ...
    def restoreState(self) -> None: ...
    def save(self) -> VASSAL.command.Command: ...
    def setup(self, boolean: bool) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.build.module.noteswindow")``.

    AddSecretNoteCommand: typing.Type[AddSecretNoteCommand]
    PrivateNotesController: typing.Type[PrivateNotesController]
    PrivateText: typing.Type[PrivateText]
    SecretNote: typing.Type[SecretNote]
    SecretNotesController: typing.Type[SecretNotesController]
    SetPrivateTextCommand: typing.Type[SetPrivateTextCommand]
