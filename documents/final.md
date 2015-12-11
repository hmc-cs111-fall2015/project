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


## Example Program

### Java File

```java
import java.util.Scanner;
import java.util.stream.IntStream;

public class Demo {
  public static void main(String[] args) {
    Scanner reader = new Scanner(System.in);

    //$ Get a positive integer from the user
    System.out.print("Enter a positive integer: ");
    int n = reader.nextInt();

    //$ Prompt user for sum or product
    System.out.printf("Would you like the sum of the positive integers up to %d? (y/n) ", n);

    //? Sum selected?
    if (reader.next().equals("y")) {
      //X Compute and print sum
      System.out.printf("The sum is %d.\n",
          IntStream.rangeClosed(1, n).sum());
    } else {
      //X Compute and print product
      System.out.printf("The product is %d.\n",
          IntStream.rangeClosed(1, n).reduce(1, (a,b) -> a * b));
    }
  }
}

```

### Output Flowchart

![Demo Flowchart]


## Language Implementation

Codeviz is an external DSL whose syntax is embedded within a targetted language
for the purpose of making the tool accessible and easy to use:
programmers don't have to venture far from the code itself to generate the flowcharts.
The DSL must be external so that it can parse the comments
which are ignored by the underlying language's compiler.
I chose Java as the host language because I wanted to target Java
as the first language that Codeviz supports&mdash;since the language is currently very popular,
and I want to maximize impact. The best parser I found for parsing Java
is written in Java, so I figured I'd just use Java.

For this first iteration, the computation process looks like this:

1. Parse a Java file into an abstract syntax tree (AST) using [JavaParser]
2. Translate this Java AST into an AST that represents a flowchart
3. Generate a DOT file with [graphviz4j] (a Java library for writing DOT files)
that represents a flowchart based on the flowchart AST

The flowchart abstract syntax uses a foundational abstract class `FlowchartNode`
(originally just `Node` but changed due to a name conflict with JavaParser's `Node` class)
which represents the smallest component of a flowchart
that has any number of arrows entering and exiting.
The concrete classes that stem from `FlowchartNode` are `Process`, `Decision`, `Terminal`, `Connector`,
each of which has a distinct meaning and shape in a flowchart
and each of which (if applicable) points to the subsequent node(s).
`Process` and `Connector` extend the abstract class `SingleExitNode`
(which extends `FlowchartNode`) because both have a notion of a single `nextNode`
to which they're (potentially) linked; the abstract class centralizes methods for setting and retrieving this node,
and provides a name for (and therefore easy reference to) the trait.

The DOT file generation is currently coupled with the flowchart abstract syntax:
each `FlowchartNode` 'knows' how to render itself via a method,
so after the flowchart AST is built, the 'rendering' method of the first node is called
and each node calls the rendering method for any nodes to which it's linked.


## Evaluation




[code2flow]: http://code2flow.com/
[Codeviz]: https://github.com/JustisAllen/Codeviz
[Demo Flowchart]: https://github.com/JustisAllen/Codeviz/blob/master/example/Demo.jpg
[DOT]: http://www.graphviz.org/content/dot-language
[Flowgen]: http://jlopezvi.github.io/Flowgen/index.html
[Flowgen Paper]: http://arxiv.org/pdf/1405.3240.pdf
[graphviz4j]: https://github.com/shevek/graphviz4j
[JavaParser]: https://github.com/javaparser/javaparser
