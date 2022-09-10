from VASSAL.build.module import PieceWindow
from VASSAL.build import Widget
from VASSAL.build.widget import PieceSlot
from VASSAL.build.widget import TabWidget
from VASSAL.build.widget import PanelWidget
from VASSAL.build.widget import ListWidget
from VASSAL.build.widget import BoxWidget
from .util import isPieceWidget, isPieceWindow


class Walker:
    @staticmethod
    def _print_widget(self, widget):
        space = self._level * '    '
        if isPieceWidget(widget):
            name = widget.getAttributeValueString('name')
            if not name:
                name = widget.getAttributeValueString('entryName')
            print(f"{space}{name}")
            return True
        elif isinstance(widget, PieceSlot):
            print(f"{space}{widget.getPiece().getName()}")
            return False
        else:
            print(f"Error: {widget.__class__}")
            return False

    def __init__(self, module):
        self._gm = module
        self._level = -1
        self._cb = None
        self.data = None

    def walk(self, callback):
        self._cb = callback
        self._level = -1
        pws = self.get_piece_windows()
        for panel in pws:
            if self._cb(self, panel):
                self._walk(panel)

    def _walk(self, widget):
        self._level += 1
        buildables = list(widget.getBuildables())
        for b in buildables:
            if self._cb(self, b):
                if isPieceWidget(b):
                    self._walk(b)
        self._level -= 1

    def get_walk_level(self):
        return self._level

    def get_piece_windows(self):
        return list(filter(isPieceWindow, self._gm.getBuildables()))

    def print_game_module_pieces(self):
        self.walk(self._print_widget)

    def get_all_module_pieces(self):
        self.data = []
        self.walk(self._get_pieces)
        return self.data

    @staticmethod
    def _get_pieces(self, widget):
        if isinstance(widget, PieceSlot):
            self.data.append(widget.getPiece())
            return False
        elif isPieceWidget(widget):
            return True


