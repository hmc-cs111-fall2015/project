# Preliminary evaluation

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

