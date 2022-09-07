import jpype
import jpype.imports

jpype.startJVM(
    classpath=[
        "../vassal/release-prepare/target/lib/Vengine.jar",
        "classlib/"
        ])

import VASSAL.tools.python.Helper
import VASSAL.build.module.PieceWindow
import VASSAL.build.widget.PieceSlot
import VASSAL.build.Widget
import VASSAL.build.widget.TabWidget
import VASSAL.build.widget.PanelWidget
import VASSAL.build.widget.ListWidget
import VASSAL.build.widget.BoxWidget
from IPython import embed

def printPieces(pw, indent):
    space = indent * '    '
    name = pw.getAttributeValueString('name')
    if not name:
        pw.getAttributeValueString('entryName')
    print(f"{space}{name}")

    buildables = list(pw.getBuildables())
    for b in buildables:
        if isinstance(b, VASSAL.build.widget.PieceSlot):
            print(f"{space}{b.getPiece().getName()}")
        elif isPieceWidget(b):
            printPieces(b,indent+1)
        else:
            print(f"Error: {b.__class__}")


def getPieces(pw):
    pieces = []
    if isinstance(pw, VASSAL.build.widget.PieceSlot):
        print("Found piece slot")
        pieces.append(pw.getPiece().getName())
    else:
        buildables = list(pw.getBuildables())
        for b in buildables:
            if isPieceWidget(b):
                pieces.extend(getPieces(b))

    return pieces

def isPieceWindow(pw):
    return isinstance(pw, VASSAL.build.module.PieceWindow)

def isPieceWidget(pw):
    return isinstance(pw, (
        VASSAL.build.module.PieceWindow,
        VASSAL.build.widget.TabWidget,
        VASSAL.build.widget.ListWidget,
        VASSAL.build.widget.PieceSlot,
        VASSAL.build.widget.PanelWidget,
        VASSAL.build.widget.BoxWidget)
    )


helper = VASSAL.tools.python.Helper("0.1")
print(f'Script version: {helper.getPythonVersion()}')
print(f'Java version: {helper.getJavaVersion()}')
print(f'VASSAL version: {helper.getVASSALVersion()}')

print("Opening game module")
gameModule = helper.initGameModule("./test.vmod")

pws = list(filter(isPieceWindow, gameModule.getBuildables()))
print(f'{pws}')

for panel in pws:
    printPieces(panel,0)

print("Success!")
