**Introduction:** Describe your domain and motivate the need for a DSL
(i.e., how could domain-experts use and benefit from a DSL?). What is the
essence of your language, and why is it a good language for this domain?

_Note: Your project description can serve as a good first draft 
of the introduction._

# Project description and plan

This project serves a group of people who share a set of spaces and need to use the spaces at various times. Examples include kitchens, lab spaces, and study room. This language would be good for any user to reserve a space or designate the space as 'occupied'. The project involves three main components, an intermediate representation, a front-end and a back-end. The plan is to develop in that order as well. The intermediate representation will take the front-end language and convert it into object relations for the back-end. The front-end will be the outer language for users to interact with space and event management. The back-end will hold the persistent objects and information about rooms.

## Motivation

This project is interesting to me because it solves one of my frustrations at Harvey Mudd. When I try to organize events, I find it frustrating to check multiple dates and times or try to do multiple reservations. A DSL is an appropriate solution because the management system needs to be intuitive so that any user will be able to use the system without burdensome training.

## Language domain

The domain of this project is the event management domain.

## Language design

The design of this language is a text-based query system.

A program in this language is a clause or set of clauses that query or change the data model.

When a program runs, the program is interpreted into the data model and which then translates the database info into the desired information. Or translates changes in the data model to database changes.

The program takes string inputs, such as room names and times, and produce string outputs.

Syntax errors are possible, which will need to be caught in the parser. Compile-time errors will likely not be an issue, but run-time issues may occur since there may be discrepancies between the data model and the database. These errors should be handled with comparisons between the data model and the assumed data model.
I will need to design the language to catch foreseeable errors and also prevent users from changing data models in an inconsistent matter.

## Example computations

When asked for when a room is open, the program should check the schedule for that room and then return the schedule.

When asked for what rooms are open at some time, the program should check the schedule for that time period and then return the rooms that are open.

When asked for the schedule, the program should show a list of rooms and their availabilities. 

When a room is requested, the program should check the schedule for availability and then return whether the reservation was successful or not.

Each of these requests could be combined to automate looking for an open room.

**Language design details:** Give a high-level overview of your language's
design. Be sure to answer the following questions:

-   How does a user write programs in your language (e.g., do they type
    in commands, use a visual/graphical tool, speak, etc.)?
-   How does the syntax of your language help users write programmers
    more easily than the syntax of a general-purpose language?
-   What is the basic computation that your language performs (i.e.,
    what is the computational model)?
-   What are the basic data structures in your DSL, if any? How does a the user
    create and manipulate data?
-   What are the basic control structures in your DSL, if any? How does the user
    specify or manipulate control flow?
-   What kind(s) of input does a program in your DSL require? What
    kind(s) of output does a program produce?
-   Error handling: How can programs go wrong, and how does your
    language communicate those errors to the user?
-   What tool support (e.g., error-checking, development environments)
    does your project provide?
-   Are there any other DSLs for this domain? If so, what are they, and
    how does your language compare to these other languages?

## Language design

Users write programs in SimpleEMS by typing out queries and requests. The queries then get information from a local data model that draws information from an external data source such as a databse. The requests ask for changes that are then interpreted to changes in the data model which then makes the appropriate changes to the external data source. This DSL aims to have neither data structures nor control structures. There are hints of OOP in the sense that users will be manipulating 'themselves' as occupants in 'room' objects in the intermediate representaton. Ideally, this langauge will also show hints of control flow by enabling users to request a room for a number of dates! The DSL only requires text inputs but the text inputs have to be in a recognizeable format for the parser. (A syntax!) The output will also be text-based however we can do some ASCII formatting to make results easier to read. Programs can go wrong if the intermediate representation/data model cannot reconiliate with the external data source. This could happen due to one-off errors and edge cases that were missed in testing (hopefully not) or due to corruption of data in tranfer (though unlikely). The program should be able to make a text output detailing at least the general idea of where the error occured ("your query was wrong syntactically right here <>" or "something went wrong with the database... try again in a few seconds or post a bug!"). I left a week of time for error-handling so I hope this project will be able to handle most errors. The environment in which they query in will be a Scala console environment. Other DSLs are generally graphical, e.g. the HMC EMS system. However, the system is clunky and hard to use. For users that prefer working from the console, this application fills that niche. Also, one language goal is that the API is flexible enough to allow someone to write a graphical interface if they so desired. 

**Example program(s):** Provide one or more examples that give the
casual reader a good sense of your language. Include inputs and outputs.
Think of this section as "Tutorial By Example". You might combine this section
with the previous one, i.e., use examples to help describe your language.

'''
// Describing rooms:
room {
    building : 'Parsons';
    name : '2470';
    open : '8:00AM';
    closed : '5:30PM';
    occupancy : '14';
    type : 'classroom';
}

// Describing queries:

reserve {
    start : '8:00AM';
    end : '9:00AM';
    date : '12/8/2015';
    occupants : '11';
    type : 'classroom';
}
'''

