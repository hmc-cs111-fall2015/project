_Anna Pinson_

A minor suggestion, but could the language be set up to handle spaces? It seems that users would naturally add spaces after each comma.
Some of the keywords, like `DontWantToWorkWith`, seem kind of clunky, but users could get used to it.
I believe parsers should be able to match strings with spaces in them; then again, my parser is broken, so I may be completely wrong.

Your first option seems to be your best bet. You can encode in both ways as you build your dictionary, too.
For instance, `"Math"` maps to `1`, and `1` maps to `"Math"`.
Because (presumably) the user is always supplying strings for constraints, then all keys in the dictionary that are strings are guaranteed to be in the "forward" direction, and all keys that are integers are guaranteed to be in the "backward" direciton.
Of course, building two separate dictionaries works just as well.


=======



# Critique: 23 November 2015

Alex Ozdemir

Another solid week - your parser looks pretty good!

## Some more notes on parsing

This may or may not be useful to you, but I found that in the same way you can
set the Scala parser combinators to be whitespace sensitive or insensitive, you
can edit their definition of whitespace. Because my grammar treats newlines as
significant characters I just removed them from the set of whitespace.

If the pypeg2 parser library allows you to do this as well, that could be
useful Alternatively the preprocessor you set up looks great as well!

## Interacting with the Constraint Solver

I think that it is probably worth it to stick with the PyConstraint solver
you've been planning to use. If it only provides good support for integer type
objects, then I think your strategy of mapping all your objects to integers is
fine.

You can probably build a `String -> Int` map and an inverse map at the same
time, and use those to seemlessly convert between the two domains.

Clearly you would have to convert the input to and the output from the solver.
Perhaps you may also have to convert for error messages as well.

## Regarding Syntax

It's great :smile:.

If you're looking for ideas, I know that this is valid:

```
Header:
    GroupSize: 3
    Names: Robin,Jackie,John,Marcus,Evan
    Interests: Math,Chemistry,Biology,Politics,Media_Studies,English,History
    Positions: Leader,Communications,Head_of_Design
```

Could you find a way to make this equivalent:

```
Header:
    GroupSize:
        3
    Names:
        Robin
        Jackie
        John
        Marcus
        Evan
    Interests:
        Math
        Chemistry
        Biology
        Politics
        Media_Studies
        English
        History
    Positions:
        Leader
        Communications
        Head_of_Design
```

A sort of comma / newline equivalence?
