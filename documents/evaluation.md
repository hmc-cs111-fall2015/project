# Preliminary evaluation

Everything is working as expected which is good.
I'm particularly pleased with the external libraries I'm using
to parse the input Java file and write the [DOT] file that describes the flowchart:
[JavaParser] and [graphviz4j], respectively. For the most part,
the current implementation accomplishes exactly the user experience
at which I'm currently aiming. It could probably be better documented though:
both in terms of usage and commented code.

As for language evaluation, I haven't really used too much of either of the proposed tools.
To evaluate the _design_, I proposed using the language
to generate flowcharts that represent solutions for problems in CS 5 or 60,
but instead I opted to use the language in the in the language implementation,
which has actually been very enlightening. In particular,
I realized that flowcharts might not all end at the same point,
so both branches of a conditional are not required to converge,
and that text for each node might not fit in a single end-of-line comment,
so there should be some way to indicate that the text of an end-of-line comment
is a continuation of the text from the previous comment.
To evaluate the _implementation_, I essentially proposed ease of extensibility,
but I haven't been consistently thinking about it until recently.
I think parsing is pretty straightforward as far as extensibility
since the flowchart abstract syntax is separate from the parser:
if anyone wants to parse a language into the abstract syntax,
they use whatever parser they want to parse the comments and just instantiate and connect the nodes.
One limiting aspect of the parser is that I think its interface needs to be in Java
so that the user can access the flowchart abstract syntax.
One way I might alleviate this rigidity in the future
is to describe the flowchart abstract syntax with [Protocol Buffers];
then, someone could parse a language into the flowchart abstract syntax from essentially any language,
and send it to a separate program in another language
that knows how to create a flowchart from the abstract syntax.
Currently, writing a program that creates a flowchart from the flowchart abstract syntax isn't accessible
since the flowchart creation part is (again currently) baked into the abstract syntax
and there's no way to use a different implementation.

Since I stated in my project plan, "I'll deem Codeviz a success if users can generate simple,
`if`-`else`-based flowcharts without much effort," I think I'll focus on parsing and rendering `if` statements,
then refactor the imlementation to be more modular and language independent. More specifically,
probably translating the flowchart abstract syntax to Protocol Buffers,
then splitting the parsing and flowchart creation into separate programs
which appropriately produce and consume a protocol buffer. In this way,
I demonstrate how to use the flowchart abstract syntax.
One thing I still need to consider is how these components should interact in the source/project structure.
The true backbone of the language is the flowchart abstract syntax; everything else can be swapped out.

[DOT]: http://www.graphviz.org/content/dot-language
[graphviz4j]: https://github.com/shevek/graphviz4j
[JavaParser]: https://github.com/javaparser/javaparser
[Protocol Buffers]: https://developers.google.com/protocol-buffers/?hl=en
