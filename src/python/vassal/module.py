import vassal.manager # we make sure the JVM is started before importing VASSAL classes

from VASSAL.build.module.properties import GlobalProperties

GP_CLASS = GlobalProperties().getClass()


def get_global_properties_container(game_module):
    for b in game_module.getBuildables():
        if b.getClass() == GP_CLASS:
            return b
