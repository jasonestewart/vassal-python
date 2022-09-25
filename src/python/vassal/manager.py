from typing import Final
import jpype
import jpype.imports
from jpype import JImplements, JOverride

jpype.startJVM()
from VASSAL.tools.python import Helper
from VASSAL.build import GameModule
from java.lang import Runtime, Thread, Runnable


class Manager:
    VERSION: Final = "0.2"
    _instance: Helper = None

    def __init__(self):
        if self._instance is None:
            self._instance = Helper(Manager.VERSION)

    def print_versions(self):
        print(f'Script version: {self._instance.getPythonVersion()}')
        print(f'Java version: {self._instance.getJavaVersion()}')
        print(f'VASSAL version: {self._instance.getVASSALVersion()}')

    def open_module(self, module_filename: str):
        '''
        :param module_filename: the path to the module to be opened
        :type module_filename: str
        :return: the module
        :rtype: GameModule
        '''
        return self._instance.initGameModule(module_filename)

    def get_build_string(self, module: GameModule):
        '''
        :param module: the module from which to get the buildString
        :type module: GameModule
        :return: the buildString xml
        :rtype: str
        '''
        return self._instance.getBuildString(module)

    def save(self, module) -> None:
        '''
        :param module: module to save
        :type module: GameModule
        '''
        self._instance.saveGameModule(module)

    def get_prototype(self, piece):
        return self._instance.getPrototype(piece)

    @staticmethod
    def shutdown() -> None:
        print(f"Manager: Shutting Down")
        # Runtime.getRuntime().halt(0);
        Helper.shutdown()