**Language implementation:** Describe your implementation. In
particular, answer the following questions:

-   What host language did you use (i.e., in what language did you
    implement your DSL)? Why did you choose this host language (i.e.,
    why is it well-suited for your language design)?
-   Is yours an external or an internal DSL (or some combination thereof)? Why
    is that the right design?
-   Provide an overview of the architecture of your language: front, middle, and
    back-end, along with any technologies used to implement these components.
-   "Parsing": How does your DSL take a user program and turn it into
    something that can be executed? How do the data and control
    structures of your DSL connect to the underlying semantic model?
-   Intermediate representation: What data structure(s) in the host language do
    you use to represent a program in your DSL?
-   Execution: How did you implement the computational model? Describe
    the structure of your code and any special programming techniques
    you used to implement your language. In particular, how do the
    semantics of your host language differ from the semantics of your
    DSL?

## Language implementation

The API is an internal language to Scala. I will implement the DSL as an internal DSL because I think an internal DSL is sufficient to make queries. This decision may change once the implmentation starts...
I chose to implment this in Scala because that is the language I am most familiar with. Also, it makes it easier to tie the IR with the front-end if they are in the same language. So this is a choice for the implmentor more-so than the user. In addition, the syntactic sugars that Scala allows are also more flexible than the other GP languages that I am familiar with. 
I have not made significant syntax decisions, most of my decisison have been made towards the API so far. 
The system will consist of an IR, what's implmented so far, a front-end "console query style language" that will be interpreted to the IR data model and then a db back-end that will capture persistent data objects. (Since EMS should have persistent data)

**Evaluation:** Provide some analysis of the work you did. In
particular:

-   How "DSL-y" is your language? How close or far away is it from a general-
    purpose language?
-   What works well in your language? What are you particularly pleased with?
-   What could be improved? For example, how could the user's experience
    be better? How might your implementation be simpler or more
    cohesive? Are there more features you'd like to have? Does your current
    implementation differ from your larger vision for the language?
-   Re-visit your evaluation plan from the beginning of the project. Which tools
    have you used to evaluate the quality of your design? What have you learned
    from these evaluations? Have you made any significant changes as a result of
    these tools, the critiques, or user tests?
-   Where did you run into trouble and why? For example, did you come up
    with some syntax that you found difficult to implement, given your
    host language choice? Did you want to support multiple features, but
    you had trouble getting them to play well together?
-   If you worked as a pair, describe how you have divided your labor and
    whether that division has worked well.

_What works well? What are you particularly pleased with?_
I like the language feature base that I am working into the language.
The goal of the language and the query system I am working on still seems to be the way to go.
I worked out some examples on paper on my own and during the prototyping studio time, and the general way it works is intuitive.
I did notice that what I wanted my language to do and how I was building the AST/parser were pretty different. So, this week I spent some time rebuilding the AST.

_What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive?_
I am having a lot of trouble building out the parser and I need to really work on this over the long weekend. The implementation tried to do too much in the intermediate representation and front-end and I did not have to correct seperation of concerns that would make the implmentation *much* simpler. So, these are what I will work on for the remainder of the project. On the bright side, this means that I have one of the back-ends almost completed! (On the other hand, the parser is still in progress... and I have not made much progress on the parser).

_Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests?_
From the paper prototype, the project is going very well in terms of ease-of-use, which my critiquers suggested be something I prioritize. I have not made any significant changes as a result of user testing and self-evaluations but I think there are some small design choices that I made because of them. One example is how to handle errors (simply fail and say what went wrong opposed to asking if they meant this or that). 


_Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?_
I ran into a lot of trouble first with structuring scala code. I still have trouble with being expressive with Scala which is slowing me down. Also, the IDE is giving a lot of trouble with error checking.
A large part of that is also figuring out how to express the syntax I want and how to interpret that syntax into the AST/Parser/Interpreter format that we used for piconot-external. This one was a huge set back for me. I think it is because my understanding of how the three parts fit together and what roles they each played was unclear meant a lot of work that had to be redone or refactored. However, outside of this project, I think this model is really cool for implmenting languages so I have definitely learned a lot over the past few weeks.

_What's left to accomplish before the end of the project?_
* Writing a parser that matches the new AST that I wrote this week
* Developing a back-end that allows me to test that the parser and AST are working as desired
* Writing sugar.scala to make the parser easier to understand
* Adding equivalent keywords into the parser so that things that should work in the same way ("after 8 pm before 9 pm" and "between 8pm and 9pm" should do the same things)
* 

_If you worked as a pair, describe how you have divided your labor and whether that division has worked well._
Solo project!
