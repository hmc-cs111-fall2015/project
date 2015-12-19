# Project plan

## Language evaluation
How will I evaluate my language design?
1. What features did I plan for my language (how many types of group projects) that it can support?
2. How intuitive is it to use? (Test by asking a intro CS person who has never seen my language to try and use)
3. Do programs for making all different kinds of groups look like they are all in my same language? (AKA does it look like I just wrote several different languages for several different cases? cohesiveness is KEY)
## Implementation plan
I got behind this past week because I have been so sick but I think that my implementation has to start with the front end. I think I have located the [constraint solver](http://bach.istc.kobe-u.ac.jp/copris/) I want to use but its not a perfect solution. I really think that the ideal situation would be parsing and doing logic in Scala, and then passing to a prolog constraint solver. I think that this would allow for a much much prettier system.

After I solve the parser (and therefore set up the syntax of my language) I will need to figure out the logic of how I will weight and handle different constraints. I think the breakdown of that will look something like this:

__By Nov. 8: Catch up on time lost and lock down what tools I want to use, I really need online feedback here because I am unable to meet with anyone in person or meet with Prof Ben :(__

By Nov. 15: Write a parser and IR and get it to a point where I can do basic logic I want to do in Scala (accessing constraints individually, printing out all of the variables relavent to each name, etc)

I think beyond this point, I will need to get closer in order to know what I need to do. I need help figuring out what my strategy is for solving constraint problems will be (When constraints aren't always constraints, theyre more like hopes). This is a pretty weird grey area that I am unfamiliar with.

## Teamwork plan
N/A
