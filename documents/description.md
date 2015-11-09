# Project description and plan


## Motivation

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

Not only would this solution help anyone (i.e., programmers and non-programmers alike)
in understanding code, but it also reduces the effort necessary to produce 'good' documentation:
a Codeviz program shows up as syntax in an existing programming language,
so programmers don't have to venture too far from the code itself to generate the flowcharts.
It's primarily for this reason, and the fact that programmers might not want
every implementation detail to leak into the flowcharts&mdash;such that
there should be some way to indicate what _should_ appear on the flowcharts&mdash;that
a DSL is an appropriate vehicle for this solution.
Perhaps optimistically, the language will also compel programmers
to write more high level, commented, and documented code
because doing so is a sort of requirement of the language.


## Language domain

Codeviz lives in the domain of code documentation and visualization,
which is important for the reasons prescribed above.
Documentation helps people understand the purpose or high level control flow of some code
without necesarilly requiring knowledge of the underlying implementation;
and visualization is sometimes a better medium than pure text documentation.

[code2flow] is another language in the domain, and is designed to make flowchart creation easy
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


## Language design

Codeviz illustrates the control flow of some code by means of a flowchart.
A valid Codeviz program is a valid program in the underlying language
with the additional trait that the program must include 'Codeviz comments'
(i.e., the embedded, comment-based syntax). The runtime for the language compiles a file,
parsing both Codeviz comments and control flow keywords in the underlying language,
and then generates one or more flowcharts, where the user, potentially,
specifies the names and destinations of each flowchart. Additionally,
users can interact with the generated flowcharts: for instance,
one of the components of the flowchart could represent a fairly complex helper function
that could be clicked to reveal another flowchart
that represents the helper function's algorithm.
Abstract syntax trees will be helpful in both parsing the underlying language
and maintaining a flowchart generation standard.

One syntax error a user might encounter involves indicating a condition check
before a statement that does not check a condition. Alternatively,
a user would encounter a compile-time warning if the user indicates
that an `if`-`else` block should be represented in the flowchart,
but only adds Codeviz comments within _one_ of the `if` or `else` portion of the block.
Albeit the flowchart would still be generated since it's completely appropriate
for only one portion to contain Codeviz comments,
the user should still be notified that one would _typically_ expect
_both_ portions to contain Codeviz comments.
Since, in this case, a valid flowchart could still be generated,
users should be able to dismiss warnings so they do not (re)appear.
I think these warnings and errors can sensibly be reported on the command line.


## Example computations

Computations in Codeviz are pretty homogeneous: parse the Codeviz comments
and control flow keywords into an abstract syntax for a flowchart,
then use a mapping from the flowchart abstract syntax to a flowchart creation API
to generate the flowchart. The file parsing step might involve
parsing the underlying language into some abstract syntax,
and then mapping this syntax to the flowchart abstract syntax.


[code2flow]: http://code2flow.com/
[Codeviz]: https://github.com/JustisAllen/Codeviz
[Flowgen]: http://jlopezvi.github.io/Flowgen/index.html
[Flowgen Paper]: http://arxiv.org/pdf/1405.3240.pdf
