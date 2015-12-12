CAOS is a language designed to ease the prediction of organic chemistry reactions. It is designed
to help chemists (in particular students at the undergraduate level) with the tricky and boring bits
so they can focus on the actual chemistry and labwork.  By providing a simple method of predicting reactions,
with minimal user interaction required, chemists have the ability to simplify and streamline their jobs.

The language is designed to be extremely flexible and extensible.  As an internal DSL (really, more of a library)
in Python it has access to the full host of Python features.  Each mechanism is simply a Python function that has
been registered with the system, and then is located dynamically at runtime.  For example,

```python
@register_mechanism
def acid_base(reactants, conditions):
    ...
```

Additionally, it is possible (and in fact required) to list some pre-conditions of the reaction - this can be
done by passing arguments to the decorator

```python
@register_mechanism(pka_diff('> 10'))
def acid_base(reactants, conditions):
    ...
```

Each of these pre-conditions must be a function - in this case, `pka_diff('> 10')` returns a function that checks
for a pKa difference of at least 10.  Every pre-condition function takes two parameters - a list of reactants,
and a conditions object, and must determine whether or not they meet the requirement.

Users write simple programs by just specifying input molecules and conditions, and then calling the `react`
function on them.  Users can also extend the language using the method described above.

The syntax doesn't help much (as it is just the syntax of a GPL), however it does provide very clear functions
and decorators that can be used by the programmer.  The computational model essentially consists of requirements
validation, and then a variety of graph problems (as all molecules are represented as graphs).  The basic data 
structure is the dispatching class, and the molecule class.  The user can load molecules from files, or can
create them from explicit dictionaries.  There are no custom control structures implemented - simply the ones
that come with Python.  As previously mentioned, the program requires input molecules, and optionally the
reaction conditions.  It will either produce errors if the reaction cannot be completed as specified, or
a list of output molecules and modified reaction conditions.  These errors are normal Python exceptions,
and while they can be caught, by convention they generally shouldn't be except to produce meaningful output of
there not being any result. These are simply printed to stderr.  There isn't really any tooling provided
alongside the language, however a GUI/IDE would be nice at some point.  There aren't really other DSLs,
although there are expensive, somewhat not fantastic applications that I know little about because I 
can't afford them.

Simple reactions can be performed like so:

```python
from CAOS.dispatch import react
from CAOS.structures.molecule import Molecule

acid = Molecule(
    {'a1': 'H', 'a2': 'H', 'a3': 'H', 'a4': 'O'},
    {'b1': {'nodes': ('a1', 'a4'), 'order': 1},
     'b2': {'nodes': ('a2', 'a4'), 'order': 1},
     'b3': {'nodes': ('a3', 'a4'), 'order': 1}
    },
    id='Hydronium'
)

base = Molecule(
    {'a1': 'H', 'a2': 'O'},
    {'b1': {'nodes': ('a1', 'a2'), 'order': 1}},
    id='Hydroxide'
)

conditions = {
    'pkas': {'Hydronium': -1.74, 'Hydroxide': 15.7},
    'pka_points': {'Hydronium': 'a1', 'Hydroxide': 'a2'}
}

products = react([acid, base], conditions)
```

In this case, based on the information in the molecules and the conditions,
the system will predict an acid base reaction that results in the creation of
two water molecules and no salt.

Additionally, user-defined reaction mechanisms can be added to the system.

```python
# aqueous_mechanism.py
from CAOS.dispatch import register_reaction_mechanism

def aqueous(reactants, conditions):
    return conditions.get('aqeuous', False)

@register_reaction_mechanism([aqueous])
def some_mechanism(reactants, conditions):
    # do something
    return products

# reaction.py
import aqueous_mechanism
from CAOS.dispatch import react
from CAOS.structures.molecule import Molecule

m1 = Molecule(...)
m2 = Molecule(...)
conditions = {'aqueous': True}

products = react([m1, m2], conditions)
```

Here the system would use the aqueous mechanism that you have defined,
because the conditions match the aqueous requirement the mechanism was
decorated with.

Python was chosen as a host language because I am very comfortable with the language,
and it is super easy to read and write code in it (i.e. for the speed of implementation
and ease of implementation).  This is an internal DSL because, in particular,
implementing new mechanisms may often require the full capabilities of a GPL in order
to easily implement the mechanism - adding those features to my own external DSL
would be time consuming, and somewhat pointless given that an internal DSL provides
that already.

The first layer has two parts - loading molecules from files using OpenBabel 
(well, technically this doesn't work yet, but can be considered a vital part of
the language and will work eventually), as well as reacting molecules together
using the `react` function - this simply checks the pre-conditions of all known
mechanisms, and attempts all of the ones whose pre-conditions pass.  Then it attempts
to determine which one gave the best result, and returns that result (this is the
middle layer).

In the back layer there are mechanism functions that have been implemented and the
dispatch system that registers them.  These are basically a bunch of decorated
functions, and a class that maintains its own class-level dictionary with all of the 
known functions.  These are added as the mechanisms are decorated.  This can be thought of,
conceptually, as a graph where each node is another tree whose leaves are pre-conditions.
The molecules themselves are graphs, and are treated that way throughout the program.
This is how the mechanisms identify important parts of a molecule and mash them
together.

My language isn't much of a DSL - it is very much on the internal/API/module side
of things.  That being said, it has been designed to be extensible and has 
definitely taken to heart the concept of programming as language design.  Right now
the dispatch system is the crown jewel of the program - it works quite well and
achieves just about all of the goals of the project (there are sometimes some
ordering issues).  I could improve the implementation of the mechanisms and 
requirements functions - they don't really work quite as well as I'd like.  Additionally,
I'd really like if loading molecules from file actually worked. Throughout I've been
using a lot of static analysis and commit-level hooks to keep the quality of my
project, and the documentation, at a high level.  This has helped me keep everything
working and up to date.  I had a lot of difficulty with the actual details of the
chemistry, however this was expected and isn't really the main point of the project.
I really like the current base of the language, and I think it'll lead well into
future work.
