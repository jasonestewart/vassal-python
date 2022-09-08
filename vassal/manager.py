import jpype
import jpype.imports

jpype.startJVM()
from VASSAL.tools.python import Helper

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
