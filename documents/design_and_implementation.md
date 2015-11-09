# Language design and implementation overview

## Language design
_How does a user write programs in your language (e.g., do they type in commands, use a visual/graphical tool, speak, etc.)?_  
They will write a normal Python program that uses the functions and classes that come built-in.

_What is the basic computation that your language performs (i.e., what is the computational model)?_  
It analyzes the chemical reactants, as well as the chemical conditions, and based off of pre-determined
criteria attempts to predict how they will interact in the given circumstances.

_What are the basic data structures in your DSL, if any? How does a the user create and manipulate data?_  
The basic data structures are molecules, represented as modified graphs.  In general the user won't
have to do too much direct manipulation of data - they can load their molecules from many different common
chemical file formats, or specify the atoms and bonds as elements in a standard Python dictionary.  Beyond 
that the manipulations are performed by the program itself.

Additionally, the user can define their own data structures as needed and register them for specific types
of reactions, allowing the language to use them as appropriate or as needed.

_What are the basic control structures in your DSL, if any? How does the user specify or manipulate control flow?_  
In general control flow should be unnecessary for most programs, however it has access to everything that
can be used in vanilla (C)Python.

_What kind(s) of input does a program in your DSL require? What kind(s) of output does a program produce?_  
It needs to get the molecules in - these will usually be represented by text files (such as CML or SMILES).
It produces similar output.  

There (may) also be a molecule viewer, however this would be a stretch goal.

_Error handling: How can programs go wrong, and how does your language communicate those errors to the user?_  
If the user tries to define their own reaction mechanisms and/or data types, and they fail to meet the requirements
of the program, errors will be thrown as normal Python exceptions.

Failed reactions/impossible reactions will be treated the same way.

Otherwise, all of the normal Python restrictions apply.

_What tool support (e.g., error-checking, development environments) does your project provide?_  
Not much beyond what is provided with Python.  Depending on development time, visualizers and linters
may be developed as well.

_Are there any other DSLs for this domain? If so, what are they, and how does your language compare to these other languages?_  
See [the previous week's response][1] - the answer is unchanged.

## Language implementation
_Your choice of an internal vs. external implementation and how and why you made that choice._  
I chose an internal DSL because I think I'm going to have a much harder time getting everything working
without the additional hassle of parsing and implementing everything in an external DSL.  Additionally,
while I may try to make an external DSL available at some point, all extension features will have to be
written in the host language because I expect they may require the expressivity of a GPL, and I don't see
the point of implementing all of that myself.

_Your choice of a host language and how and why you made that choice._  
I chose Python because it is by far the language I am most comfortable with.  Additionally, given the time
constraints of the project I decided that Python would give me the optimal results while also giving the 
fastest experience in terms of development time.

_Any significant syntax design decisions you've made and the reasons for those decisions._  
Not especially - I haven't implemented my own syntax, just provided a few functions and decorators. These 
were chosen for readability and ease of use.

_An overview of the architecture of your system._  
Users write functions that serve as reaction mechanisms, and register them with the language. They can also
do this with their own custom data types.  They then write a (mostly boilerplate) program specifying
what things should be reacted together, and the conditions under which they should be, and the system
analyzes those components and tries to determine the best way to react them together.


  [1]: https://github.com/PyCAOS/project/blob/master/documents/description.md#language-domain
