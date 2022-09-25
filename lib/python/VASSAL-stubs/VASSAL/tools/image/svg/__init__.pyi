import java.awt
import java.awt.geom
import java.awt.image
import java.io
import java.net
import java.util
import org.apache.batik.transcoder
import org.w3c.dom.svg
import typing



class SVGImageUtils:
    @staticmethod
    def getDocument(string: str, inputStream: java.io.InputStream) -> org.w3c.dom.svg.SVGDocument: ...
    @staticmethod
    def getExternalReferences(string: str) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getImageSize(inputStream: java.io.InputStream) -> java.awt.Dimension: ...
    @typing.overload
    @staticmethod
    def getImageSize(string: str, inputStream: java.io.InputStream) -> java.awt.Dimension: ...
    @typing.overload
    @staticmethod
    def getImageSize(sVGDocument: org.w3c.dom.svg.SVGDocument) -> java.awt.Dimension: ...
    @staticmethod
    def relativizeExternalReferences(string: str) -> typing.List[int]: ...

class SVGRenderer:
    KEY_BACKGROUND_COLOR: typing.ClassVar[org.apache.batik.transcoder.TranscodingHints.Key] = ...
    KEY_FORCE_TRANSPARENT_WHITE: typing.ClassVar[org.apache.batik.transcoder.TranscodingHints.Key] = ...
    @typing.overload
    def __init__(self, string: str, inputStream: java.io.InputStream): ...
    @typing.overload
    def __init__(self, uRL: java.net.URL, inputStream: java.io.InputStream): ...
    @typing.overload
    def render(self) -> java.awt.image.BufferedImage: ...
    @typing.overload
    def render(self, double: float, double2: float) -> java.awt.image.BufferedImage: ...
    @typing.overload
    def render(self, double: float, double2: float, rectangle2D: java.awt.geom.Rectangle2D) -> java.awt.image.BufferedImage: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.image.svg")``.

    SVGImageUtils: typing.Type[SVGImageUtils]
    SVGRenderer: typing.Type[SVGRenderer]
