from abc import ABCMeta, abstractmethod
from functools import wraps
class Interpreter(metaclass=ABCMeta): pass

# Ignore this. I'm considering parsing a solved problem
# for the purposes of this project, so it's just a dummy.

def parse(t):
    def run(s):
        if s == "1 + 2":
            return t.output(t.add(t.num(1), t.num(2)))
        elif s == r"\x -> (1 + 0) + x":
            return t.output(t.lam(lambda x: t.add(  t.add(t.num(1), t.num(0)), x  )))
    return run

# The idea of this project basically ends up being
# manipulating code with the goal of extending languages.
# In other words, the whole point is "Write easily, externally modifiable DSLs."
# So I'm actually making a DSL framework, of sorts.

# The first problem to tackle is the expression problem.
# Easy, right?
# While doing this I accidentally reinvented the Visitor pattern
# and was instantly horrified with myself. But anyways, onwards!
# As the paper "Extensibility for the Masses" suggests,
# I am using object algebras, which I'll now show you how they work.

# Here's a super simple example of a DSL.
# It has numbers and addition, and that is all.
# We define an Expr class that represents an "Interpreter"
# of this DSL. An Interpreter knows how to construct
# value bottom-up.
# It might produce any kind of value:
# Perhaps the number you get when you evaluate it,
# perhaps a pretty-printer string.
# All it has to know is how to make that kind of value from
# a number, and how to make that kind of value from
# two values (added).
class Expr(Interpreter):
    # actions = ['num', 'add']
    @abstractmethod
    def num(self, a): pass
    @abstractmethod
    def add(self, a, b): pass

    @classmethod
    def output(self, x):
        return x

# Here's an implementation that evaluates to a number.
class EvalExpr(Expr):
    def num(self, a):
        return a
    def add(self, a, b):
        return a + b

# Here's an implementation that evalutes to a string representation.
class PrintExpr(Expr):
    def num(self, a):
        return str(a)
    def add(self, a, b):
        return "({} + {})".format(a, b)

# Here's how you actually interpret stuff.
def expr1(out):
    return out("1 + 2")
def expr2(out):
    return out(r"\x -> (1 + 0) + x")

# You generally chain interpretations;
# for example here, first you parse the string,
# and then you interpret it.
# We'll see more chaining later on.
print(expr1(parse(EvalExpr() )))
print(expr1(parse(PrintExpr() )))

# Now that we have a starting point, let's try to extend it.
# We'll add some new syntax: lambda calculus Functions.
# We need everything we used to, but now we also need
# to deal with lambdas and function application.
class LC(Expr):
    @abstractmethod
    def lam(self, body): pass
    @abstractmethod
    def app(self, a, b): pass

# It's super easy to reuse the implementation for just Exprs,
# and only add the new things to it.
class EvalLC(EvalExpr, LC):
    def lam(self, body):
        return body
    def app(self, func, arg):
        return func(arg)

# However, with printing, we encounter a problem.
# As this is implemented, in order to print a lambda, we need to know
# how deep it is, because we name the variables x0, x1, ... based on
# how deeply nested it is.
#
# One way to get this top-down information in a bottom-up system like we
# have is to return functions from context -> result. Here context is
# just depth, and result is a final string.
#
# We run the last function on a default context (here, 0).
# That is done by the `output` function, which finalizes the last result.
#
# This WORKS, but it loses on expressivity. We have to redefine num and
# add, even though we already made printers for them! Because those printers
# return strings, and we need int -> string functions! BAD!!
class PrintLC(LC):
    def num(self, a):
        return lambda n: str(a)
    def add(self, a, b):
        return lambda n: "({} + {})".format(a(n), b(n))
    def lam(self, func):
        return lambda n: r"\x{} -> {}".format(n, func(lambda _: r"x{}".format(n))(n+1))
    def app(self, func, arg):
        return lambda n: "({})[{}]".format(func(n), arg(n))
    def output(self, x):
        return x(0)

print(expr2(parse(EvalLC() )))
print(expr2(parse(PrintLC() )))

# So how do we solve this problem? Well, num and add were basically just dummy
# implementations. Take a string s, and turn it into lambda n: s.
# The way to solve this problem is to recognize that we can make these
# dummy implementations follow a set pattern. Then we'll be able to abstract that out.

class PrintLC2(PrintExpr, LC):
    def wrap(self, s):
        return lambda n: s
    def unwrap(self, ctxt2s):
        return ctxt2s(0)

    def num(self, a):
        return self.wrap(super().num(a))
    # Big problem here: Unwrap uses the wrong depth. Add isn't propagating
    # information to its children.
    # So, somehow we need to know what things need to propagate to children.
    # (I.e., anything that has children)
    # How to establish that information is a work-in-progress
    def add(self, a, b):
        return self.wrap(super().add(self.unwrap(a), self.unwrap(b)))

    def app(self, func, arg):
        return lambda n: "({})[{}]".format(func(n), arg(n))
    def lam(self, func):
        return lambda n: r"\x{} -> {}".format(n, func(lambda _: r"x{}".format(n))(n+1))

    def output(self, func):
        return super().output(self.unwrap(func))

# We can auto-generate something of that form. So this is the best version.
# PrintLC3 "lifts" the implementation of PrintExpr into its own domain
# using wrap and unwrap, and then adds the truly new implementations.
class PrintLC3(Lift(PrintExpr), LC):
    def wrap(self, s):
        return lambda n: s
    def unwrap(self, ctxt2s):
        return ctxt2s(0)

    def app(self, func, arg):
        return lambda n: "({})[{}]".format(func(n), arg(n))
    def lam(self, func):
        return lambda n: r"\x{} -> {}".format(n, func(lambda _: r"x{}".format(n))(n+1))

# Other than Lifting, we also often want to Transform.
# In this case, we are simply adjusting the AST.
# We take in another interpreter (t) to continue the evaluation with.
# Again, a lot of the basic stuff just involves wrapping and unwrapping
# values, and passing them on to the t interpreter.
#
# DontAddZero takes things of the form A + 0 or 0 + A and turns them into
# just A. It applies this all the way through the tree.
# Values are represented as (value, trueIfThisValueIsZero).
# (This is somewhat unnecessary but illustrates the point.)
class DontAddZero(Transform(LC)):
    def wrap(self, val):
        return (val, False)
    def unwrap(self, val):
        return val[0]

    def num(self, a):
        return (self.t.num(a), a == 0)

    def add(self, a, b):
        if a[1]:
            return b
        elif b[1]:
            return a
        else:
            return self.wrap(self.t.add(self.unwrap(a), self.unwrap(b)))

print(expr2(parse(DontAddZero(PrintLC() ))))

# But, even that code is unncessarily complicated. We would really like
# to be able to automatically generate wrap and unwrap, and perhaps more as well,
# at least for simple scenarios.
# Wrap and unwrap just essentially hold the pattern matching context,
# so if we can auto-generate them, we can do something like this:
A, B, C = Pattern.metavars('A B C')
DontAddZero = Transformer(LC, 0 + A >> A, A + 0 >> A)
RightAssociate = Transformer(LC, (A + B) + C >> A + (B + C))

# Finally we're really starting to see a DSL.
# Unfortunately, this is as much as I've got, and several crucial parts
# above aren't even implemented, so only some of this can actually run.



