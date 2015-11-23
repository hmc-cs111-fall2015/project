# Preliminary evaluation

_What works well? What are you particularly pleased with?_

Right now dispatch feels quite elegant, and simply implemented.  There are a few
quirks regarding ordering and priority, however it mostly _just works_.  

_What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive?_

As suggested in the critiques, I think I might remove the dictionary aspect of the
requirements, and instead just the use the functions' names.  That way we avoid 
duplication in the form of `{'aqueous': aqueous_requirement}` in every section - 
instead I can just do `[aqueous]`.  Additionally, if I provide more use of
variadic keyword arguments (`**kwargs`) I can make this more easily extensible and
allow users to create functions that can use extra information.

I should also return product-condition pairs, instead of just products, as I may
want to use the (potentially changed) conditions for a subsequent reaction.

It might also be nice to have some sort of "run to completion" concept where if the
products of a reaction can react together, predict what happens there.

_Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests?_

I've been using a lot of tools like travis-ci, coveralls, and readthedocs.  They've
been super helpful in making sure everything runs, that it is well documented, and that
I have thorough tests.  Additionally, style checkers like flake8 and pep257 have been
invaluable as well.  I have 100% written cleaner, better tested, and well-documented
code because of these tools.

_Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?_

I've been avoiding some of the specific chemistry details because they're hard and I'm
not positive how I want to handle them.  I also have a lot of different reactions I'd
love to implement, but simply don't have time for.

_What's left to accomplish before the end of the project?_

I need to make reactions at least appear to work, or work if provided enough information.
Ideally the mechanisms can extract vital information from the reactants and conditions,
however for demonstrative purposes I may leave that out for now and put necessary information
into the `conditions` of the reaction.
