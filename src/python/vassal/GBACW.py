import re

import vassal.manager # we make sure the JVM is started before importing VASSAL classes

from vassal.gamepiece import GamePiece
from vassal.module import get_global_properties_container
from vassal.util import is_named_window, get_all_pieces_with_prototype
from vassal.walker import Walker
from vassal.layer import Layer

from VASSAL.counters import Marker, Decorator
from VASSAL.build.module.properties import GlobalProperty
from VASSAL.build.module.folder import GlobalPropertyFolder

LEADER_NAME = "LeaderName"
LEADER_NAME_KEY = Marker.ID + LEADER_NAME
PROP_NAME_INITIAL_VALUE = "initialValue"
PROP_NAME_DESCRIPTION = "description"
PROP_NAME_NUMERIC = "isNumeric"
PROP_NAME_MIN_VALUE = "min"
PROP_NAME_MAX_VALUE = "max"
PROP_NAME_WRAP = "wrap"


def add_leader_name(leader):
    mark = Marker(LEADER_NAME_KEY, leader)
    leader.getParent().setPiece(mark)
    name = Decorator.getInnermost(leader).getName()
    match = re.match(r'^\w+', str(name))
    prop_name = match.group()
    print(f"Adding Marker LeaderName: {prop_name} to leader: {Decorator.getInnermost(leader).getName()}")
    mark.mySetState(prop_name)


def replace_layer_fix(leader):
    # Change the Layer 'Flip' to 'Replace'
    emb_flip = Layer.find_layer(leader, 'Flip')
    if not emb_flip:
        print(f"Error: leader {Decorator.getInnermost(leader).getName()} has no layer 'Flip'")
        return
    layer_flip = Layer(emb_flip)
    layer_flip.set_name('Replace')
    layer_flip.set_layer()


def get_usa_piece_window(pws):
    return get_piece_window_by_name(pws, 'USA')


def get_csa_piece_window(pws):
    return get_piece_window_by_name(pws, 'CSA')


def get_piece_window_by_name(pws, name):
    window = None
    for p in pws:
        if is_named_window(p, name):
            window = p
    if not window:
        raise Exception(f"No {name} Piece Window")
    return window


def find_leader_name(leader_piece):
    mark = leader_piece.get_trait(Marker().getClass(), LEADER_NAME_KEY)
    return mark.getProperty(LEADER_NAME)


def add_brigade_leader_properties(fat_folder, lvl_folder, eff_folder, leader):
    leader_piece = GamePiece(leader)
    leader_name = find_leader_name(leader_piece)
    fat_prop = make_leader_fatigue_prop(leader_name)
    add_item_to_folder(item=fat_prop, folder=fat_folder)

    eff_prop = make_leader_effective_prop(leader_name)
    add_item_to_folder(item=eff_prop, folder=eff_folder)

    lvl_prop = make_leader_replace_prop(leader_name)
    add_item_to_folder(item=lvl_prop, folder=lvl_folder)


def make_leader_replace_prop(leader_name):
    lvl_prop = GlobalProperty()
    lvl_prop.setConfigureName(f"{leader_name}LeaderLevel")
    lvl_prop.setAttribute(PROP_NAME_DESCRIPTION, f"Track if {leader_name} has been replaced")
    lvl_prop.setAttribute(PROP_NAME_INITIAL_VALUE, "1")
    lvl_prop.setAttribute(PROP_NAME_NUMERIC, True)
    lvl_prop.setAttribute(PROP_NAME_MIN_VALUE, "1")
    lvl_prop.setAttribute(PROP_NAME_MAX_VALUE, "2")
    lvl_prop.setAttribute(PROP_NAME_WRAP, False)
    return lvl_prop


def make_leader_effective_prop(leader_name):
    eff_prop = GlobalProperty()
    eff_prop.setConfigureName(f"{leader_name}EffectiveLevel")
    eff_prop.setAttribute(PROP_NAME_DESCRIPTION, f"Track brigade/division effectiveness level for {leader_name}")
    eff_prop.setAttribute(PROP_NAME_INITIAL_VALUE, "1")
    eff_prop.setAttribute(PROP_NAME_NUMERIC, True)
    eff_prop.setAttribute(PROP_NAME_MIN_VALUE, "1")
    eff_prop.setAttribute(PROP_NAME_MAX_VALUE, "2")
    eff_prop.setAttribute(PROP_NAME_WRAP, False)
    return eff_prop


