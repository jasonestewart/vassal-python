# VASSAL Python
## Tools for manipulating VASSAL module files using python. 
This python module is aimed at developers of VASSAL game modules. It's purpose to automate repetive module upgrades (e.g. adding or removing a new trait to all pieces of a certain type based on some number printed on the piece's physical counter).

Implemented using jpype

The successor to VASSAL::Perl

# Core Components

The package implements the following modules for working with VASSAL game modules. These are the essential packages most useful to developers. 

## Manager

The class that wraps a headless version of the VASSAL so that it is possible to call all the module loading, parsing, and saving features without a Swing GUI. It is important to know that it is manager.py that actually calls jpype.startJVM() - so modules need to make sure they import Manager *before* importing any VASSAL java modules - or they will get a runtime error.

```python
from vassal.manager import Manager

manager = Manager()
gameModule = manager.open_module("./test.vmod")

# change some stuff...

manager.save(gameModule)
print("Success!!")
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

# Helper modules
These modules are included to automate certain tasks and to hide some of the Java-ism of the VASSAL code structure.

## Util
This includes helper methods that are useful for grabbing pieces from piece windows in your module. Arguably, most are too low-level and will be moved into Walker or other module in the future.
```python
from vassal.util import is_piece_widget, is_piece_window, is_named_window, piece_has_prototype, get_all_pieces_with_prototype
from vassal.walker import Walker
from vassal.manager import Manager

manager = Manager()
game_module = manager.open_module("test.vmod")
walker = Walker(game_module)
pws = walker.get_piece_windows()
pieces = walker.get_all_module_pieces()

leaders = []
for p in pieces:
    if piece_has_prototype(p, "Leader"):
        leaders.append(p)
        
jackson_pw = None
for pw in pws:
    if is_named_window(pw, "Jackson Division")
        usa_pw = pw
        break
jackson_pieces = walker.get_all_module_pieces(jackson_pw)

csa_arty = get_all_pieces_with_prototype(pieces, "CSA Artillery")        

# These two are *pretty* low level and probably not generally useful
if is_piece_window(jackson_pw):
    print("Found!")

pieces = []
if is_piece_widget(jackson_pw):
    pieces.append(list(walker.get_all_module_pieces(pw))) 

```

## GBACW
This module is specific to the GBACW (Great Battles of the American Civil War) series of modules. It might serve as an example for other module authors.

Some examples:
```python
from vassal.GBACW import get_piece_window_by_name
from vassal.walker import Walker
from vassal.manager import Manager

manager = Manager()
game_module = manager.open_module("test.vmod")
walker = Walker(game_module)
pws = walker.get_piece_windows()
usa_inf = get_piece_window_by_name(pws, "USA Infantry")
usa_cav = get_piece_window_by_name(pws, "USA Cavalry")
```

## Loading the JVM

Jpype needs the JVM started before it can begin loading the Java classes. This is handled inside manager.py during the module loading. The JVM needs to find both ```Vengine.jar``` and ```Helper.class``` in the classpath. One easy way to do that is to configure the classpath using jpype.addClassPath before loading manager.py. 

```python
import jpype
import jpype.imports

jpype.addClassPath("./lib/java/Vengine.jar")
jpype.addClassPath("lib/java")  # Helper.class
from vassal.manager import Manager

```
Another method is to set the CLASSPATH environment variable before invoking application:

```shell
export CLASSPATH="$CLASSPATH:${VASSALPYTHON_HOME}/lib/java/Vengine.jar"
export CLASSPATH="$CLASSPATH:${VASSALPYTHON_HOME}/lib/java 
python ${VASSALPYTHON_HOME}/app/module-print.py --mod ${VASSALPYTHON_HOME}/tmp/test.vmod
```

# Example Applications
The package includes a few example tools created using this package. They illustrate how to interact with the VASSAL GameModule and it's data from 

## image-scrape.py
Interactively scrape numbers from counter images and save it in a .csv file 
The image scraper will ask for confirmation if it doesn't have sufficient confidence in the guess. It will pop up an image window showing what it scraped and what it's best guess of the number is. Click on the image window and hit `enter` to make it go away and then back in the shell window, hit `enter` to use the default value or type in a new value and hit `enter` to continue. 

```shell
$ python3 image-scrape.py --image-dir ./images --names-file names.txt --ss-file start-str.txt
Reading image: 14IN_front.png
Found strength: 9

