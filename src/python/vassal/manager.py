import jpype
import jpype.imports
from jpype import JImplements, JOverride

jpype.startJVM()
from VASSAL.tools.python import Helper
from java.lang import Runtime, Thread, Runnable


class Manager:
    VERSION = "0.2"
    _instance = None

    def __init__(self):
        if self._instance is None:
            self._instance = Helper(Manager.VERSION)

    def print_versions(self):
        print(f'Script version: {self._instance.getPythonVersion()}')
        print(f'Java version: {self._instance.getJavaVersion()}')
        print(f'VASSAL version: {self._instance.getVASSALVersion()}')

    def open_module(self, module_filename):
        return self._instance.initGameModule(module_filename)

    def get_build_string(self, module):
        return self._instance.getBuildString(module)

    def save(self, module):
        return self._instance.saveGameModule(module)

    def get_prototype(self, piece):
        return self._instance.getPrototype(piece)

    def shutdown(self):
        self._instance.shutdown()


@JImplements(Runnable)
class MyShutdownHook:
    @JOverride
    def run(self):
        Manager().shutdown()


# Runtime.getRuntime().addShutdownHook(Thread(MyShutdownHook()))
