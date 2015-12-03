# Pattern Matching in Python

class ADTMeta(type):
    pass
    # getitem -> Pattern Constructor

class ADT(metaclass = ADTMeta):
    def unapply(self, value):
        pass




# Just a pattern on one side, and a value on the other
# In that case...
def match(self, value):
    subvalues = self.root.unapply(value)



class Expr(Node):
    @initial
    def type(self):
        return
class Func(Node):
    @initial
    def type(self):
        return Func(meta(), meta())



class Pattern:
    def __init__(self, root, subpatterns):
        self.root = root
        self.subpatterns = subpatterns

    def match(self, value, subs):
        subvalues = self.root.unapply(value)
        assert len(subpatterns) == len(self.subvalues)
        for value, pattern in zip(subpatterns, subvalues):
            subs = pattern.match(value, subs)
            # Pattern failed to match
            if not subs:
                return None
        # All patterns matched
        else:
            return subs


class Metavar(Pattern):
    def __init__(self):
        self.v = None

    def match(self, value, subs):
        # If metavar has already been matched to a pattern,
        # just use that directly
        if self in subs:
            pattern = subs[self]
            return pattern.match(value, subs)

        # Otherwise, match directly to the value.
        else:
            return subs.union(self, )

