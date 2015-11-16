# Critique: 16 November 2015

Alex Ozdemir

First off, great work - it seems like your decision to switch to python has
allowed you to get all sorts of stuff done!

## Which Constraint Solver to Use

I agree that [NumberJack](http://numberjack.ucc.ie/) is probably the right tool
for your DSL because it supports cost function optimization. The documentation
for it seems a bit tough to read, but it's probably worth it.

Alas, the Python-Constraint library does seem to have a very well designed
interface.

## Syntax and Design

I agree that the +/- business seems a bit clunky - I think doing a pre-parse
pass as discussed may be an appropriate solution. If that doesn't work out I
know it is also possible to make the parser whitespace-sensitive and then
specify where extra whitespace can go.

I wonder how you are going choose weights to give each constraint the users
indicate. Will the different types of constraints be mapped to different
weights? Will the users be able to specify which of their constraints they
value most?

I ask because I think that if you allow users to weight their constraints you
will need to be thoughtful about how they indicate those, and what those
weights mean.

## Validation

I noticed that you're writing a fair amount of code to do validation on the
input. I think it is super cool to do that validation before running the
program, as you're doing! I do wonder if all of the validation can be done
statically though. If you end up having to check some errors statically (before
the program runs) and some dynamically (while the program runs) then it might
be good to be thoughtful about which errors are being caught when, and how
those error-catching systems work.

To that end it may be valuable to list all the types of errors that could arise
and then identify when you would be able to detect each type of error.

## Next Steps

I think some appropriate next steps might be to hook up Numberjack to the
system and have it solve grouping problems without weighted constraints. I
think from their adding the weights would be a natural extension.
