[jastadd]: http://jastadd.org/
[taglessfinal]: http://okmij.org/ftp/tagless-final/course/
[descriptor]: https://docs.python.org/3.5/howto/descriptor.html

# Under-Lang

## Introduction

UnderLang is a language that intends to be a scratchpad for
doing the implementations of languages.
It is almost declarative and low-boilerplate,
and handles as much of the computational details as it can for you.
Ideally, you don't have to do much more than code the very
essence of what it is you want to implement.

## Language Design Details

_How does a user write programs in your language (e.g., do they type in commands, use a visual/graphical tool, speak, etc.)?_

UnderLang is an internal DSL in Python. Programs written using UnderLang are for
the most part normal Python code organized and manipulated by UnderLang's constructs.
However, UnderLang does most of the heavy lifting, and hides these
computational details from the user.

Although the user is actually writing normal Python code,
they will hopefully  ever need to write simple,
short computations. The goal is that using UnderLang
will feel like declarative programming.


_How does the syntax of your language help users write programmers more easily than the syntax of a general-purpose language?_

UnderLang does many sophisticated and interdependent computations underneath the hood.
Occasionally with bugs, but, uh, let's ignore that.

In contrast, UnderLang's syntax is mostly declarative, and extremely concise.
The user gets to think more about what they want their language to be,
and less about how exactly the details of those computations should take place.

_What is the basic computation that your language performs (i.e., what is the computational model)?_

Ultimately, UnderLang is an implementation of Knuth's *attribute grammars*, along with
several of the extensions pioneered by [JastAdd][jastadd]. An attribute grammar
essentially describes the flow of data through an abstract syntax tree.
Nodes have attributes, that depend on other attributes and nodes, that are computed
on-demand.

_What are the basic data structures in your DSL, if any? How does a the user create and manipulate data?_

Thus, there are two basic data structures that a user interacts with.

1. Nodes

2. Attributes

A *Node* is a node in the abstract syntax tree. Typically, it corresponds fairly
directly to an element of the actual syntax of the user's language.

Nodes have *Attributes*. An Attribute can be basically anything - a value,
a type, a string representation for printing. The user simply tells UnderLang how
to compute it, usually using the values of several different Attributes.

_What are the basic control structures in your DSL, if any? How does the user specify or manipulate control flow?_

Almost all of the control flow is implicit, since UnderLang aims to be declarative.
The user specifies how to compute attributes, but never actually does that
themselves.
They simply request the values they need, and UnderLang will supply them.

A user can get some extra control
by specifying special features on Attributes, such as default or initial
values. They also control which nodes do which computations,
However, the general idea is that the user _doesn't_ have to deal with control flow.

_What kind(s) of input does a program in your DSL require? What kind(s) of output does a program produce?_

UnderLang makes no attempt to actually construct an abstract syntax tree from
text, leaving that job to standard parsing techniques.
Given an abstract syntax tree, UnderLang essentially provides the
underlying implementation of the language.
In that sense, UnderLang's output is the same as that of an interpreter,
where interpreter is used loosely to mean any kind of computations
done using an AST.


_Error handling: How can programs go wrong, and how does your language communicate those errors to the user?_

Most errors will simply be standard Python errors.
In the interest of having as little boilerplate as possible,
UnderLang allows quite a lot.
This means that actual errors in the UnderLang portion of the
code mostly crop up as misinterpretations.
For example, since Attributes don't have to be declared,
a misspelling simply means you're referencing a different Attribute.
Thus, like Python itself, UnderLang can be considered lacking
in what kinds of errors it can actually catch.


_What tool support (e.g., error-checking, development environments) does your project provide?_

As an internal DSL, UnderLang can leverage any tools that are used for normal
Python development.
However, since UnderLang is so lenient,
and because it makes heavy use of relatively arcane features of
Python under the hood, simple static analysis tools might not end up
providing much information about an UnderLang program.


