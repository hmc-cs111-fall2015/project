## Diagnostic Information
### Syntax
It seems weird to have to say `myfunction.logger.log` when you're already in
the `myfunction` function. It would be really nice if you could just say `log`
or `info`. This also makes it nicer for helper functions to log things. If you
had this:
```
def is_blue(r,c):
    if (c == 'the ocean'):
        log("We're in the ocean, everything is blue")
        return True
    return r == Molecule('oxygen')

@register
def my_reaction1(r,c):
    if is_blue(r,c):
        return ['yay']
    else:
        return ['must be purple']

@register
def my_reaction2(r,c):
    if is_blue(r,c):
        return ['definitely blue']
    else:
        return ['17']
```
it would not be possible to log if you had to specify the function name, unless
you made `is_blue` a logger in itself. You could get the underlying reaction in
a similar way that the exception stack does.

### Useful Information
I can immediately see the need for about 5 logging levels:
 * None, just give the final product
 * Chain, give the sequence of reactions and intermediaries
 * Reasoning, say why each reaction was chosen
 * More reasoning, say why other reactions were not chosen
 * Debug, print EVERYTHING

None of these, besides perhaps Debug, really require the ability for
rule-writers to be able to print things out. As I see it, relatively few
reactions will be taking place but LOTS of options will be tried, so most of the
work of the language is not done by running user code, it's done by running all
these different requirements checkers and seeing which ones line up the best.
You might want a requirement checker to say _why_ it decided that it was not
suitable, but if you enabled that, _every_ requirement checker would be printing
like mad. So maybe the option to enable logging per-requirement, or only enable
logging on passing requirements, could be helpful.

## Syntax
This may be what we talked about last week, but it looks like in your
examples/tests, the user needs to write the same thing twice quite a bit. In a
reaction like
```
@register_reaction_mechanism('a', {'requirement1': requirement2})
def a(r, c):
    return ["Hello, world!"]
```
You have to write `a` twice and `requirement` twice. Paring this down to just
saying
```
@register_reaction_mechanism(is_blue, has_oxygen)
def adamsMechanism(r,c):
    return ['NOPE']
```
could still give all the necessary information (in function names and
docstrings) but is a lot cleaner. 

## Focus
It seems like you've been saying that you DSL is people writing
`react(Molecule('O2'))`, but I don't think that's the right focus -- it's too
narrow to be a real language. Really (in my opinion), you should be making it
nice to specify new reaction mechanisms, because that's the hard part and the
part that makes your language extensible and therefore useful.

## Other
Maybe requirements should return a floating pointer number between 0 and 1 that
represents how "likely" they are to happen? If two reactions both say that they
will happen, which one wins out?
