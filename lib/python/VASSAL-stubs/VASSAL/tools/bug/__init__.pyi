import java.lang
import typing



class BugHandler:
    def accept(self, throwable: java.lang.Throwable) -> bool: ...
    def handle(self, throwable: java.lang.Throwable) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.bug")``.

    BugHandler: typing.Type[BugHandler]
