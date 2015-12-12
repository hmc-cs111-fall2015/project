**Introduction:** Describe your domain and motivate the need for a DSL
(i.e., how could domain-experts use and benefit from a DSL?). What is the
essence of your language, and why is it a good language for this domain?

This project serves website designers who seek to create an event management system, or reservations system. These systems in turn serve a group of people who share a set of spaces and need to use the spaces at various times. Examples include kitchens, lab spaces, and study room. This language would be good for any user to reserve a space or designate the space as 'occupied'. The language also seeks to descibe rooms, so that users can also define a set of rooms. I took on this project because it solves one of my frustrations at Harvey Mudd. When I try to organize events, I find it frustrating to check multiple dates and times or try to do multiple reservations. A DSL is an appropriate solution because the management system needs to be intuitive so that any user will be able to use the system without burdensome training. This langauge draws ideas from SQL, and JSON to provide easy to read descriptions of reservations and rooms while allowing users to query against a constraint solver. SimpleEMS is an appropriate language because it will act as an easy to read intermediate langauge for those who wish to write GUI's for reservation systems.


**Language design details:** Give a high-level overview of your language's
design. Be sure to answer the following questions:

-   How does a user write programs in your language (e.g., do they type
    in commands, use a visual/graphical tool, speak, etc.)?
-   How does the syntax of your language help users write programs
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

Users write 'programs' in SimpleEMS by typing out descriptions of queries and rooms. As part of a larger system, the queries then get information from a local data model that draws information from an external data source such as a database. The requests ask for changes that are then interpreted to changes in the data model which then makes the appropriate changes to the external data source. The syntax allow for users to write code that is easy to understand and alter since we have scoped down the words and data types that users can use. Currently, the language supports ints, strings, and dates as field values. The language currently is set up to parse, and then return a mapping of fields to values. While this language was designed for schedule constraint solving, there was not enough time to implement one for this project (especially considering that I switched the language I was developing). So, the language will simply provide a mapping that can be plugged into a constraint solver library with some wrapping to provide calendar functionality. The basic data structure it the very map that users are manipulating when they write out their program. The DSL requires text inputs in the forms of the example programs shown later. DSL currently outputs a data structure, but the add-on will print out the mappings to show that it works. Because of the late switch, there is no error-checking or development environments. These types of features would be the next step in the process of developing this language. For 'functionality', many JSON libraries provide the same type of functionality because they are showing mappings. However, JSON can syntactically frustrating and this provides a simpler way of describing fields and values. For event management, I do not know of another langauge that provides an intermediate representation between the interface and the constraint-solver.

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
