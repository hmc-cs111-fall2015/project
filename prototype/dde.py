class ExtendMeta(type):
    def __new__(mcl, name, bases, namespace):
        mcl.cls.__dict__.update(namespace)
        return cls




class A:
    a = 1

class B(A):
    b = 2

class C(A):
    c = 3

print(C.a, C.c)
class C(metaclass=ExtendMeta):
    b = 5
    c = 1
    a = -9


print(C.a, C.c, C.b)


