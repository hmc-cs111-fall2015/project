#Introduction
In nearly every academic setting there is a need for group projects. Additionally, everyone who has ever worked on a group project can testify to the fact that a good group can enhance everyones experience while a bad group can pretty much ruin everything.

As things stand currently the main ways of creating groups are participants choose, organizer chooses, or random. None of these are ideal because participants choosing often leads to friends working together or a failure to consider all possible group options. Teachers choosing often works well but then the teacher has to put in major effort and also is at fault if the groups dont work out. Finally, random groups are simply an acknowledgement that there is no good way to find groups. I disagree with that, though. I think that if we can leverage input by both the participants and the organizers then we can try and make it so there are always good groups!

A languge is perfect for this because the idea, making groups, is constant while the way that looks (think about how different it might look for a group project done in an english class to write a book together vs clinic groups). A language allows expressiveness regardless of what the nouns are. Grouper is all about trying to ensure that there is input from all people that have stake in the group project (organizer and participants) and trying to leverage all that information into making people as happy with their groups as possible. 

#Language Design Details
When a user wants to write a Grouper program they write a text file that has two parts: The header, where they specify general information about the groups and the project, and the body, where they specify information about each person that is to be grouped. These parts come together to be the entire program. 

The syntax of Grouper is intuitive and clean, and allows a non technical user to essentailly do complex constraint programming without ever knowing that they are. The computational model of my program is essentially a constraint solver, but it is actually more than that because it also uses weighted constraints and other analysis to create the best possible groups (in theory). The only datastructure is my DSL is the Groupee, which is the structure that represents one person to be grouped: their interests, partner preferences, and positional choices. There are no control structures at all, except for the declarative words `Header:` and `Body:`.

Grouper takes a .txt file as an input and outputs a string to the command line. There are two types of errors, syntactic and logic. The syntactic errors are checked before the program is run and return an error to the user in the command line. Logical errors are not handled very well at this point. I did my best to minimize the ability to make logical mistakes but if you specify an impossible problem, no solutions will be returned.

There are no tools provided for the user, except for some example programs which are admittedly very helpful. There are not really any other DSLs in this domain.

#Example Program
The following is an example input for a Groupe program:
```
Header:
    Group Size: 3
    Names: Robin,Jackie,John,Marcus,Evan,Lane
    Interests: Math,Chemistry,Biology,Politics,Media Studies,English,History
    Positions: Leader,Communications,Head of Design

Body:
    Groupee Robin:
        Dont Want To Work With: Marcus
        Want To Work With: Jackie,John
    Groupee Evan:
        Interests:Math,Biology,Media Studies
        Positions:Leader,Head of Design
        Want To Work With: Jackie,John
        Dont Want To Work With: Marcus,Evan
    Groupee Jackie:
        Interests:English,History,Biology
        Positions:Communications,Head of Design
        Want To Work With: Marcus,Robin,Evan
        Dont Want To Work With: John
    Groupee Marcus:
        Interests:Chemistry,Politics,Math
        Dont Want To Work With:Jackie
    Groupee John:
        Positions:Leader
    Groupee Lane:
        Want To Work With: Robin,Marcus,Jackie,John
        Interests: Math,Chemistry,Politics,English,History
```
This input would give the following output:
```
Group 1 is Evan, Jackie, Robin and they have mutual interest in Biology. Jackie has been assigned the role of Communications, Robin has been assigned the role of HeadofDesign, Evan has been assigned the role of Leader


Group 2 is John, Lane, Marcus and they have mutual interest in Chemistry, Math, Politics. Marcus has been assigned the role of HeadofDesign, Lane has been assigned the role of Communications, John has been assigned the role of Leader
```
#Language Implementation
Grouper is written in Python3 which was chosen due to my proficiency in Python. I wanted to be able to spend more time writing the code instead of struggling to express what I wanted to express.

My DSL is external which was definitely the right choice because I really wanted to have a clean and simple syntax that did exactly one thing. Grouper starts by parsing the text file using a framework called [PyPeg2](http://fdik.org/pyPEG/). This framework worked really great, although it mandated me using Python3, and allowed me to easily define a parser that made a lot of sense to me and was readable and functional. After parsing I had an internal representation in two parts. The header was a dictionary of fields with their values while the body was a list of a python class `Groupee` that stored all the relevant information about each groupee. This worked really well for me. The backend is pretty complicated but the gist is this. I take in the data and set up a constraint problem.

I then apply constraints in three steps, checking to see if I have narrowed down the problem enough after each set of constraints is added. I use signals to interrupt the `getSolutions` method after a certain amount of time. If there are no solutions I say that and if there is not enough information to slim down the problem to solutions in a reasonable amount of time then I say that as well. Finally I take the data returned by the solver and `uniquify` it by making sure all solutions are unique. I use that list of solutions to formulate a return string which is passed back to the programmer on the command line.

#Evaluation
My language is super DSL-y. I think that a non-programmer could use it (if it worked better) and you can _really only do the one thing it was designed to do_ in it. I think that is really awesome and is a big success for me. Im really excited about my successes with the parser by using a prepass function (to clean up the input and make it more computer-readable), the 3 step constraint solution to simulate weighted constraints, and how clean and simple the syntax is. All of these things were focuses of mine (get the syntax I wanted, have weighted constraints).

I wish that my constraint solving was better. It just doesnt really do anything that a human couldnt also do pretty quickly, and I think that the algorthmic thought about what cosntraints are important etc is also not perfect. Additionally I really wish the user could _say more_. I initially had hoped that the user would be able to specify what fields would be included in the header/groupees for any given program. I also wish that the input wasnt so finickiy. I really like the syntax but if you have weird whitespace anywhere or anything it breaks the parser which sucks. I also wish it used python 2.7 instead of python 3, simply because it is more widespread.

As I mentioned in my preliminary evaluation, my evaluation plan was pretty weak so I dont have much to look back on. I planned on evaluating on more holistic things,like did i implement all the features I wanted to. I was obviously not going to, so its not a very useful evaluation tool. I havent made any significant changes to my project due to my plan, which is a real shame.

I ran into trouble in a couple places. The first was trying to get my parser to work with 2.7, which I eventually gave up on. This is really interesting because the design choice to switch to python 3 ended up dictating my choice of constraint-solver. I wanted to use this parser and _also_ a constraint solver that had weighted constraints but there _werent any for python 3_. This was a trade off I made. Additionally, I just ran into trouble using the constraint solver in general. I am new to logic programming and that was pretty pretty challenging for me.

#Conclusion
I had such a fun time and learned so much doing this project. I worked really hard at times and also flagged when I hit a wall at times. I learned a lot about working through times that I felt like I was making no progress. I feel like this project was a great success, even though I didnt necessarily get all the features I wanted or all the functionality I had hoped.
