## Introduction

Trying to understand someone else's code&mdash;especially
at a large scale&mdash;can be an intimidating, difficult, and overwhelming task:
having to distinguish keywords and follow control flow in raw source code can be tiring,
even if the code is well-commented. Documentation can ease this process,
but the norm for documentation is text-based, which isn't always
the best or most accessible way to express an idea;
and there aren't many popular tools for making documentation that _is_ more accessible.

[Codeviz]&mdash;short for "Code Visualizer"&mdash;addresses this problem
by providing a language that makes it easier for programmers to create flowcharts
that represent the control flow of their code,
offering a more visually- and spatially-appealing representation of code:
normally code-based algorithms are expressed in 1D,
but with flowcharts, these algorithms can be expressed in 2D.

Not only does this solution help anyone (i.e., programmers and non-programmers alike)
in understanding code, but it also reduces the effort necessary to _produce_ documentation:
a Codeviz program shows up as comments in an existing programming language,
so programmers don't have to venture far from the code itself to generate the flowcharts.
It's primarily for this reason, and the fact that programmers might not want
every implementation detail to leak into the flowcharts&mdash;such that
there should be some way to indicate what _should_ appear on the flowcharts&mdash;that
a DSL is an appropriate vehicle for this solution.
Perhaps optimistically, the language will also compel programmers
to write more high level, commented, and documented code
because doing so is a sort of requirement of the language.


## Language Design

Codeviz illustrates the control flow of some code by means of a flowchart.
A valid Codeviz program is a valid program in the underlying language
(Java for this first iteration) with the additional condition
that the program must include 'Codeviz comments'
(i.e., the embedded, comment-based syntax).
As stated above, this syntax offers an accessible way (like Javadoc)
to generate documentation without venturing far from the code.
A program does not accept any input but produces a Graphviz [DOT] file representing a flowchart as output.
The basic data structures are flowchart nodes
which users create using Codeviz comments:
`//$` generates a `Process` node, `//X` generates a `Terminal` node,
and `//?` (along with an `if` statement) generates a `Decision` node.
Currently, users can describe but not manipulate control flow:
there is no notion of nodes that are conditionally included in a flowchart.

### Errors

An error is reported on the command line if:

* the Codeviz program/input file
  * doesn't compile in the underlying language.
  * contains no Codeviz comments.
  * doesn't have a "main" method.
* the user indicates that an `if` statement should be represented in the flowchart,
but does not add Codeviz comments in the `if` portion.

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


## Language Implementation




## Evaluation




[code2flow]: http://code2flow.com/
[Codeviz]: https://github.com/JustisAllen/Codeviz
[DOT]: http://www.graphviz.org/content/dot-language
[Flowgen]: http://jlopezvi.github.io/Flowgen/index.html
[Flowgen Paper]: http://arxiv.org/pdf/1405.3240.pdf
