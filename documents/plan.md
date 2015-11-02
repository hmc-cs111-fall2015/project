# Project plan

## Language evaluation

I will know that the language is good if writing a simple state machine for a
robot is very easy and takes very little code. As a metric, writing picobot in
C++ should be only a few lines of code.

I should also ensure that error messages are high-quality. I can make programs
that have errors in them, but to get a truly good idea of how good the error
messages are I should ask someone else to try to use my DSL and see what the
common errors that they get are, and how understandable the error messages are.

To make sure that the language actually works I'll need to write a back end for
a robot that I have and also think of a complex thing I want it to do. This will
be tricky but I'm sure I'll get inspired.

## Implementation plan
Since I'm doing an internal DSL in C++, I don't have to worry about a parser,
just the semantics. Thus, almost all of my implementation work will be there,
and probably in C++.

### Schedule

 * November 8: A mostly-complete list of semantic features
 * November 15: Example programs in C++ showing off most of the features I want
   in the syntax I want. Also be done with back-end implementation for the
   robot.
 * November 22: Basic syntax and semantics implemented
 * November 30: Everything works!
 * December 6: Extra features / External DSL / Slop
