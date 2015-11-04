# Project description and plan

## Motivation

I initially got the idea of some sort of "constraint solving" DSL from chatting with Prof Ben, and he pushed me to consider the problem of forumlating clinic groups (at HMC). Since I'm not an HMC student, may not do clinic, and have not really had any friends go through that, that problem didn't strike at my heart chords the way I had hoped a project might. 

I have however been a part of group projects and felt the very real difference between a good group and a bad group. It can be semester-changing, honestly, and I hope to solve the problem of bad groups for everyone, in every situation, for every project (ambitious, i know :))! 

I think that a DSL is a really good solution to this because every group project is different in a lot of ways, but in a very predictable set of ways: group size, need for specific roles, subject matter/freedom to choose subject matter, etc. I think that this makes a DSL a _great_ solution for this problem because it allows me, as implementer, to plan for group projects to be different in these ways and allow it to be __easy__ for my user to specify how they want their project to be! Also, I think that there is enough information necessary to create good groups that its pretty much impossible for the human brain to do it for more than groups made form 6-7 people, say. This hopes to simply extend that kind of logic to larger pools, with any sized groups, and perhaps even improve the logic!

## Language domain

The domain for this language is any situation in which you need to make groups that will work well together. This domain comes up _all the time_ in academia and quite often in real life, to boot. I would imagine that professors everywhere would save countless hours and stress over bad groups if they had a working tool like this and, as Prof Ben said, "I would use it"

There are some other tools in this domain but they all basically revert back to three categories: self selection, organizer selection, or random selection. __Self selection__ tends to lead to friends working together which has high boom-bust potential and then those who don't have friends in the class basically getting randomly selected. __Organizer selection__ is dubiously successful at best and requires significant work for the organizer who then is left responsbile (kind of) for the success and failure of the groups. __Random selection__ is exactly what it sounds like and is randomly successful and unsuccessful. 

On some level, if all else is equal, decisions must be random but I aim to design a language that leads every grouping choice to be made with _intention_. 

## Language design

_Simple format for organizers to specify reasons why people should or should not work together._

A program in my language will look like a series of declarations of global variables, as mentioned above, that will stand to heavily (but easily) influence the constraint solving such as group size. Then it will be a series of data structure declarations of the (i think) only data structure in my language: The Groupee. This will consist of a name followed by several fields that are filled in with a variety of information like topic interests, position interests, experience, people they do/don't want to work with, etc.

When a program runs essentially the language will need to be parsed into a number of constraints that are then put into a constraint solver to determine the groups that allow for the _least flaws_ in the constraint solver. This is kind of a tough problem because most constraint solvers are just like "well nothing works" instead of "heres the thing that works the most" but I think I should be able to work around this __(help here, please! I need to find a way to say "I want this" instead of "I need this" to a constraint solver but I'm not really sure what that looks like)__ Each program will output a list of lists! Probably I'll render it nicer than that but thats the jist, a list of lists of names that constitute the best groups, according to the constraints I was given.

I think I _shouldn't_ need any control flow structures and should only need the _Groupee_ data structure, but thats a big chunk of works that can't be overlooked!

Things that can go wrong:

    * Failure to specify necessary global vars (group size e.g.)
    
      * This will need to be an error and ask the user

    * Contradictory constraints (John says he wants to work with Sally, John says he does not want to work with Sally)

       * This could either be an error and ask the user, or just ignore the contradictory constraints

    * Group Size is larger than number of people input

       * I'm tempted to say that I would just ignore this and return a group of all people submitted but I feel like this _must_ be a mistake so I think it would have to be an error and ask the user.

## Example computations
