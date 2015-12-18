_Critiquer: Matt Valentine_

_A day late_

## Logging

Concerning the `log` function, I am not sure why you'd need to go so
far as injecting it into the function's global scope.
You probably just want to have people import and use the same function
"log".

If you to automagically figure out _which_ reaction is doing the logging,
the best thing to do would be to set a global variable before you
actually call the reaction. Alternatively, you can use `inspect.stack`.

Admittedly though, the decorator + modifying func_globals, if it works
out, is plenty fine in my book. It's terrible, which is wonderful.

## Requirements and Mechanisms

I think your implementation of requirements and mechanisms, from a high-level,
is straightforward and understandable. A minor nitpick is that perhaps

    @register_reaction_mechanism(aqueous, blah, ...)

would be preferred to

    @register_reaction_mechanism([aqueous, blah, ...])

but, basically, whatever works.

After looking at your example code for the acid-base reaction for quite
some time, it seems to me that the hardest things the user is made
to do to interact with molecule objects. So:

## Molecules

### Creation

Obviously, constructing the molecules is not a joy. But, to be fair, I don't think
anybody has a very good solution for that particular problem. Of course, there might 
be slightly more convenient constructors:

    Hydronium = molecule(
        atoms = [H, H, H, O],
        bonds = [
          single(0, 4),
          single(1, 4),
          single(2, 4),
          single(3, 4)
        ]
    )

but really I bet the real solution is "read from file", like you've mentioned.

### IDs / Labels

Ideally, the user should be spared the details of how your labelling
system works, at least unless they want to dive into it.
Even better would be if the user were able to believe they were manipulating
"atoms" directly - even if in reality, what they're shuttling about
are actually labels.

_Add/Remove:_ For example, removing a node should probably return the type of atom that
used to be there. And adding a node should not take in an id (by default anyways),
since it can figure that out on its own. But it should _return_ the id that it selects,
so you can add an atom and then continue to do things like add bonds to it.


_Numbering:_ There's an unstated requirement that all atom id's be of the form
'a#' and all bond ids be of the form 'b#'. The only advantage this seems
to get you over NetworkX's idea of just letting anything be a label is
that you can find a "next open id". But that really only requires that
you limit yourself to integers as labels.

In fact, it doesn't even require that. Because if you add all kinds of
labels, not just integers, into `invalid_nums`, you can still loop through
`range(len(invalid_nums))` and find a number not being used as a label.
So, really, it just means that your _default_ labels are numbers,
but in general you _could_ be free to use anything as a label.

### Data

It interests me that you decided to store information like PKa in the conditions, rather than
having molecules themselves contain arbitrary data like that directly on themselves.

### Database / Molecule Identification

I imagine you've intended to do this from the beginning but, since you have access to NetworkX and graph isomorphism 
and all, it would be terribly slow and
such but, technically if you had a database of molecules, and an unidentified one, you could
search your database to see if you could identify it.
Not that you really need to add this.
