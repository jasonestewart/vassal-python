from VASSAL.build.module import PieceWindow
from VASSAL.build import Widget
from VASSAL.build.widget import PieceSlot
from VASSAL.build.widget import TabWidget
from VASSAL.build.widget import PanelWidget
from VASSAL.build.widget import ListWidget
from VASSAL.build.widget import BoxWidget
from .util import isPieceWidget, isPieceWindow

class Walker:
    def __init__(self, module):
        self.__game_module__ = module
        self.__indent__ = -1

    def printGameModulePieces(self):
        pws = list(filter(isPieceWindow, self.__game_module__.getBuildables()))
        for panel in pws:
            self.__indent__ = -1
            self.printPieces(panel)


    def printPieces(self, pw):
        self.__indent__ += 1
        space = self.__indent__ * '    '
        name = pw.getAttributeValueString('name')
        if not name:
            pw.getAttributeValueString('entryName')
        print(f"{space}{name}")

        buildables = list(pw.getBuildables())
        for b in buildables:
            if isinstance(b, PieceSlot):
                print(f"{space}{b.getPiece().getName()}")
            elif isPieceWidget(b):
                self.printPieces(b)
            else:
                print(f"Error: {b.__class__}")

        self.__indent__ -= 1


    def getPieces(self, pw):
        pieces = []
        if isinstance(pw, PieceSlot):
            pieces.append(pw.getPiece().getName())
        else:
            buildables = list(pw.getBuildables())
            for b in buildables:
                if isPieceWidget(b):
                    pieces.extend(self.getPieces(b))

        return pieces
