# Project description and plan

## Motivation
_Why is this project useful or interesting, what problem are you trying to address, and why is a DSL an appropriate solution?_

CAOS is a language designed to assist (primarly student) organic chemists.
It will do so by allowing the simple representation of molecules, as well 
as loading various common existing representations of molecules, and by 
lastly making accurate predictions about how, and why, two (or more) 
molecules will react.

This is currently a rather tedious operation for most chemists - it must be 
done by hand or by using expensive (and limited) commercial software.  Lastly,
most of these solutions are aimed at researchers and professional chemists, 
not students (and certainly not undergraduate students).  By developing a free,
open source alternative, the more technically minded (and hopefully all) budding
chemists will have an invaluable tool at their disposal.

The language of chemical formulas and reactions is already essentially a DSL - 
this would just provide the computational ability to actually run and test a
reaction.  Ideally the program would not look substantially different from a
reaction on paper - write the things that are reacting, the conditions under
which they are reacting, and then the result.

## Language domain

The domain is that of organic chemistry reactions.  This is a vital domain for
much of chemistry (as it turns out, we're all just sacks of organic molecules
so the study of these molecules is of vital importance).  Chemists, especially
learning chemists, will benefit.  There are some existing languages, including
the one I've been working on [here](https://github.com/Dannnno/Chemistry).

There are some other ones too, that I learned about asking 
[this question](http://chemistry.stackexchange.com/questions/7765/program-that-simulates-basic-reactions-in-organic-chemistry)
on the Chemistry Stack Exchange.  I know little about them; they are of varying
usefulness and popularity, and many are only available via paying or having
actual scientific credentials:

- [WODCA from the Gasteiger group](http://www2.chemie.uni-erlangen.de/software/wodca/index.html)
- [CHIRON from the Hanessian group](http://osiris.corg.umontreal.ca/chiron.shtml)
- [LHASA from the Corey group](http://cheminf.cmbi.ru.nl/cheminf/lhasa/)
- [SYLVIA](https://www.molecular-networks.com/products/sylvia)
- [ArChem - also called Route Designer](http://www.simbiosys.ca/archem/)
- [Chematica](https://en.wikipedia.org/wiki/Chematica)
- [Some guy's pet project](http://www.dimuthu.org/blog/2008/11/22/organic-chemistry-reaction-simulator/)

None of them appear to have widespread use or support, and have varying levels
of functionality.  I like that people have tried things, but honestly I don't really
like any of them. I don't plan on borrowing much from them - I'd like to approach
this from a clean slate.

## Language design

Closely mirror the actual process of writing a reaction out by hand.  A program will
be a normal Python program.  When it runs it will search through a tree of potential 
reaction mechanisms and apply a (partial) order to them and attempt to find the best
possibility of success.  It can take many kinds of output (those supported by [OpenBabel](http://openbabel.org/docs/2.3.0/FileFormats/Overview.html)) and return
a data structure that I have implemented.  This data structure will be easy to convert
into any of those same formats, as well as decently readable on its own.

Things that could go wrong are impossible molecules or conditions, or invalid reaction
mechanisms.  In these cases a fatal exception (one that is uncatchable by convention)
should be thrown explaining what error occurred, and why - this exception should be
thrown as soon as possible.  Other than that the normal Python syntax and runtime rules
should apply.

## Example computations

This is the canonical example of an acid-base reaction:

HCl + NaOH → NaCl + H2O

```python
from CAOS import react, load_molecule_from_file

hydrochloric_acid = load_molecule_from_file('HCl.cml')
sodium_hydroxide = load_molecule_from_file('NaOH.cml')
products = react([hydrochloric_acid, sodium_hydroxide], conditions=None)
print products
# ["Sodium Chloride", "Water"]
```

It is also possible to add your own data structures and reactions and run
reactions using them.

```python
# dielsAlder.py
from CAOS.dispatch import register_reaction_mechanism, register_data_type
from CAOS.reaction.preconditions import nucleophile, heat, light

@register_reaction_mechanism(
    "Diels-Alder",
    heat("x > 500K"),
    light("x > 30"),
    nucleophile)
def diels_alder_mechanism(reactants, conditions):
    ...
    
@register_data_type
class DielsAlderType(object):

    @classmethod
    def from_default(cls, molecule):
        return DielsAlderType(molecule.atoms, molecule.bonds, molecule.other_data)
        
    def __init__(self, atoms, bonds, other_data):
        ...

# myreaction.py
import dielsAlder
from CAOS import react, load_molecule_from_file

r1 = load_molecule_from_file('filename1.cml')
r2 = load_molecule_from_file('filename2.cml')

# Because of the reactants and the conditions it will try the Diels-Alder Reaction
products = react([r1, r2], conditions={'light': 55, 'heat': "30C"})
products.show()
# It will fail though, and give no result
# [None]

r3 = load_molecule_from_file('filename3.cml')
products = react([r1, r3], conditions={'light': 100, 'heat':"700K"})
products.show()
# [product_name]
```
