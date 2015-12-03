from pyrsistent import pmap

class Num(Node, n=Value): pass

class Add(Node, a=Child, b=Child): pass




class Add(extend):
    def print(self):
        return "({} + {})".format(self.a.print, self.b.print)

class Num(extend):
    def print(self):
        return str(self.n)



class Add(extend):
    def value(self):
        return self.a.value + self.b.value

class Num(extend):
    def value(self):
        return self.n



class App(Node, children='func arg'): pass
class Lam(Node, children='var body'): pass
class Var(Node, values='name'): pass


class Expr(Node): pass
Expr << Num, Add, App, Lam

class Expr(extend):
    @subtree
    @initial
    def scope(self):
        return pmap()

class Lam(extend):
    @subtree
    @fixedpoint
    def scope(self):
        return self.scope.set(self.var.name, self.var)

class Var(extend):
    def binding(self):
        return self.scope[self.name]


class Expr(extend):
    def value2(self, env):
        return self.value

class Var(extend):
    def value2(self, env):
        return env[self.name]

class App(extend):
    def value2(self, env):
        return self.func.value2(env)(self.arg.value)

class Lam(extend):
    def value2(self, env):
        def func(arg):
            env2 = env.set(self.var.name, arg)
            return self.body.value2(env2)
        return func


