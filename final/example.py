from underlang import *
import sys

class Num(Node):
    n

class Add(Node):
    a
    b

@Num.value
def f(num):
    return num.n

@Add.value
def f(add):
    return add.a.value + add.b.value

# Picobot

class Picobot(Node):
    rules

class Rule(Node):
    fromState
    surr
    move
    toState

class State(Node):
    name

@State.decl
def r(state):
    return state.root.getState[state.name]

@State.reachable(initial = lambda s: False)
def r(state):
    return state.decl.reachable or any(p.reachable for p in state.decl.predecessors)

State.predecessors(initial = lambda s: set())

@Rule.toState.decl.predecessors
def add(rule, preds):
    preds.add(rule.fromState.decl)

Root.getState(initial = lambda s: dict())

@State.root.getState
def declare(state, getState):
    getState.setdefault(state.name, state)

s = State
r1 = Rule(s(0), 0, 1, s(3))
r2 = Rule(s(1), 0, 1, s(3))
r3 = Rule(s(3), 0, 1, s(2))
p = Picobot([r1,r2,r3])

p.rules[0].fromState.decl.reachable = True
print(p.rules[1].toState.reachable)
print(p.rules[2].toState.reachable)
print(p.rules[1].fromState.reachable)
