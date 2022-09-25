import argparse
import os
import sys
import re
import jpype
import jpype.imports

from vassal.manager import Manager
from vassal.walker import Walker
from vassal.util import is_piece_widget
import VASSAL.build.widget.PieceSlot
from VASSAL.counters import Marker

my_parser = argparse.ArgumentParser(description='add starting strength decorators to units of a GBACW VASSAL module',
                                    prog='add-starting-strengths',
                                    usage='%(prog)s --modfile file.vmod --ssfile starting-strengths.txt')
my_parser.add_argument('--modfile',
                       action='store',
                       type=str,
                       required=True,
                       help='the path to the module file')
my_parser.add_argument('--ssfile',
                       action='store',
                       type=str,
                       required=True,
                       help='the path to the starting strengths file')
my_parser.add_argument('--buildfile',
                       action='store',
                       type=str,
                       help='write out the buildFile.xml')

args = my_parser.parse_args()
modfile_path = args.modfile
ssfile_path = args.ssfile

if not os.path.isfile(modfile_path):
    print(f'module file: {modfile_path} not found')
    sys.exit(1)

if not os.path.isfile(ssfile_path):
    print(f'starting strengths file: {ssfile_path} not found')
    sys.exit(1)

regex = r'([^:]+):(\d+)'
IMG_NAMES = {}
with open(ssfile_path) as ss_file:
    lines = ss_file.readlines()
    for line in lines:
        match = re.search(regex, line)
        (name, strength) = match.groups()
        IMG_NAMES[name] = strength

print(f'found {len(IMG_NAMES.keys())} pieces in {ssfile_path}')

manager = Manager()
module = manager.open_module(modfile_path)
walker = Walker(module)


def add_starting_strengths(walker, node):
    if is_piece_widget(node):
        return True
    elif isinstance(node, VASSAL.build.widget.PieceSlot):
        add_starting_strength(node)
        return False


def add_starting_strength(node):
    piece = node.getPiece()
    basic = piece.getInnermost(piece)
    img_name = basic.getAllImageNames().first()
    print(f"Piece: {img_name}")
    if img_name in IMG_NAMES:
        ss = IMG_NAMES[img_name]
        print(f"\tFound SS for piece: {img_name}, strength: {ss}")
        try:
            mark = Marker(KEY, piece)
            mark.mySetState(ss)
            node.setPiece(mark)
        except jpype.JException as e:
            print(f"Couldn't create Marker: {str(e)}")
            print(e.stacktrace())


KEY = VASSAL.counters.Marker.ID + "StartingStrength"
walker.walk(add_starting_strengths)

if args.buildfile:
    outfile = "buildFile-tmp.xml"
    build_string = manager.get_build_string(module)
    with open(outfile, 'w') as buildFile:
        buildFile.write(str(build_string))
    print(f"Successfully wrote {outfile}")

print("Writing game module")
manager.save(module)

print("Successfully wrote game module")

exit()
