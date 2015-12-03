# Extendo classes

class ExtendMeta(type):
    @classmethod
    def __prepare__(mcl, name, bases):
        return dict(globals()[name].__dict__)
    def __new__(mcl, name, bases, namespace):
        if name is None:
            return super().__new__(mcl, 'extend', bases, namespace)
        else:
            assert bases[0].__name__ == 'extend'
            cls = globals()[name]
            for key, val in namespace.items():
                setattr(cls, key, val)
            excludeBases = set(cls.__bases__)
            # We assume that extend is the first base class ...
            bases = tuple(b for b in bases[1:] if b not in excludeBases)
            cls.__bases__ = bases + cls.__bases__
            return cls

def extend(_, cls):
    class BoundExtendMeta(type):
        @classmethod
        def __prepare__(mcl, name, bases):
            return dict(cls.__dict__)
        def __new__(mcl, name, bases, namespace):
            if name is None:
                return super().__new__(mcl, 'extend', bases, namespace)
            else:
                assert bases[0].__name__ == 'extend'
                for key, val in namespace.items():
                    setattr(cls, key, val)
                excludeBases = set(cls.__bases__)
                # We assume that extend is the first base class ...
                bases = tuple(b for b in bases[1:] if b not in excludeBases)
                cls.__bases__ = bases + cls.__bases__
                return cls
    return BoundExtendMeta(None, (), {})

extend = ExtendMeta(None, (), {'__new__': extend})

class blah: pass

class A(blah):
    a = 6
a=A()

print(dir(A))
print(A.a)
print(a.a)

class _(extend(A)):
    a = -2
    b = 1

print(dir(A))
print(A.a, A.b)
print(a.a, a.b)

class B:
    b = 25
    x = 70

class _(extend(A), B):
    pass

print(dir(A))
print(isinstance(a, B))
print(A.a, A.b, A.x)
print(a.a, a.b, a.x)

class NodeMeta(type):
    extend = property(extend)

class Node(metaclass=NodeMeta):
    pass

class A(Node):
    a = 2
print("MAGIC!", A.a)
class _(A.extend):
    a = 5
    b = 9
print(A.a, A.b)

class A(extend, B):
    c = 10

print(A.a, A.b, A.c)

# Utility

class Namespace(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, val):
        self[attr] = val
    def __delattr__(self, attr):
        del self[attr]

# attribute

class Field:
    def __init__(self, name, equation=None, initial=None, update=None):
        self.name = name
        self._equation = equation
        self._initial = initial
        self._update = update

    def _copy(self, **setAttrs):
        cp = Field(self.name, self._equation, self._initial, self._update)
        for attr, val in setAttrs.items():
            setattr(cp, attr, val)
        return cp

    def equation(self, equation):
        assert self._equation is None
        return self._copy(_equation = equation)
    def initial(self, initial):
        assert self._initial is None
        return self._copy(_initial = initial)
    def update(self, update):
        assert self._update is None
        return self._copy(_update = update)

    def _data(self, obj):
        if self.name not in obj.__dict__:
            obj.__dict__[self.name] = Namespace(computed=False, val=None)
        return obj.__dict__[self.name]


    def __get__(self, obj, cls=None):
        if obj is None:
            return self
        data = self._data(obj)
        if not data.computed:
            data.val = self.equation(obj)
            data.computed = True
        return data.val

    def __set__(self, obj, value):
        data = self._data(obj)
        if self._update is None:
            raise AttributeError("Field '{}' doesn't support updates.".format(self.name))
        else:
           value = self._update(obj, data.val, value)
        data.val = value
        data.computed = True

class FixedpointField(Field):
    def __get__(self, obj, cls=None):
        if obj is None:
            return self
        data = self.data(obj)
        if not data.computed:
            data.val = val = self.initial(obj)
            data.computed = True
            while True:
                nextVal = self.equation(obj)
                if nextVal == val:
                    break
                data.val = val = nextVal
        return data.val


# Something that will be set by the parents can have an initial value
# Should it take on that value before it is set?

# initial
# update
# fixedpoint
# subtree

# Subtree simply takes the function
# and applies it to all of the children.
# Hmm.
# Either that, or, there's actually a subtree object.
# And you simply overwrite it with other versions ...
# That's pretty OK as well, and a whole lot easier to implement.



# Unify
#    A Metavar knows its current pattern,
# or it doesn't. This method does NOT allow you
# to backtrack. The other method requires you
# to always provide a substitution though ...
#    This means that there needs to be a difference
# between match, which does produce a substitution,
# and produces a default value,
#     and unify,
# which you can't backtrack on.
# So a failed unification produces an error..!
# You need to be able to override though.

# Pattern match

def fib(n):
    A, B = meta(2)
    with match(n):
        if Func[A, B]:
            return Func(~A, ~B) # Nasty... and awful if you forget it
        if Func[B, C]:
            pass

# Parsing


