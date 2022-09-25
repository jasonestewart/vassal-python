import types
import typing

import VASSAL
import java


@typing.overload
def JPackage(__package_name: typing.Literal['VASSAL']) -> VASSAL.__module_protocol__: ...


@typing.overload
def JPackage(__package_name: typing.Literal['java']) -> java.__module_protocol__: ...


def JPackage(__package_name) -> types.ModuleType: ...

