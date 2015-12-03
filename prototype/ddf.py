import typing
from pyrsistent import pmap


class PUnionFind:
    '''
    If a metavar is not in the dictionary, it is assumed
    to refer to itself.
    '''
    def __init__(self):
        self.data = pmap()

    def _find(self, key):
        return self.data.get(key, (key, 0))

    def union(self, a, b):
        aRoot, aRank = self._find(a)
        bRoot, bRank = self._find(b)
        if aRank > bRank:
            pass








class Pattern:
    def unify(self, value, subs = None):
        subs = PUnionFind() if subs is None else subs
        for subpatterns in self.extractor.unapply(value):
            pass

class Metavar:
    def unify(self, value, subs = None):
        current = subs[self]
        if current is self:
            self._cached = value





# Unify

def unify(pat1, pat2):
    pass

# We have an ADT.
# We have an extractor.
# It takes in a value, and is either successful or not.
# If successful, it returns a tuple.
# Each element of the tuple is then matched
# against the whatchamacallit. OK.
# Unify could be @= ?

# With an ADT, getitem produces a pattern.
# A pattern is an object with a unify method.


class ADTMetaclass(type):
    def __getitem__(cls, *args):
        return Pattern(cls, *args)




# Metavar


# Pattern


