import jpype
import jpype.imports

jpype.addClassPath("../vassal/release-prepare/target/lib/Vengine.jar")
jpype.addClassPath("classlib/")
from vassal.manager import Manager
from vassal.walker import Walker
# from IPython import embed

manager = Manager()
gameModule = manager.open_module("./test.vmod")
walker = Walker(gameModule)
walker.printGameModulePieces()

print("Success!")
exit()
