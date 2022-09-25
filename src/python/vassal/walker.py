import vassal.manager # ensure JVM started
from VASSAL.build.widget import PieceSlot
from vassal.gamepiece import GamePiece

from vassal.util import is_piece_widget, is_piece_window


class Walker:
    @staticmethod
    def _print_widget(self, widget):
        space = self._level * '    '
        if is_piece_widget(widget):
            name = widget.getAttributeValueString('name')
            if not name:
                name = widget.getAttributeValueString('entryName')
            print(f"{space}{name}")
            return True
        elif isinstance(widget, PieceSlot):
            print(f"{space}{widget.getName()}")
            return False
        else:
            print(f"Error: {widget.__class__}")
            return False

    def __init__(self, module):
        self._gm = module
        self._level = -1
        self._cb = None
        self.data = None
        self.start = None

    def walk(self, callback, start_widget_or_list=None):
        self._cb = callback
        self._level = -1
        if start_widget_or_list:
            if isinstance(start_widget_or_list, list):
                pws = start_widget_or_list
            elif is_piece_window(start_widget_or_list):
                pws = [start_widget_or_list]
        else:
            pws = self.get_piece_windows()
        for panel in pws:
            if is_piece_window(panel):
                if self._cb(self, panel):
                    self._walk(panel)

    def _walk(self, widget):
        self._level += 1
        buildables = list(widget.getBuildables())
        for b in buildables:
            if self._cb(self, b):
                if is_piece_widget(b):
                    self._walk(b)
        self._level -= 1

    def get_walk_level(self):
        return self._level

    def get_piece_windows(self):
        return list(filter(is_piece_window, self._gm.getBuildables()))

    def print_game_module_pieces(self):
        self.walk(self._print_widget)

    def get_module_pieces_from_widgets(self, start_widget_or_list):
        self.data = []
        self.walk(self._get_pieces, start_widget_or_list)
        return self.data

    def get_all_module_pieces(self):
        return self.get_module_pieces_from_widgets(None)

    # We must track the PieceSlot in case we need to add
    # or delete traits from the GamePiece later
    @staticmethod
    def _get_pieces(self, widget):
        if isinstance(widget, PieceSlot):
            gp = GamePiece(widget)
            self.data.append(gp)
            return False
        elif is_piece_widget(widget):
            return True
