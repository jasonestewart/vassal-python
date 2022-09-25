import argparse
# noinspection PyUnresolvedReferences
import jpype
# noinspection PyUnresolvedReferences
import jpype.imports

from vassal.manager import Manager
from vassal.walker import Walker
from vassal.GBACW import get_leaders, do_leader_fixes

# from IPython import embed

my_parser = argparse.ArgumentParser(description='modify pieces of a GBACW VASSAL module',
                                    prog='piece-edit',
                                    usage='%(prog)s --modfile file.vmod')
my_parser.add_argument('--modfile',
                       action='store',
                       type=str,
                       required=True,
                       help='the path to the module file')
args = my_parser.parse_args()
modfile_path = args.modfile

manager = Manager()

game_module = manager.open_module(modfile_path)
walker = Walker(game_module)

csa_leaders_names = {"brigade": "Confederate Brigadier",
                     "division": "Confederate Division Commander",
                     "corps": '',
                     "commander": "Confederate Commander",
                     }
usa_leaders_names = {"brigade": "Union Brigadier",
                     "division": "Union Division Commander",
                     "corps": '',
                     "commander": "Union Commander",
                     }
leaders_names = {'csa': csa_leaders_names, 'usa': usa_leaders_names}
leaders = get_leaders(leaders_names, game_module)

pieces = walker.get_all_module_pieces()
print(f'Found {len(pieces)} game pieces in {game_module.getGameName()}')

print(f"Found {len(leaders['all_leaders'])} game pieces in {game_module.getGameName()}")

do_leader_fixes(leaders, game_module)

# embed()

print("Writing game module")
manager.save(game_module)

print("Success!")
exit()
