import VASSAL.build.module.PieceWindow
import VASSAL.build.Widget
import VASSAL.build.widget.PieceSlot
import VASSAL.build.widget.TabWidget
import VASSAL.build.widget.PanelWidget
import VASSAL.build.widget.ListWidget
import VASSAL.build.widget.BoxWidget

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
