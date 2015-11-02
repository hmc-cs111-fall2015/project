# Project description and plan

## Motivation
_Why is this project useful or interesting, what problem are you trying to
address, and why is a DSL an appropriate solution?_

This project tries to address the problem that writing a state machine in C++
is a really painful experience to get all the features one might want and is a
task that has to be done in basically the same way for every robot. A DSL is
appropriate because people can write their logic in the DSL but also be able to
freely call their code written in C++.

## Language domain
_What is the domain that this language addresses, and why is the domain useful?
Who will benefit from this language? Are there any other DSLs for this domain?
If so, what are they, and how might they influence your language design and
implementation?_

The domain of this language is programming robot logic, specifically for
arduino. Instead of having to write all logic in a GPL such as C++, this
language will be an internal DSL in C++ that will let you write robot logic more
simply.

There are similar DSLs that are external that let you write all the robot code
in an entirely different language, but taking the power and expressiveness of
C++ and making it easier to use is a niche that I do not think has been filled
well. I will look at how the external DSLs work and see what ideas from them I
like.


## Language design
_If you had to capture your DSL's design in one sentence, what would it be? What
constitutes a program in your language? What happens when a program runs? What
kinds of input might a program take, and what kinds of output might it produce?
Are there data or control structures that you know will be useful? What kinds of
things might go wrong in a program in this domain (e.g., syntax errors,
compile-time errors, run-time errors)? How might you design your language to
prevent such errors or to clearly communicate the results of errors to the
user?_

My DSL is designed to make coding a state machine simpler. In my language, a
program will be a specification of states and state transitions. The inputs and
outputs will be those of the robot itself, i.e.\ sensor inputs and motor
outputs. A lot of C++ will be used for things like data and control structures,
although my DSL will obviously add state data structures and control flow via
state transitions. Errors outside of normal C++ errors could happen when a state
transitions isn't specified (you haven't told it what to do with a certain set
of inputs) or if the robot simply does the wrong thing. In the former case,
there should definitely be a compile-time check for exhaustiveness that gives a
clear error message (lots of compilers do similar things so I can take ideas
from those), but in the latter case there's not much I can do to help the
programmer except for making the framework simple.


## Example computations
_Describe some example computations in your DSL. These computations should
describe what happens when a specific program in your DSL executes. Note that
you shouldn't describe the syntax of the program. Rather you should describe
some canonical examples that help someone else understand the kinds of things
that your DSL will eventually be able to do._


