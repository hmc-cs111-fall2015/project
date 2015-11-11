# Critique 2
_Critiquer: Matt Valentine_

## Chemistry

You mention abstracting the chemistry details away, but I am not sure that is the case yet.
That is, you don't yet have any reaction code, a data format for reactants or
conditions, or condition checker predicates.
That's where the chemistry would actually exist.
It's nearly invisible to the dispatcher anyways.

I think it's more that the chemsitry details are being left to the user
That's perhaps reasonable, given that I'm sure they would all have their own
ideas of how to handle that part.

## Dispatch Implementation

As you noted, dispatch was not as tricky as you were expecting. That's because ultimately you are not dispatching
on static properties, but completely general predicates.
As such, all of the interesting and complex optimizations that are involved in multiple dispatch
are just unsuitable for your application.
As-is, all you can do is what you're already doing and just check all the requirements of each 

Now, it would certainly be _possible_ for you to change the system somewhat
for that all to work.
You would need to cache predicate results, for one thing.
But I would recommend that you do NOT do that.
You have a functioning dispatch system, and anything beyond that is unecessary for
the purposes of this assignment.

_Unless!_ you change the point of your project to focus more on the dispatch
side of things, and let the chemistry fall to the side. Which could work out fine.

## Dispatch Generalization

You ask if you should generalize your dispatch system,
and then allow the users to deal with the domain-specifics.
It sounds like you're suggesting that the main purpose of
CAOS is the dispatching system.
But I think there's a lot more that the dispatch systsem
has nothing whatsoever to do with.

- What do the _reactants_ and _conditions_ parameters actually
look like? How are they constructed, and how do you deal with them?
- How should people write code that runs reactions?
What should reaction code look like? How much abstraction can be done there?
- Similarly, how should people write condition checkers (like heat)?
- Do you still intend to implement condition importance and scores?

That is to say: If someone were to use CAOS, I would expect
_most_ of their effort to occur either in setting up reactants and conditions,
if they are a user, or writing code that runs reactions, if they are a
developer.

_But!_ That is if I am taking your project to be about organic synthesis.
If instead you were _really_ trying to make something about ranking
a bunch of different alternatives based on requirements/preferences,
such as what your dispatcher is a preliminary implementation of,
then that could indeed be a reasonable project,
and would end up meaning spending more time on the dispatcher,
which seems to be something you're very excited about.

## Code quality

My goodness, that's some thoroughly commented code. Also consistent style, separated files.
Great potential for debugging since everything is logged. That's going above
and beyond.

My concerns about the code are therefore only the actual design.
There are occasionally things like `info['function']`. This is a strange hybrid
between having a completely general object type (just a dictionary: could have any keys whatsoever)
and expecting it to have a certain format, with specific keys.
It might be better to have an actual data class. Then its constructor would guarantee
the existence of those keys that need to exist, and you can do `info.function`.

Generally some of the data layout, as in what keys are expected to exist and such,
appears to still be in flux. At times like these, it's easy for bugs to creep in
when you switch from one design to another. In a language with no static checking
like Python, this is especially problematic. That's another reason to maybe have
a specific class: there is at least a single "source of truth" for how things should
be organized.

I am also not sure what the purpose of the `name` in the requirements dictionary is.
Since predicates are shared amongst multiple mechanisms, it seems odd that you allow
each to name it a different thing. That's especially the case when you have things like
`'heat':heat`. It might make more sense for the predicate itself to know its own name.

## A couple syntax options

1. Rather than
 
     @register_reaction_mechanism('a', {'requirement1': self.requirement1})
 
 by using `**kwargs` you could also do
 
     @register_reaction_mechanism('a', requirement1 = self.requirement1)

 as long as you're expecting names to be identifiers.
 
2. Some various options for how requirements are done:

     requirements = {'heat':heat(0.5), 'light':light(0.2), 'resonance':resonance(1)}
 
 If the requirement predicate knew its own name:
     heat(0.5), light(0.2), resonance(1)]

 If all predicates were expected to have a priority, but the dispatcher
 dealt with it instead of the predicate:
 
     requirements = {heat: 0.5, light: 0.2, resonance: 1}
     requirements = {heat: Moderate, light: Low, resonance: Required}

3. If you felt like looking into some black magic, which I actually _do not_ recommend,
you could use a metaclass to handle the registration. In which case things would look like:

     class DielsWhateverItWas(Reaction):
         requirements = {'heat':heat(0.5), 'light':light(0.2), 'resonance':resonance(1)}
         
         def react(reactants, conditions):
             pass

 The Reaction class's metaclass would handle the registration automatically
 at class creation time. The name could come from class name, or from a `name` variable.