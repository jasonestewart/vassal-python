import jpype
import jpype.imports

jpype.startJVM(
    classpath=[
        "../vassal/release-prepare/target/lib/Vengine.jar",
        "classlib/"
    ])
from vassal.util import isPieceWidget, isPieceWindow

from VASSAL.tools.python import Helper
from VASSAL.build.module import PieceWindow
from VASSAL.build.widget import PieceSlot

# from IPython import embed

def printPieces(pw, indent):
    space = indent * '    '
    name = pw.getAttributeValueString('name')
    if not name:
        pw.getAttributeValueString('entryName')
    print(f"{space}{name}")

    buildables = list(pw.getBuildables())
    for b in buildables:
        if isinstance(b, PieceSlot):
            print(f"{space}{b.getPiece().getName()}")
        elif isPieceWidget(b):
            printPieces(b, indent + 1)
        else:
            print(f"Error: {b.__class__}")


def getPieces(pw):
    pieces = []
    if isinstance(pw, PieceSlot):
        print("Found piece slot")
        pieces.append(pw.getPiece().getName())
    else:
        buildables = list(pw.getBuildables())
        for b in buildables:
            if isPieceWidget(b):
                pieces.extend(getPieces(b))

    return pieces


helper = Helper("0.1")
print(f'Script version: {helper.getPythonVersion()}')
print(f'Java version: {helper.getJavaVersion()}')
print(f'VASSAL version: {helper.getVASSALVersion()}')

print("Opening game module")
gameModule = helper.initGameModule("./test.vmod")

pws = list(filter(isPieceWindow, gameModule.getBuildables()))
print(f'{pws}')

for panel in pws:
    printPieces(panel, 0)

print("Success!")
exit()
