# Introduction

State Of The Robot is a domain-specific language that lets users easily create
state machines for robotics in their C++ code.

## Motivation
This project tries to address the problem that writing a state machine in C++
is a really painful experience to get all the features one might want and is a
task that has to be done in basically the same way for every robot. By having
this functionality wrapped up in an internal DSL, people can write their logic
in the DSL but also be able to freely call their code written in C++.

## Similar Languages
There have been many languages designed for robots, such as [the LEGO Mindstorms
languages](http://www.legoengineering.com/program/nxt-g/). The main problem with
these is that they are external DSLs that have been designed for beginners. They
can be nice to use to get started, but the language designers were not able to
get a necessary level of power in the language for more heavy usage. Since the
languages are external, it's not possible for a user to just switch to the host
language's features to do what they want, they must rewrite their code in an
entirely different language. Since State Of The Robot is an internal DSL, if it
is missing any features, a user can just use straight C++ code to do what they
want while still using the DSL where it is appropriate.

# Language design
My DSL is designed to make coding a state machine simpler. In my language, a
program will be a specification of states and state transitions. The inputs and
outputs will be those of the robot itself, i.e.\ sensor inputs and motor
outputs. A lot of C++ will be used for things like data and control structures,
although my DSL will obviously add state data structures and control flow via
state transitions. Errors outside of normal C++ errors could happen when a state
transitions isn't specified (you haven't told it what to do with a certain set
of inputs) or if the robot simply does the wrong thing.

## Language Use
A user writes programs by writing their robot code in C++ but use my DSL for
logic features. The basic computation is to move between states in a state
machine and call user-provided functions when they asked them to be called. The
only real data structure in my DSL is the state of the robot (including
substates), along with all the different functions supplied by the user.

# Examples
Here is a basic example, showing how basic state functions work.

Here we include the header file for StateOfTheRobot
```
#include <StateOfTheRobot.h>
using namespace std::literals::chrono_literals; // for 500ms, 2s, etc
```

Here we declare what states the robot has
```
DefineStates(Start, GoNorth, GoSouth, Confused);
```

Now we define several state functions. The first argument is the state in which
the function will be called, and the second is the function. Usually, the
functions you pass will be lambdas, and this is shown below. You can see that
`set_state` changes state and `tm_in_state()` returns the amount of time the
robot has been in that state. State functions are repeatedly called while the
robot is in that state.
```
state_func(Start, [] {
    set_state(GoNorth);
    printf("Starting up!\n");
});

state_func(GoNorth, [] {
    printf("Moving north.\n");
    if (tm_in_state() > 2s) {
        set_state(GoSouth);
    }
});
state_func(GoNorth, [] {
    printf("Also moving north!\n");
});

state_func(GoSouth, [] {
    printf("Moving south.\n");
    if (tm_in_state() > 2s) {
        set_state(GoNorth);
    }
});

state_func(Confused, [] {
    printf("I'm confused!\n");
}
```

Here we define an interrupt function. To use an interrupt function, you give the
`interrupt_func` macro two arguments. The first is a function that returns a
`bool`. When this function returns `true`, the second function is called. This
is useful if you want your robot to be continually checking something such as a
bump sensor and want to immediately do something if it is pressed no matter the
state.
```
interrupt_func([]{return rand() % 400 == 0;}, [] {
    if (state() != Confused) {
        printf("Randomly got into interrupt from state %d\n", prev_state());
        set_state(Confused);
    }
});
```

# Implementation
As already discussed, State Of The Robot is an internal DSL in C++. State Of The
Robot is more than just a library because it changes what parts of the user code
is being run and essentially defines a new control flow for C++. This is exactly
what we want, since the DSL is supposed to define robot logic but allow any sort
of computation or robot command to take place. So the DSL controls the logical
control flow, and the user is free to write whatever they want in the blocks.

There are essentially two layers to my DSL, and a minor third one. The first
layer happens at compile time. C++ doesn't generally allow code to be run
outside of a function, but I wanted to let users register functions with State
Of The Robot outside of a function. I did this by writing macros that translated
function-like syntax into object construction, so that users would be calling a
constructor that registered the function instead of calling a function to
register it. This translation is important but pretty minor.

The first big layer happens at the beginning of runtime, before `main()` is
called. This is something that could theoretically happen at compile time, but
C++ does not provide the features to do it at that point. What happens is that a
dummy object is constructed for each registered function, and these dummy
object constructors add that function to one of several lists.

State Of The Robot defines the `main()` method. When `main()` is called, the
final layer starts to be executed. This is when State Of The Robot starts
keeping track of the robot's current state and substates and starts calling the
user state functions, interrupts, and global functions. User code can also call
State Of The Robot functions to do things like change the global state or
substates, so these variables have to be kept so that all the State Of The Robot
functions can change them.

# Evaluation
I think I did a pretty good job designing and implementing my DSL. The main
concerns I have about it now is that I have not written complicated enough
programs in it to see where it gets annoying to use.

I feel like State Of The Robot is very DSL-sy. Since it's an internal DSL, I
could just implement the features that I wanted and didn't have to make any
helpers that would push it more towards the GPL side. I would say that State Of
The Robot is actually more on the side of an API/library than a GPL, since it is
just something you include and use. But I still think it is thoroughly a DSL
since it fundamentally changes the way that programs are written from standard
C++, and it provides a whole new language on top of C++'s features. 

### Works Particularly Well
I'm really pleased with how nice the time functions are. I switched from using
my own time class to using C++'s chrono library and it makes some things really
nice (although it also makes other things more annoying). The user-defined
literals that let you say things like `if (tm_in_state() > 430ms)` are just so
beautiful.

### Could Be Improved
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

### Evaluation Plan
I've re-visited my plan pretty frequently while designing and implementing, and
I've stuck to it pretty well. I have implemented what is basically picobot and
it was very simple, so I'm happy about that. I wrote a pretty detailed backend
for a real robot, which I was really excited about doing. Unfortunately, the
robot I have does not have enough interesting sensors to be able to do much more
than move and turn. Adding something like a distance sensor on a servo would let
the language show its power and help provide good feedback on what features the
language should have, but that's a lot more work.

### Trouble
The biggest trouble I ran into was with the substates. My initial idea for them
was too vague to be realized, and any sort of solution with coprocesses is too
hard to implement in C++. The current way isn't the greatest but it's the best
that I can come up with.

The syntax didn't turn out to be that bad. I took it as a given that some things
would not look the nicest but decided that having it in C++ would outweigh the
disadvantages of the ugly syntax.

# Conclusion
State Of The Robot is about where I want it to be. There are potentially some
quality-of-life improvements that could be made, and some of them could require
rewriting almost all of the implementation code. But this is fine by me, since
the code was not the main point of the project. The ideas and design are the
important part, and that is preserved through any rewriting that may have to
take place.
