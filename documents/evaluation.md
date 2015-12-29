# Preliminary evaluation

#### What works well? What are you particularly pleased with?
The state and interrupt functions work well. I'm really pleased with how nice
the time functions are. I switched from using my own time class to using C++'s
chrono library and it makes some things really nice (although it also makes
other things more annoying). 
#### What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive?
There's a few things that I don't like. The design for substates is the best I
could think of, but it's still a little clunky for the simple tests I'm doing.
There are also a few other features that I think would be useful in some cases
but would hurt in others. For example, the interrupt condition checkers do not
work until some initialization has happened, so every condition check also has
to check to make sure the robot isn't in the start state. There are a few things
I could do to fix this. One is to give the user the ability to globally disable
interrupts, and start with them disabled, so once setup occurs they can be
enabled. In a related issue, currently my DSL's library defines the main method.
It might be nice if the user defined the main method and called a function in
the library to do the main loop, but I also feel like this detracts too much
from the language, since any initialization really should take place in a start
state.

I'm pretty happy with my implementation. I think I implement enough features for
my DSL to be useful, but not so many that a user would be overwhelmed. It's very
predictable how my DSL will operate, which makes it less confusing to debug user
programs.

#### Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests?
I've re-visited my plan pretty frequently while designing and implementing, and
I've stuck to it pretty well. I have implemented what is basically picobot and
it was very simple, so I'm happy about that. I have not yet written a real back
end for a real robot or asked someone else to write an example program. I have
not done the former because it would require a good amount of time not really
related to the project that I have not yet found, and I have not done the latter
because I don't have a good back end. Soon I should get a simple back-end
working so that I can ask other people to test.

#### Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?
The biggest trouble I ran into was with the substates. My initial idea for them
was too vague to be realized, and any sort of solution with coprocesses is too
hard to implement in C++. The current way isn't the greatest but it's the best
that I can come up with.

The syntax didn't turn out to be that bad. I took it as a given that some things
would not look the nicest but decided that having it in C++ would outweigh the
disadvantages of the ugly syntax.

#### What's left to accomplish before the end of the project?
Basic functionality appears to work pretty well now. The main thing I want to do
now is to get a back end put together and try writing some example programs
myself and then ask other people to write programs in it. This will give me lots
of feedback that I can use to tweak my language.
