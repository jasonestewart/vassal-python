# VASSAL Python
Tools for manipulating VASSAL module files using python

Implemented using jpype

The successor to VASSAL::Perl

# Components

The package implements the following modules for working with VASSAL game modules

## Manager

The class that wraps a headless version of the VASSAL so that it is possible to call all the module loading, parsing, and saving features without a Swing GUI.

```python
from vassal.manager import Manager

manager = Manager()
gameModule = manager.open_module("./test.vmod")
```

## Walker

The class that enables recursive descent into the Buildables hierarchy of a game module and enables printing or actions on pieces and components.

```python
from vassal.manager import Manager
from vassal.walker import Walker

manager = Manager()
gameModule = manager.open_module("./test.vmod")
walker = Walker(gameModule)
walker.print_game_module_pieces()
```

## Loading the JVM

Jpype needs the JVM started before it can begin loading the Java classes. This is handled inside manager.py during the module loading. The JVM needs to find both ```Vengine.jar``` and ```Helper.class``` in the classpath. One easy way to do that is to set the classpath using jpype before loading manager.py

```python
import jpype
import jpype.imports

jpype.addClassPath("./lib/Vengine.jar")
jpype.addClassPath("classlib/") # Helper.class
from vassal.manager import Manager

```

## Example Applications
* module-print.py: recursively prints the names of all the piece windows and the pieces in each window
* add-starting-strengths.py: compares the name of each piece in the module to a predefined list of piece names, and if found, creates a new "StartingStrength" trait on the piece and sets the value to that listed in the file