Reading image: 14INa_front.png
Found strength: 5

Reading image: 14INb_front.png
Found strength: 4

Reading image: 8OH_front.png
Found strength: 14

Reading image: 8OHa_front.png
ss_10: 7, ss_8: NONE>> 7
...[SNIP: interactively prompts user for confirmation]
enter correct strength: >> 7: 
Found strength: 7
...[SNIP: more output]
Success!
```


## add-starting-strengths.py
Compares the name of each piece in the module to the names in the .csv file from image-scrape, and if found, creates a new "StartingStrength" trait on the piece and sets the value to that listed in the file
```shell
$ python3 add-starting-strengths.py --mod file.vmod --ssfile starting-strengths.txt
VASSAL: initGameModule: start
[SNIP: vassal-pyton startup messages]
VASSAL: initGameModule: end
Piece: 34MA_8_front.png
	Found SS for piece: 34MA_8_front.png, strength: 8
Piece: 5NY_HA_12_front.png
	Found SS for piece: 5NY_HA_12_front.png, strength: 12
Piece: 116OH_10_front.png
	Found SS for piece: 116OH_10_front.png, strength: 10
Piece: 123OH_10_front.png
	Found SS for piece: 123OH_10_front.png, strength: 10
Piece: 170OH_front.png
	Found SS for piece: 170OH_front.png, strength: 8
Piece: Ely_front.png
Piece: 1WV_2_1_AWV_front.png
	Found SS for piece: 1WV_2_1_AWV_front.png, strength: 8
Piece: 4WV_front.png
	Found SS for piece: 4WV_front.png, strength: 8
Piece: 12WV_2_1_AWV_front.png
	Found SS for piece: 12WV_2_1_AWV_front.png, strength: 8
Piece: 18CT_2_1_AWV_front.png
	Found SS for piece: 18CT_2_1_AWV_front.png, strength: 8
Piece: 2MD_ES_front.png
	Found SS for piece: 2MD_ES_front.png, strength: 8
Piece: Young's_PB_front.png
	Found SS for piece: Young's_PB_front.png, strength: 8
[SNIP: more output]
Success!
```
## module-print.py
Recursively prints the names of all the piece windows and the pieces in each window
```shell
$ python3 module-print.pl --mod test.vmod
VASSAL: initGameModule: start
... [SNIP: vassal-pyton startup messages]
VASSAL: initGameModule: end
USA
Union Army of West Virginia
    Commander
        Crook, AWV
    Thoburn's Division, 1/AWV
        Thoburn's Division, 1/AWV
            Thoburn 1/AWV
            1/AWV Brigades
                Wells, 1/1/AWV
                    Wells 1/1/AWV
                    Wells Rgmt 1
                    Wells Rgmt 2
                    Wells Rgmt 3
                    Wells Rgmt 4
                    Wells Rgmt 5
                Ely, 2/1/AWV
[SNIP: more output]
Success!
```
## piece-edit.py - (GBACW-specific)
Uses the GBACW module included in this package to find game pieces based on prototype. For example, find all "Leaders" on the side "USA" and create four new global properties using that leader's name as the basis for the property name.

# Known Problems
Here is a list of things I already know are not working as planned.

## Applications hang on exit
Currently, VASSAL does not close all it's running threads on System.exit() - so python apps will be left hanging after they have completed. (Probably something in how Helper.class needs to fake Swing into thinking it's not running headless when it really is. Probably, VASSAL is trying to pop-up a dialog asking if we want to save.)

They need to be killed to force a shutdown:
```shell
$ python3 module-print.pl --mod test.vmod
... some output
Success!!
(hangs)
^Z
[1]+  Stopped                 python app/module-print.py --mod test.vmod
$ kill %1
[1]+  Exit 143                python app/module-print.py --mod test.vmod
$
```

Not graceful, but hey! It works...

I will check to see if it is possible to set a flag so VASSAL doesn't ask for a save.