def make_leader_fatigue_prop(leader_name):
    fat_prop = GlobalProperty()
    fat_prop.setConfigureName(f"{leader_name}FatigueLevel")
    fat_prop.setAttribute(PROP_NAME_DESCRIPTION, f"Track fatigue level for {leader_name}")
    fat_prop.setAttribute(PROP_NAME_INITIAL_VALUE, "1")
    fat_prop.setAttribute(PROP_NAME_NUMERIC, True)
    fat_prop.setAttribute(PROP_NAME_MIN_VALUE, "1")
    fat_prop.setAttribute(PROP_NAME_MAX_VALUE, "7")
    fat_prop.setAttribute(PROP_NAME_WRAP, False)
    return fat_prop


def make_leader_am_prop(leader_name):
    fat_prop = GlobalProperty()
    fat_prop.setConfigureName(f"{leader_name}_Count")
    fat_prop.setAttribute(PROP_NAME_DESCRIPTION, f"Track activations for {leader_name}")
    fat_prop.setAttribute(PROP_NAME_INITIAL_VALUE, "1")
    fat_prop.setAttribute(PROP_NAME_NUMERIC, True)
    fat_prop.setAttribute(PROP_NAME_MIN_VALUE, "1")
    fat_prop.setAttribute(PROP_NAME_MAX_VALUE, "4")
    fat_prop.setAttribute(PROP_NAME_WRAP, False)
    return fat_prop


def add_division_leader_properties(ams_folder, lvl_folder, eff_folder, leader):
    leader_piece = GamePiece(leader)
    leader_name = find_leader_name(leader_piece)
    eff_prop = make_leader_effective_prop(leader_name)
    add_item_to_folder(item=eff_prop, folder=eff_folder)

    lvl_prop = make_leader_replace_prop(leader_name)
    add_item_to_folder(item=lvl_prop, folder=lvl_folder)

    ams_prop = make_leader_am_prop(leader_name)
    add_item_to_folder(item=ams_prop, folder=ams_folder)


def add_commander_properties(lvl_folder, eff_folder, leader):
    leader_piece = GamePiece(leader)
    leader_name = find_leader_name(leader_piece)
    eff_prop = make_leader_effective_prop(leader_name)
    add_item_to_folder(item=eff_prop, folder=eff_folder)

    lvl_prop = make_leader_replace_prop(leader_name)
    add_item_to_folder(item=lvl_prop, folder=lvl_folder)


def do_leader_fixes(leaders, game_module):
    print("Starting Leader Fixes")
    for leader in leaders['all_leaders']:
        print(f"replacing: {Decorator.getInnermost(leader).getName()}")
        replace_layer_fix(leader)
        add_leader_name(leader)

    global_properties = get_global_properties_container(game_module)
    props = create_prop_folders(global_properties)

    for side in ('csa', 'usa'):
        print(f"creating brigade props for side: {side}")
        for leader in leaders[side]['brigade']:
            add_brigade_leader_properties(eff_folder=props[side]['eff'],
                                          fat_folder=props[side]['fat'],
                                          lvl_folder=props[side]['ll'],
                                          leader=leader)
        print(f"creating division props for side: {side}")
        for leader in leaders[side]['division']:
            add_division_leader_properties(eff_folder=props[side]['eff'],
                                           ams_folder=props[side]['ams'],
                                           lvl_folder=props[side]['ll'],
                                           leader=leader)
        print(f"creating commander props for side: {side}")
        for leader in leaders[side]['corps'] + leaders[side]['commander']:
            add_commander_properties(eff_folder=props[side]['eff'],
                                     lvl_folder=props[side]['ll'],
                                     leader=leader)
    print("Finished Leader Fixes")


