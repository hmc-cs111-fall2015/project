# Project plan

## Language evaluation

Since I am hoping to return an iCalendar file as the output
to my program, it would probably be hard to test the syntax 
of the file itself. I plan on creating a test suite that
will add events to an iCalendar file one by one, and then
a complexCalendar script (my DSL) that should ideally create
the same events. It will then compare if the two calendars are
the same. This will be done in a testing suite


To test if iCalendar is achieving what I want it to, I plan 
on creating a script that would represent my Mudd schedule, and
after each large interation I would test if it creates the right
calendar, when imported into google calendar. 

## Implementation plan

I have already found the host language.

Implementing the semantics - 2 weeks

Implementing the syntax - 3 weeks (this depends on the scope achieved)

Date | Deliverables
--- | ---
November 8th | Intial Semantics Done (adding repeated events to icalendar)
November 15th | Prototype (Initial Syntax done for initial semantics)
November 22nd | Semantics and syntax for Templating
December 6th | Aditional features mostly implemented. 
December 11th | Final Project finished  / Final writeup

## Teamwork plan 

N/A