_Are there any other DSLs for this domain? If so, what are they, and how does your language compare to these other languages?_

The domain of "writing language implementations" is extremely broad, so there are
many languages in the .
However, the most relevant to UnderLang is without a doubt [JastAdd][jastadd].
The core philosophy and computational models are almost exactly the same.
There are of course differences.
The simplest are that
JastAdd is not an internal DSL, but instead more like a preprocessor;
and that UnderLang is infinitely slower.

The more important differences, in terms of language design and use,
mostly stem from the fact that JastAdd uses Java as its base general-purpose language,
while UnderLang uses Python.
Therefore, JastAdd is statically typed, while UnderLang is dynamic.
JastAdd also has very slightly more required annotations than UnderLang,
in terms of boilerplate,
as well as declaring and specifying the special properties of Attributes.
The tradeoff is that, as previously mentioned, UnderLang is perfectly
happy to run with logical errors that might be caught by a static system.


## Examples & Usage

A simple example is just a straightforward numerical calculator.

### Nodes

Node types are defined concisely, simply by listing the names
of their children.

```python
from underlang import Node
from operator import add, mul

class Num(Node):
    n

class Binop(Node):
    op
    a
    b
```

### Attributes

Then, calculations are done by adding attributes to these node types,
and then querying them.

```python
@Num.value
def val(num):
    return num.n

@Binop.value
def val(bop):
    return bop.op(bop.a, bop.b)

assert Binop(add, Num(6), Binop(mul, Num(-1), Num(5))).value == 1
```

All computations are lazily evaluated and cached, so adding extra
attributes won't make UnderLang do more work.

UnderLang has some far more powerful features to offer as well.
Let's look at a more complicated example, a context free grammar.

```python
from underlang import *

class Grammar(Node):
    productions

class Production(Node):
    ntrm
    products

class Nonterminal(Node):
    name
```

### Remotely Evaluated Attributes

When the AST is first constructed, every nonterminal
will be a different object, even if they have the same name.
So we'll define a _canonical_ attribute on Nonterminals,
that all point to one specially chosen one of the same name.

The easiest way to do that is to use the `root` attribute,
which comes predefined. Every node in the same AST shares
the same value for its root attribute, so you can use the
root as a global environment.

It is intended that in the future, you could do similar things
with the `local` attribute. The difference is that changes made
to the local attribute would only propagate down the subtree
they came from, rather than being global.
However, the local attribute is not yet implemented.

So, assuming our root has a `lookupNtrm` dictionary:

```python
@Nonterminal.canonical
def lookup(ntrm):
    return ntrm.root.lookupNtrm[ntrm.name]
```

Now, how do we actually create such a `lookupNtrm` dictionary?
Usually, the value of attributes are computed by the node
that owns them. However, here, we will make use of remotely
calculated attributes. Each Nonterminal will add itself into
the root's lookupNtrm.

We just specify an initial starting point on the root,

```python
Root.lookupNtrm(initial = lambda root: dict())
```

and then

```python
@Nonterminal.root.lookupNtrm
def add(ntrm, lookupNtrm):
    # setdefault only sets the value if it isn't already set
    lookupNtrm.setdefault(ntrm.name, ntrm)
```

When first accessed, the lookupNtrm dictionary will
go and aggregate the modifications specified by all
the Nonterminals, so we'll have a complete table whenever we need it.

If you are curious, here's how you could implement the Root
node all by yourself:

```python
class Root(Node):
    child

@Node.root
def root(node):
    if node.parent is None:
        return Root(node)
    else:
        return node.parent.root
```

You'll notice that nodes also have convenient access to their parent in the AST :)

### Circular attributes

