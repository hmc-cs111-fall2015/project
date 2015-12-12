[jastadd]: http://jastadd.org/
[attrgrammar]: https://en.wikipedia.org/wiki/Attribute_grammar

# UnderLang

UnderLang is a small class project. It tries to make implementing the backend
of a simple language a simple task.
All you have to do is declaratively specify how to compute attributes
such as values or types,
and UnderLang will piece together the computations itself.
UnderLang also provides a few convenient methods of handling
much more complex tasks, such as implicitly rewriting the
abstract syntax tree. The user never has to worry about when
or how the actual computations and rewrites will take place.
Since UnderLang is implemented as a domain specific language within
Python, you also have access to Python's full power and libraries.

More specifically, UnderLang is a declarative, lazily-evaluated implementation
of [attribute grammars][attrgrammar] in Python 3.

## Comparison with JastAdd

UnderLang is _heavily_ influenced by [JastAdd][jastadd],
essentially implementing a subset of its features
(and not nearly as well!)
While JastAdd is capable of supporting actual industrial-strength
projects, UnderLang aims to be more of an easy-to-use hackpad.

JastAdd is an entirely new language built on top of Java.
Users declare types, as well as certain properties of attributes
such as whether they should be lazily evaluated.
These features are absolutely critical for a large, efficiently-running
project.

In comparison, UnderLang is just an ordinary, pure Python library.
It is dynamically typed, and the user doesn't have to specify
properties related to the computational details of attributes.
It is also implemented in a pretty small amount of code,
and in that way amenable to extension.

That said, if you _actually_ want to do something instead of just
messing around with somebody's bug-ridden, hastily put-together class
project, I would suggest you look into JastAdd. :)

## Requirements

UnderLang is a single file with no dependencies other than Python 3!

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



