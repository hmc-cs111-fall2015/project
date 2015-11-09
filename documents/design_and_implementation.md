# Language design and implementation overview


## Language design

Codeviz illustrates the control flow of some code by means of a flowchart.
A valid Codeviz program is a valid program in the underlying language
(Java for the first iteration) with the additional condition
that the program must include 'Codeviz comments' (i.e., the embedded, comment-based syntax).
The runtime for the language parses a file, analyzing both Codeviz comments
and control flow keywords in the underlying language,
then generates one or more flowcharts, where the user, potentially,
specifies the names and destinations of each flowchart. Additionally,
users can interact with the generated flowcharts: for instance,
one of the components of the flowchart could represent a fairly complex helper function
that could be clicked to reveal another flowchart
that represents the helper function's algorithm.

For this first iteration, the computation process looks like this:

1. Parse a Java file into an abstract syntax tree (AST) using [JavaParser]
2. Parse this Java AST into an AST that represents a flowchart
3. Generate a flowchart based on the flowchart AST

### Errors

One syntax error a user might encounter involves indicating a condition check
before a statement that does not check a condition.
Another compile-time error would occur if the user indicates
that an `if`-`else` block should be represented in the flowchart,
but only adds Codeviz comments within _one_ of the `if` or `else` portions of the block.
Previously I figured this error would instead be a warning
because I thought (and still think) there might be a valid usecase
for not specifying a description for a branch;
but in most cases if you're documenting one branch,
you should probably document the other,
so I decided to consider it an error until a compelling usecase is presented.
I think these errors can sensibly be reported on the command line.

### Similar Projects

[code2flow] is another language in the domain of code documentation and visualization,
and is designed to make flowchart creation easy
by providing a C++/Java-esque interface for generating flowcharts.
Though charming, this language does not suit my ideal well
because it's not embedded in an existing language.

[Flowgen] is much more aligned with my idea&mdash;it's on GitHub,
and it's even associated with a [paper][Flowgen Paper]!
Flowgen works for C++ and addresses the problem much as I intend to;
however, the language is not entirely opt-in oriented
and thus includes _every_ `if` statement (and `for` loop) in flowcharts,
causing C++'s syntax to leak into the flowchart
when users do not provide a more human-readable description for the condition.
To prevent this leaking, Codeviz _only_ includes user-specified descriptions
in generated flowcharts, which has the beneficial side effect
of further enforcing comment documentation.


## Language implementation


[code2flow]: http://code2flow.com/
[Flowgen]: http://jlopezvi.github.io/Flowgen/index.html
[Flowgen Paper]: http://arxiv.org/pdf/1405.3240.pdf
[JavaParser]: http://javaparser.github.io/javaparser/
