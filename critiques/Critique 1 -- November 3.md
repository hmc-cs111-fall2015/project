Note: I'll group my comments by section they pertain to, with misc comments at the bottom

## Motivation

I agree that the usual calendar creation tools struggle with this problem. 
One nice thing about the fact that you have many "competitiors" is that it's a good way to frame your evaluation of the DSL - 
you can ask yourself "Would I rather be using this language than directly using the interface of google calendar or iCal?" 
If the answer is no, you can ask what features you could add to the language to change the answer to yes. 

I also agree that repeated events is where this language would prove most useful, but you should make sure that it's easy to add
one-off events in the language too. It seems to me like writing your entire calendar in one place would be more useful than 

## Language domain

While there are no other DSLs proper in the domain you're examining, there are certainly applications that are centered around 
allowing students to export their class schedules - you can check out Cheng Wai's schedule exporter 
[here](https://bitbucket.org/cwkoo/portal-funnel/src), and I believe Alex O. has added this functionality to Casey's scheduler
applet. That said, these applications are clearly limited, and I think that your language still has a very important place
in the problem domain here. (Note that in both of these applications, you can't specify your non-classes schedule).

## Language design

I agree that allowing overlapping events is a good thing - users might want this. You could, if you like, implement a warning
system and warn the user if their calendar contains overlapping events.
I'm not sure what you mean by date ranges that are defined on an event that don't agree with each other - could you elaborate?
Do you mean like the start date for a repeating event being after the end date?

## Example computations

These computation descriptions sound good to me, and sound like relevant use cases. I would recommend writing
out the code of a few example programs before you start writing the code - you're going to want an idea of how to turn your
intent into a concrete syntax before you start writing code. In particular, I'd recommend writing out the most complicated
thing you'd like your users to be able to say and use that for a model for your parser/IR. 

Here's an example syntax I thought of (you'll note that it looks a lot like SQL - this may be the influence of my DBs class :smile: ):
```
CREATE EVENT "Domain Specific Languages" ON MONDAY AT 1:15-2:30 FROM 9/1/15 TO 12/11/15 EXCEPT ((10/10/15 TO 10/14/15 AND 11/22/15 to 11/26/15));
```

**EDIT**: I note that you've included an example syntax in your project-notebook for this week. One critique I have of your example
syntax is that it's very complicated for a non-programmer - it follows a distinctly object-oriented style that only 
programmers have intuition about. In using this structure, you may be limiting your potential audience. 

## Language evaluation

I like that you're thinking of using a test suite to evaluate your language! Along the way, you can also do manual testing
to check if your language is doing what your want it to. In addition, can you think of unit tests that you could use for specific
parts of the language? This could be useful in diagnosing problems when the language doesn't do what you want it to. 

## Implementation plan

Scala is a good choice :thumbsup:

Your implementation plan looks pretty good to me, though being able to add templates in just a week seems quite ambitious. Good luck!
Within your implementation plan, what do you mean by syntax and semantics? Are you planning to use the parser/IR/semantics 
division of concerns that piconot-external does. If you are, which category does the IR fall into - syntax or semantics?
Since you're building the semantics and syntax in separate weeks, at what point are you planning to have a language that you
can test for "correctness"? Can you think of ways to test the semantics before you've implemented the parser? 

The last comment I'd make about your implementation plan is this - in case parts of the implementation take longer than expected, 
do you have an idea of what features you'd be willing to cut to speed things up? If not, that would be a point worth thinking
about. Similarly, if you finish massively ahead of time, what additional ways could you add polish? 

## Design notebook

What do you want priority to do in the context of your DSL? 
Will this just translate into a priority setting in the iCal output?

I see what you mean about scoping! I think this a really interesting concept - hopefully the language features lectures
will be helpful to you when implementing scope. 

## Miscellaneous

You mentioned that your critique partners could help you by thinking of more use cases. I think that building the 
language around use cases is a dangerous road to go down - exhaustively enumerating the set of use cases for a calendar
seems like a very difficult task, and if an unforseen use case comes up late in the project it may force you to entirely 
redesign your language. I would focus on designing your language so that it's easily extendible, and let your users come
up with their own use cases. In that sense, I agree that giving your users a lot of freedom is the way to go.
