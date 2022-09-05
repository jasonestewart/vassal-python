import jpype
import jpype.imports

jpype.startJVM(
    classpath=[
        "/Users/jasons/personal-dev/vassal/release-prepare/target/lib/Vengine.jar",
        "classlib/"
        ])

from VASSAL.tools.python import Helper

helper = Helper("0.1")
print(f'Script version: {helper.getPythonVersion()}')
print(f'Java version: {helper.getJavaVersion()}')
print(f'VASSAL version: {helper.getVASSALVersion()}')

print("Opening game module")
gameModule = helper.initGameModule("./test.vmod")
print("Success!")
