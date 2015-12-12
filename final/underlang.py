# osetattr = object.__setattr__
# ogetattr = object.__getattr__
import sys

from collections import defaultdict, Iterable

class Storage(dict):
    '''
    This is a god-awful way to do pseudo-superclassing
    of attributes. That is, with
        class A:
            x = Attribute()
        class B(A):
            x = Attribute()
    B.x._storage pretends to be a subclass of sorts of A.x._storage.
    '''

    # These make it so that you can do JavaScript-style
    # dot notation access of elements inside an ordinary
    # dictionary.
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, attribute):
        super().__init__()
        self.attr = attribute

    def __missing__(self, key):
        '''
        If the key is missing from this storage,
        go to the enclosing attribute's class,
        go up to the next Node class,
        go into the corresponding attribute,
        ask its storage.
            Which may have to ask the next one up
        in turn, etc.
            Yayyy.
        '''
        for superclass in self.attr._storage.cls.__mro__[1:]:
            if issubclass(superclass, Node):
                superattr = getattr(superclass,
                                    self.attr._storage.name)
                return superattr._storage[key]
        return None

class NodeMetaDict(dict):
    '''
    Keeps track of the order and names
    of variables referenced, so you can do
        class A(Node):
            a
            b
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.list = []
    def __getitem__(self, key):
        if not key.startswith('__'):
            self.list.append(key)
            return None
        else:
            return super().__getitem__(key)

class NodeMeta(type):
    '''
    Conceptually, the type of the Node object,
    as opposed to Node instances (which are of type Node.)
    '''
    def __new__(mcls, name, bases, nmdict, **kwargs):
        '''
        Setup the children based on the class definition.
        '''
        children = nmdict.list
        namespace = dict(nmdict)
        namespace['_childNames'] = children
        childProxies = []
        for c in children:
            proxy = ChildProxy(c)
            namespace[c] = proxy
            childProxies.append(proxy)
        klass = super().__new__(mcls, name, bases, namespace)
        for c in childProxies:
            c._storage.cls = klass
        klass._remote_modifiers = defaultdict(set)
        return klass

    def __getattribute__(cls, attr):
        '''Create proxies as necessary when accessed.'''
        if attr.startswith('__') or attr in cls.__dict__:
            return super().__getattribute__(attr)
        if attr == 'rewrite':
            newattr = RewriteProxy(cls)
        else:
            newattr = AttributeProxy(attr, cls)
        setattr(cls, attr, newattr)
        return newattr

    @classmethod
    def __prepare__(metacls, names, bases, **kwargs):
        '''Use the NodeMetaDict instead of the normal local namespace
           when creating a Node class.'''
        return NodeMetaDict()

def rewrite(node):
    '''
    Rewrite a node until it is satisfied
    with its lot in life.
    '''
    while isinstance(node, Node):
        rewritten = node.rewrite
        if rewritten is node:
            break
        node = rewritten
    return node

def iterNodes(nodes):
    '''
    Since collections of nodes are
    supported as children, it's a common
    task to iterate through potentially
    one level of iterators.
    '''
    for n in nodes:
        if isinstance(n, Node):
            n = rewrite(n)
            if isinstance(n, Node):
                yield n
        if isinstance(n, Iterable) and not isinstance(n, Node):
            for n in n:
                if isinstance(n, Node):
                    n = rewrite(n)
                    if isinstance(n, Node):
                        yield n

class NodeSuper:
    '''
    This super class is mixed into Node,
    so I don't have to worry about the NodeMeta
    class doing weird things while I define
    these couple normal functions.
    '''
    def __init__(self, *args, **kwargs):
        self.parent = None
        # GLOBAL ROOT
        # if global_root is not None:
        #     global_root._children.append(self)

        '''
        Terrible implementation of a custom function
        signature based on the children declared.
        '''
        assert len(args) <= len(self._childNames)
        assert all(c in self._childNames for c in kwargs)
        for c, a in zip(self._childNames, args):
            assert c not in kwargs
            kwargs[c] = a
        assert all(c in kwargs for c in self._childNames)
        for c, a in kwargs.items():
            if isinstance(a, Node):
                a.parent = self
            elif isinstance(a, Iterable):
                for n in a:
                    if isinstance(n, Node):
                        n.parent = self
            setattr(self, c, a)

    @property
    def children(self):
        yield from iterNodes(getattr(self, c) for c in self._childNames)

    def _remote_modify(self, node, attr, value = None, ignore = None):
        '''
        Apply remote changes corresponding to node.attr.
        '''
        if ignore is None:
            ignore = set()
        if self in ignore:
            return value
        ignore.add(self)
        for modifier in self._remote_modifiers[attr]:
            val = modifier._remote_modify(node, self, value)
            value = val if val is not None else value
        for child in self.children:
            if isinstance(child, Node):
                value = child._remote_modify(node, attr, value, ignore)
        return value

    def __getattr__(self, attr):
        getattr(type(self), attr)
        return getattr(self, attr)

class Node(NodeSuper, metaclass = NodeMeta): pass

class Proxy:
    '''
    _storage is used to avoid polluting the namespace,
    and also to help chain the attributes of
    subclasses together.
    '''
    def __init__(self, name, cls = None):
        self._storage = Storage(self)
        self._storage.name = name
        self._storage.cls = cls

    def __getattr__(self, attr):
        '''
        Returns a proxy that represents
        an inherited or collection attribute on
        the node that THIS attribute supposedly
        sets
        '''
        return SubAttributeProxy(attr, self, self._storage.cls)

class ChildProxy(Proxy):
    '''
    When a child is accessed, first check if
    it wants to rewrite itself. That's
    why this proxy exists.
    '''
    def __init__(self, name, cls = None):
        super().__init__(name, cls)
        self._storage.child = {}

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        child = self._storage.child[obj]
        child = self._storage.child[obj] = rewrite(child)
        return child

    def __set__(self, obj, value):
        self._storage.child[obj] = value

class AttributeProxy(Proxy):
    '''
    The implementation of attributes.
    '''
    def __init__(self, name, cls):
        super().__init__(name, cls)
        self._storage.value = {}
        self._storage.computing = defaultdict(bool)
        self._storage.computed = defaultdict(bool)
        self._storage.circular = defaultdict(bool)

        # Now these are kept undefined.
        # Setting them to None explicitly
        # prevents them from checking up
        # the next level to see if the superclass
        # defines a property of this attribute.
        #self._storage.compute = None
        #self._storage.initial = None

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        '''
        If currently computing,
            expects to have a value
            returns it
        First, creates an initial value if there is one.
        Sets "computing" flag.
        Runs equation, gets result.
        Sets it.
        '''
        import sys
        #print("1", self._storage.name, file=sys.stderr)
        # If cached, just used that value.
        if self._storage.computed[obj]:
            return self._storage.value[obj]

        #print("2", file=sys.stderr)
        # If currently computing the value, we've
        # got a circular dependency.
        if self._storage.computing[obj]:
            self._storage.circular[obj] = True
            # We expect to have an initial value so that
            # we can do fixedpoint iteration to resolve the
            # circular dependency.
            assert obj in self._storage.value, "Circular evaluation of {} without an initial value, or circular initial value!".format(self._storage.name)
            return self._storage.value[obj]

        #print("3", file=sys.stderr)
        # Starting to compute.
        self._storage.computing[obj] = True

        #print("4", file=sys.stderr)
        # Get an initial value, if applicable.
        # Mostly used for circular dependencies and
        # remotes.
        if self._storage.initial is not None:
            self._storage.value[obj] = self._storage.initial(obj)

        # Actually compute the value,
        # doing fixedpoint iteration if it's circularly
        # dependent.
        if self._storage.compute is not None:
            value = self._storage.compute(obj)
            if self._storage.circular[obj]:
                while value != self._storage.value[obj]:
                    self._storage.value[obj] = value
                    value = self._storage.compute(obj)
            self._storage.value[obj] = value

        # If there is no compute function for this
        # attribute, then we consider it to be remote:
        # that is, it gets its value from other nodes
        # on the AST.
        else:
            value = self._storage.value.get(obj, None)
            self._storage.value[obj] = obj.root._remote_modify(
                obj, self._storage.name, value)
            self._storage.computed[obj]

        self._storage.computing[obj] = False
        self._storage.computed[obj] = True
        return self._storage.value[obj]

    def __set__(self, obj, value):
        # If we're directly setting...
        # Well, just accept it.
        self._storage.value[obj] = value
        self._storage.computed[obj] = True

    def __call__(self, func=None, initial=None):
        '''
        Sets something about this attribute.
        '''
        for key, func in [
            ('compute', func),
            ('initial', initial)
        ]:
            if func is not None:
                self._storage[key] = func
        # Allow chaining
        return self

class RewriteProxy(Proxy):
    '''
    A special proxy for the rewrite attribute.
    It's different because you can have multiple
    separate rewrite functions.
    '''
    def __init__(self, cls):
        super().__init__('rewrite', cls)
        self._storage.rewriters = []
        self._storage.rewritten = {}

    def __call__(self, rewriter):
        self._storage.rewriters.append(rewriter)

    def __get__(self, obj, owner = None):
        if obj is None:
            return self
        if obj in self._storage.rewritten:
            return self._storage.rewritten[obj]
        for rewriter in self._storage.rewriters:
            result = rewriter(obj)
            if result is not None:
                rewritten = result
                break
        else:
            rewritten = obj
        self._storage.rewritten[obj] = rewritten
        return rewritten

class SubAttributeProxy(Proxy):
    '''
    SubAttributes dispatch remote evaluation declarations
    such as
        @A.child.friend.mother.hat
        def itsPink(a):
            ...
    A: Node
    child: Attribute
    friend: SubAttribute
    mother: SubAttribute
    hat: SubAttribute
    '''
    def __init__(self, name, parent, cls):
        super().__init__(name, cls)
        self._storage.parent = parent

    def __call__(self, func):
        self._storage.func = func
        self._storage.cls._remote_modifiers[
            self._storage.name].add(self)

    def _remote_modify(self, node, modifier_node, val=None):
        parent = self._get_parent(modifier_node)
        # print("Modify match:", parent, node, id(parent), id(node))
        if parent is node or isinstance(parent, Iterable) and node in parent:
            v = self._storage.func(modifier_node, val)
            return v if v is not None else val #return None
        else:
            return None

    def _get_parent(self, obj):
        return self._storage.parent.__get__(obj, self._storage.cls)

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        parent = self._get_parent(obj)
        return getattr(parent, self._storage.name)


class Root(Node):
    _children

# GLOBAL ROOT
# global_root is an odd idea,
# which is that sometimes every
# node that a person ever creates
# is significant.
# That's often true in examples;
# but less true in practice.
# So this is disabled for now!
# There is also some disabled code
#global_root = None
#global_root = Root([])

# Look, I got to use my DSL in my DSL!
@Node.root
def root(node):
    if node.parent is None:
        return Root(node) #global_root
    else:
        return node.parent.root
