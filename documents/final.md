## Introduction

### Motivation

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

### Domain

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


## Language Design




## Language Implementation




## Evaluation




[code2flow]: http://code2flow.com/
[Codeviz]: https://github.com/JustisAllen/Codeviz
[Flowgen]: http://jlopezvi.github.io/Flowgen/index.html
[Flowgen Paper]: http://arxiv.org/pdf/1405.3240.pdf
