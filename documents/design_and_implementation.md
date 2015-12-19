# Language design and implementation overview

## Language design

In my language a user will type in commands but, ideally, a program will look simply like the statement of a problem. The user will just put in the information they have about each of the people to be grouped and the program will tell them the groups. 

The basic computation my language performs is constraint solving. It will weigh and balance different constraints that will range from `applied in an ideal case` to `cannot be conflicted`. The underlying computational model will simply be the constraint solver, however.

The only data structure will be that of a `groupee` (ha, groupie). This data structure will be flexible and be designed to be able to hold lots of different fields each having different types of data that are often included or not depending on the case. The user will create a groupee and assign it various pieces of information which will then be used when the program runs.

There shouldn't really need to be control structures, but there will be two areas of the program: the header and the body. The header will have various declarations while the body will contain all of the groupees to be grouped.

The input will be a text file (.gper, maybe?) that has all the data described above and will return a string (probably in the command line, or maybe in a gui later) that has 
`group 1: john, sally, bob`
`group 2: holly, michael, jim`
etc.

Programs can go wrong in only a couple of ways. There could be syntax errors, but in terms of logical errors the two that come to mind are conflicting constraints and constraints that dont make sense. This is something that I've been thinking about. For example should, in the header, a user have to specify which leadership positions are available so that, at complile time, my language can barf if Larry's leadership interests include `Notorious BIG impersonator`? Or should I accept that and then have my program just get bad results? __Errors will be communicated through the command line__.

I think that my language will not have very much tool support but there will hopefully be a GUI!

As discussed previously there are grouping softwares that are designed to be user choice, groupee choice, or random choice but nothing that tries to solve this problem in the way that I am, if executed how I'm imagining it.

## Language implementation

I've tenatively chosen an external implementation to give me freedom to remove the Scala flavor and make my syntax as easy as possible. I did however consider using an internal DSL in prolog, which is still an option, but have temporarily moved away from that.

I've chosen scala as my host language for a couple of reasons. First, Scala has awesome language design tools. Second, I want to learn Scala. Third, the constraint solving libraries I could find in python (which im most comfortable in) all kinda stunk.

There is a example design with some options/questions in `mockup.txt` in the Grouper repo.
