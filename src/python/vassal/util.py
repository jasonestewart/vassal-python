import vassal.manager # we make sure the JVM is started before importing VASSAL classes

from VASSAL.build.module import PieceWindow
from VASSAL.build.widget import TabWidget, PanelWidget, ListWidget, BoxWidget
from VASSAL.counters import GamePiece



def is_piece_window(pw):
    return isinstance(pw, PieceWindow)


def is_named_window(piece_window, name):
    if not is_piece_window(piece_window):
        return False
    window_name = piece_window.getAttributeValueString('name')
    return name == window_name


def is_piece_widget(pw):
    return isinstance(pw, (
        PieceWindow,
        TabWidget,
        ListWidget,
        PanelWidget,
        BoxWidget)
                      )


def piece_has_prototype(piece, prototype_str):
    if not isinstance(piece, GamePiece):
        return False

    has_prototype = False
    manager = Manager()
    prototype = manager.get_prototype(piece)
    while prototype:
        if prototype.getPrototypeName() == prototype_str:
            has_prototype = True
            break
        prototype = manager.get_prototype(prototype.getInner())
    return has_prototype


def get_all_pieces_with_prototype(pieces, prototype_str):
    found = []
    if prototype_str:
        for piece in pieces:
            if piece_has_prototype(piece, prototype_str):
                found.append(piece)
    return found
