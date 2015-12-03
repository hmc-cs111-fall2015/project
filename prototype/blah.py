from pyrsistent import pmap


# attribute
# subtree / local / global
# default / initial
# update / unify
# fixedpoint

# When you ask for a property:
#   If there's an initial value, the
#   initial value is computed.
#       The value is set to that.
#   If there's an equation, the result
#   of the equation is computed.
#       If there's a value already (initial)
#       this causes an update.
#       Otherwise, the value is just set to that.
#   If no value is set yet, then it is set to
#   the default.
#       No, I don't like that. Default should
#       just be the equation from the higher-up
#       class.
#   What about an 'output' function?
#   That is, otherwise I'm going to get metavars out
#   when I ask for the type.
#
#   Well. I guess that's actually totally fine.
#   Just have a different property that extracts something
#   from the type property.
#
#   In order to implement unification, it's very simple.
#   Start by giving an initial value of a metavar.
#   Create an update function that unifies.
#
#   Then, later equations will actually cause an update.
#

# SO I need a metavar system.

'''
Attribute
    -> Initial Equation
    -> Equation
    -> Update
    -> Getter
    -> Setter
For fixedpoint:
    +> Has an initial
    +> Has an equation (main definition)
    Getter:
        If iteration flag:
            Just give cached value
        If no iteration flag:
            Set iteration flag
            Calculate equation
            Set cached value to be that
            if result equals old value

            Set equation to be that
            Unset iteration flag
'''




class Num(Node):
    pass

class Add(Node):
    children = 'a b'

# Print
class Add(extend):
    @attribute
    def print(self):
        return "({} + {})".format(self.a.print, self.b.print)


class Num(extend):
    @attribute
    def print(self):
        return "{}".format(self.n)

# Value
class Add(extend):
    @attribute
    def value(self):
        return self.a.value + self.b.value

class Num(extend):
    @attribute
    def value(self):
        return self.n

#Lambda and such
class Lam(Node):
    children = 'var body'

class App(Node):
    children = 'func arg'

class Var(Node):
    pass

#Binding
class Expr(Node): pass
Expr << [Num, Add, App, Lam]
class Expr(extend):
    @subtree
    @default
    def binding(self):
        return pmap()

class Lam(extend):
    @subtree
    @fixedpoint
    def binding(self):
        return self.binding.set(self.var.name, self.var)

#Types
class Expr(extend):
    @update
    def type(self, current, new):


class Num(extend):
    @attribute
    def type(self):
        return int

class Add(extend):
    @attribute
    def type(self):
        self.a.type = int
        self.b.type = int
        return int

class App(extend):
    @unify
    def type(self):
        A, B = meta(2)
        unify(Func[A, B], )
        self.arg.type = A
        return B

class Lam(extend):
    pass






