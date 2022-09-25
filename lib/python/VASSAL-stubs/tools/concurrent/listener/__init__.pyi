import VASSAL.tools.lang
import java.io
import java.util
import typing



_EventListener__T = typing.TypeVar('_EventListener__T')  # <T>
class EventListener(typing.Generic[_EventListener__T]):
    def receive(self, object: typing.Any, t: _EventListener__T) -> None: ...

_EventListenerSupport__T = typing.TypeVar('_EventListenerSupport__T')  # <T>
class EventListenerSupport(typing.Generic[_EventListenerSupport__T]):
    def addEventListener(self, eventListener: typing.Union[EventListener[_EventListenerSupport__T], typing.Callable[[typing.Any, _EventListenerSupport__T], None]]) -> None: ...
    def getEventListeners(self) -> java.util.List[EventListener[_EventListenerSupport__T]]: ...
    def hasEventListeners(self) -> bool: ...
    def notify(self, t: _EventListenerSupport__T) -> None: ...
    def removeEventListener(self, eventListener: typing.Union[EventListener[_EventListenerSupport__T], typing.Callable[[typing.Any, _EventListenerSupport__T], None]]) -> None: ...

class MultiEventListenerSupport:
    _addEventListener__T = typing.TypeVar('_addEventListener__T')  # <T>
    def addEventListener(self, class_: typing.Type[_addEventListener__T], eventListener: typing.Union[EventListener[_addEventListener__T], typing.Callable[[typing.Any, _addEventListener__T], None]]) -> None: ...
    _getEventListeners__T = typing.TypeVar('_getEventListeners__T')  # <T>
    def getEventListeners(self, class_: typing.Type[_getEventListeners__T]) -> java.util.List[EventListener[_getEventListeners__T]]: ...
    def hasEventListeners(self, class_: typing.Type[typing.Any]) -> bool: ...
    def notify(self, object: typing.Any) -> None: ...
    _removeEventListener__T = typing.TypeVar('_removeEventListener__T')  # <T>
    def removeEventListener(self, class_: typing.Type[_removeEventListener__T], eventListener: typing.Union[EventListener[_removeEventListener__T], typing.Callable[[typing.Any, _removeEventListener__T], None]]) -> None: ...

_DefaultEventListenerSupport__T = typing.TypeVar('_DefaultEventListenerSupport__T')  # <T>
class DefaultEventListenerSupport(EventListenerSupport[_DefaultEventListenerSupport__T], typing.Generic[_DefaultEventListenerSupport__T]):
    def __init__(self, object: typing.Any): ...
    def addEventListener(self, eventListener: typing.Union[EventListener[_DefaultEventListenerSupport__T], typing.Callable[[typing.Any, _DefaultEventListenerSupport__T], None]]) -> None: ...
    def getEventListeners(self) -> java.util.List[EventListener[_DefaultEventListenerSupport__T]]: ...
    def hasEventListeners(self) -> bool: ...
    @typing.overload
    def notify(self) -> None: ...
    @typing.overload
    def notify(self, t: _DefaultEventListenerSupport__T) -> None: ...
    def removeEventListener(self, eventListener: typing.Union[EventListener[_DefaultEventListenerSupport__T], typing.Callable[[typing.Any, _DefaultEventListenerSupport__T], None]]) -> None: ...

class DefaultMultiEventListenerSupport(MultiEventListenerSupport):
    def __init__(self, object: typing.Any): ...
    _addEventListener__T = typing.TypeVar('_addEventListener__T')  # <T>
    def addEventListener(self, class_: typing.Type[_addEventListener__T], eventListener: typing.Union[EventListener[_addEventListener__T], typing.Callable[[typing.Any, _addEventListener__T], None]]) -> None: ...
    _getEventListeners__T = typing.TypeVar('_getEventListeners__T')  # <T>
    def getEventListeners(self, class_: typing.Type[_getEventListeners__T]) -> java.util.List[EventListener[_getEventListeners__T]]: ...
    def hasEventListeners(self, class_: typing.Type[typing.Any]) -> bool: ...
    @typing.overload
    def notify(self) -> None: ...
    @typing.overload
    def notify(self, object: typing.Any) -> None: ...
    _removeEventListener__T = typing.TypeVar('_removeEventListener__T')  # <T>
    def removeEventListener(self, class_: typing.Type[_removeEventListener__T], eventListener: typing.Union[EventListener[_removeEventListener__T], typing.Callable[[typing.Any, _removeEventListener__T], None]]) -> None: ...

_DotPrinter__T = typing.TypeVar('_DotPrinter__T')  # <T>
class DotPrinter(EventListener[_DotPrinter__T], typing.Generic[_DotPrinter__T]):
    def __init__(self, printStream: java.io.PrintStream): ...
    def receive(self, object: typing.Any, t: _DotPrinter__T) -> None: ...

_DummyEventListener__T = typing.TypeVar('_DummyEventListener__T')  # <T>
class DummyEventListener(EventListener[_DummyEventListener__T], typing.Generic[_DummyEventListener__T]):
    def __init__(self): ...
    def receive(self, object: typing.Any, t: _DummyEventListener__T) -> None: ...

_EventAccumulator__T = typing.TypeVar('_EventAccumulator__T')  # <T>
class EventAccumulator(EventListener[_EventAccumulator__T], typing.Generic[_EventAccumulator__T]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[VASSAL.tools.lang.Pair[typing.Any, _EventAccumulator__T]], typing.Sequence[VASSAL.tools.lang.Pair[typing.Any, _EventAccumulator__T]], typing.Set[VASSAL.tools.lang.Pair[typing.Any, _EventAccumulator__T]]]): ...
    def events(self) -> java.util.Collection[VASSAL.tools.lang.Pair[typing.Any, _EventAccumulator__T]]: ...
    def receive(self, object: typing.Any, t: _EventAccumulator__T) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.concurrent.listener")``.

    DefaultEventListenerSupport: typing.Type[DefaultEventListenerSupport]
    DefaultMultiEventListenerSupport: typing.Type[DefaultMultiEventListenerSupport]
    DotPrinter: typing.Type[DotPrinter]
    DummyEventListener: typing.Type[DummyEventListener]
    EventAccumulator: typing.Type[EventAccumulator]
    EventListener: typing.Type[EventListener]
    EventListenerSupport: typing.Type[EventListenerSupport]
    MultiEventListenerSupport: typing.Type[MultiEventListenerSupport]