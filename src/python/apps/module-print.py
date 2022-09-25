import argparse

# noinspection PyUnresolvedReferences
import jpype.imports

from vassal.manager import Manager
from vassal.walker import Walker
# from IPython import embed
my_parser = argparse.ArgumentParser(description='print out pieces of a GBACW VASSAL module',
                                    prog='module-print',
                                    usage='%(prog)s --modfile file.vmod')
my_parser.add_argument('--modfile',
                       action='store',
                       type=str,
                       required=True,
                       help='the path to the module file')
args = my_parser.parse_args()
modfile_path = args.modfile

manager = Manager()
gameModule = manager.open_module(modfile_path)
walker = Walker(gameModule)
walker.print_game_module_pieces()

print("Success!")
exit()