def get_leaders(name_dict, game_module):
    leaders = {"usa": None, "csa": None}
    usa_leaders = {"brigade": [],
                   "division": [],
                   "corps": [],
                   "commander": [],
                   }
    csa_leaders = {"brigade": [],
                   "division": [],
                   "corps": [],
                   "commander": [],
                   }
    walker = Walker(game_module)
    piece_windows = walker.get_piece_windows()

    usa_piece_window = get_usa_piece_window(piece_windows)
    usa_pieces = walker.get_module_pieces_from_widgets(usa_piece_window)
    csa_piece_window = get_csa_piece_window(piece_windows)
    csa_pieces = walker.get_module_pieces_from_widgets(csa_piece_window)

    csa_names = name_dict['csa']
    usa_names = name_dict['usa']

    csa_commanders = get_all_pieces_with_prototype(csa_pieces, csa_names['commander'])
    usa_commanders = get_all_pieces_with_prototype(usa_pieces, usa_names['commander'])

    csa_corps_commanders = get_all_pieces_with_prototype(csa_pieces, csa_names['corps'])
    usa_corps_commanders = get_all_pieces_with_prototype(usa_pieces, usa_names['corps'])

    csa_div_commanders = get_all_pieces_with_prototype(csa_pieces, csa_names['division'])
    usa_div_commanders = get_all_pieces_with_prototype(usa_pieces, usa_names['division'])

    csa_brigadiers = get_all_pieces_with_prototype(csa_pieces, csa_names['brigade'])
    usa_brigadiers = get_all_pieces_with_prototype(usa_pieces, usa_names['brigade'])

    usa_leaders['brigade'].extend(usa_brigadiers)
    usa_leaders['division'].extend(usa_div_commanders)
    usa_leaders['corps'].extend(usa_corps_commanders)
    usa_leaders['commander'].extend(usa_commanders)

    csa_leaders['brigade'].extend(csa_brigadiers)
    csa_leaders['division'].extend(csa_div_commanders)
    csa_leaders['corps'].extend(csa_corps_commanders)
    csa_leaders['commander'].extend(csa_commanders)

    leaders['usa'] = usa_leaders
    leaders['csa'] = csa_leaders
    leaders['all_leaders'] = csa_commanders + usa_commanders \
                             + csa_div_commanders + usa_div_commanders \
                             + csa_brigadiers + usa_brigadiers

    return leaders


def add_item_to_folder(item, folder):
    item.addTo(folder)
    folder.add(item)


def create_prop_folders(global_properties):
    csa_props = GlobalPropertyFolder()
    csa_props.setAttribute('name', 'CSA')
    add_item_to_folder(item=csa_props, folder=global_properties)

    csa_ams = GlobalPropertyFolder()
    csa_ams.setAttribute('name', 'CSA AM')
    add_item_to_folder(item=csa_ams, folder=csa_props)

    csa_ll = GlobalPropertyFolder()
    csa_ll.setAttribute('name', 'CSA Leader Levels')
    add_item_to_folder(item=csa_ll, folder=csa_props)

    csa_fat = GlobalPropertyFolder()
    csa_fat.setAttribute('name', 'CSA Fatigue Levels')
    add_item_to_folder(item=csa_fat, folder=csa_props)

    csa_eff = GlobalPropertyFolder()
    csa_eff.setAttribute('name', 'CSA Effective Levels')
    add_item_to_folder(item=csa_eff, folder=csa_props)

    usa_props = GlobalPropertyFolder()
    usa_props.setAttribute('name', 'USA')
    add_item_to_folder(item=usa_props, folder=global_properties)

    usa_ams = GlobalPropertyFolder()
    usa_ams.setAttribute('name', 'USA_AMs')
    add_item_to_folder(item=usa_ams, folder=usa_props)

    usa_ll = GlobalPropertyFolder()
    usa_ll.setAttribute('name', 'USA Leader Levels')
    add_item_to_folder(item=usa_ll, folder=usa_props)

    usa_fat = GlobalPropertyFolder()
    usa_fat.setAttribute('name', 'USA Fatigue Levels')
    add_item_to_folder(item=usa_fat, folder=usa_props)

    usa_eff = GlobalPropertyFolder()
    usa_eff.setAttribute('name', 'USA Effective Levels')
    add_item_to_folder(item=usa_eff, folder=usa_props)

    props = {
        'csa': {
            'eff': csa_eff,
            'ams': csa_ams,
            'll': csa_ll,
            'fat': csa_fat,
        },
        'usa': {
            'eff': usa_eff,
            'ams': usa_ams,
            'll': usa_ll,
            'fat': usa_fat,
        },
    }
    return props