Suppose we want to see what nonterminals we could ever possibly
produce. We define a `reachable` attribute to calculate this,
assuming we already know the other nonterminals that can produce it
(it's `predecessors`.)

A nonterminal is reachable if any of its predecessors is reachable.
So we just write that.

```python
@Nonterminal.reachable
def reach(ntrm):
    if ntrm is ntrm.canonical:
        return any(p.reachable for p in ntrm.predecessors)
    else:
        return ntrm.canonical.reachable
```

Now, there should be a problem with this. And that is,
this definition can become circular, because nonterminals can
point to each other.

Reachability is normally calculated using a closure algorithm,
or fixed-point iteration. That is, you fix an initial value,
and then you repeat the calculation over and over again until it
stabilizes. It turns out that this can solve a lot of
circular problems, so UnderLang (like JastAdd) falls into
fixed-point iteration if it detects a cycle.

You just need to specify a starting point, so here's the
true version:

```python
@Nonterminal.reachable(initial = lambda n: False)
def reach(ntrm):
    if ntrm is ntrm.canonical:
        return any(p.reachable for p in ntrm.predecessors)
    else:
        return ntrm.canonical.reachable
```

Predecessors can actually be implemented in the same way that
`lookupNtrm` was. First, we specify a starting point:

```python
Nonterminal.predecessors(initial = lambda n: set())
```

Then, we just have each production hook up the
nonterminal with its predecessors.

```python
@Production.products.predecessors
def add(production, predecessors):
    predecessors.add(production.ntrm.canonical)
```

Notably here, products is actually a whole list of nodes.
That's fine; the add procedure is just done to each individually.

There is the slight note that
because we're doing canonical stuff, we want to make
sure that we copy any predecessors we get over to the
canonical nonterminal.

```python
@Nonterminal.canonical.predecessors
def add(ntrm, pred):
    pred.update(ntrm.predecessors)

g = Grammar([
        Production(Nonterminal('A'), [Nonterminal('B')]),
        Production(Nonterminal('B'), [Nonterminal('D')]),
        Production(Nonterminal('C'), [Nonterminal('B')])
    ])
g.productions[2].ntrm.canonical.reachable = True
assert g.productions[0].ntrm.reachable == False
assert g.productions[1].ntrm.reachable == True
assert g.productions[2].ntrm.reachable == True
```

## Langauage Implementation

_What host language did you use (i.e., in what language did you implement your DSL)? Why did you choose this host language (i.e., why is it well-suited for your language design)?_

Python. I know it well. It's also well-known for being an easy-to-use scripting
language, and it's that sort of experience I want to provide.

_Is yours an external or an internal DSL (or some combination thereof)? Why is that the right design?_

Internal DSL. Because the calculations that happen on top of UnderLang
need to be arbitrarily powerful.

_Provide an overview of the architecture of your language: front, middle, and back-end, along with any technologies used to implement these components_

Front: Python,

_"Parsing": How does your DSL take a user program and turn it into something that can be executed? How do the data and control structures of your DSL connect to the underlying semantic model?_

I would typically claim that, as an internal DSL, the parsing is only minimal. However,
UnderLang makes incredibly heavy usage of Python metaprogramming techniques
in order to subvert the natural organization of the language.
Most UnderLang programs would just utterly confuse Python with
undefined variable references and the like if UnderLang wasn't
operating as middleware between the user and Python proper.

The general approach is that everything is multiply-layered.
The actual contents of the Node classes are created by the users,
so what UnderLang has control over is actually the Node _metaclasses_.
By subclassing Python's `type`, you can make you own kinds of classes,
that behave in their own special ways, and that is what UnderLang does.

Similarly, Attributes play a double role. To an actual instance of
of a Node, Attributes appear to be straightforward values.
(Well, actually, they appear to be cached properties, since what
seems to be a bare field access actually runs some computations.)
However, when they are accessed by the Node's _class_, such as in

```python
@Num.value
def val(num):
    ...
```

they behave quite differently, instead setting up the computational functions
to be used by the instances. This behavior is implemented using Python's
[object descriptors.][descriptor] I call these objects Proxies; you can imagine
them to be much more complicated properties.

Moreover, you can access one of these attributes _without ever having defined it in the first place_,
which is because the Node metaclass will create them on demand.
Furthermore, you can create them in superclasses after they are created in subclasses,
or vice versa, and the attributes will still behave like subclasses of each other.

That allows you to do things like this:

```python
@Node.root
def root(node):
    if node.parent is None:
        return Root(node)
    else:
        return node.parent.root
```

which now affect all Node kinds, unless explicitly overwritten.

_Intermediate representation: What data structure(s) in the host language do you use to represent a program in your DSL?_

In general, it is a network of Nodes, which are filled with Attributes.

However, the data layout is also a bit strange. The actual Attribute class stores the
data for all of the Nodes that use it, rather than storing the data on the
Nodes. This is for two reasons. One is to avoid polluting the user-facing
namespace, which is the one on the Nodes, as much as possible.

The other is that this opens up the possibility of implementing Attributes
inside of Nodes somewhat like the functions inside of classes/type classes
that is seen in the [tagless final][taglessfinal] representation of syntax.
It's basically a dual to the AST, and it is easily extensible in different ways.

The most compelling, beyond a type-theoretic perspective, is that you can
apply default lifting transformations to old code you want to
 extend, while leaving the old code alone.

For example, suppose you were going to switch from a `value` attribute that
was static to one that required an environment.
Now, what you should _actually_ do is use the `local` node feature, similar to
the `root` feature, but I haven't actually implemented that.

But something else you could do would be to take the old Attribute
and automatically wrap its calls in lift/unlift statements that
just passed environment information down. Then you'd only have
to change the parts that actually use the environment, like variables.

This is possible because, essentially, you add in a new Attribute that
uses the old one in its background. And that can be done because the Attribute
is not actually tied to using the Node directly.

Have I actually implemented this? No, of course not.

## Evaluation: Provide some analysis of the work you did. In particular:

_How "DSL-y" is your language? How close or far away is it from a general- purpose language?_

It's internal. But I think it is pretty darn DSL-y for that.
At least, I certainly put in the effort to remove Python's host flavor
as much as studently possible.

_What works well in your language? What are you particularly pleased with?_

The cleanliness of the syntax looks really good to me. I'm also pleased with how some
short (and I hope, readable) most things are to implement.

_What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive? Are there more features you'd like to have? Does your current implementation differ from your larger vision for the language?_

There are many, many things that it would be convenient to have that I have left
to implement. I'm also aware of some bugs in what I have implemented, although
most people wouldn't run into them. Additionally, it's total crap at error reporting,
which is a serious usability issue.

_Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests? Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?_

Evaluation-wise, mostly what I got from others was just the general
idea that for a domain that really takes quite a lot of mental effort
to work in, the main weapon I have to create accessibility is
trying to make things declarative.
I made that and low-overhead syntax my main goals.
I had to drop extensibility as a priority,
which had been my original one, because
extensibility is worthless without usability.

But, generally, I did _not_ make effective use of the advantages of the studio model.
I'm not properly sure how I could have, either.

This project felt to me like almost all of
the work was theoretical. A DSL is a way for a person to communicate an idea,
and in particular, communicate it specifically enough for it to be implemented.
I'm still not even 100% sure what the means for language implementation.
How _would_ I describe a language with pen and paper? I think what I've
produced might not be too far off from that, but it's hard to say.

I think that it might even be the case that this project ended up
being _too_ languagey. That sounds weird, but it certainly wasn't
implementation heavy. It's just that the language and communication
type ideas were more abstract than even the level of syntax.

That was terrible, because it was very difficult for me to talk
to other people about it. Even the couple of times that I did make something
concrete to show, that's mostly what it was - because I knew I was going to
completely scrap it by the next week anyway.

It felt pretty much like a math problem, where there was literally
nothing to show until the end when all I had to do was write it up.
I wish that I had reached that point a couple of weeks sooner. Or at least one.

I don't know if I would call the project too ambitious, but it was
definitely too abstract for too long to make good use of the studio model.

