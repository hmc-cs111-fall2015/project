# Language design and implementation overview

## Language design

The basic computational idea is just code generation and manipulation.
So let's explore for a moment the kinds of choices you could take
for how to use code as data. We'll explore a canonical example,
which is computing the nth power of a number. We can generate code
that is specific to the particular n given at compile-time.

This code is the original, which takes two numbers directly at runtime:

    def power(x, n):
        return 1.0 if n==0 else x*power(x, n-1)

The first and most obvious way to deal with code
is to use strings directly. For example,

    def power(x, n):
        return "1.0" if n==0 else "("+x+" * "+power(x, n-1)+")"

Then,

    power("x", 3) == "(x * (x * (x * 1.0)))"

Obviously, there are problems with this approach.
It's extremely easy to produce syntactically
incorrect code. It's also extremely easy to produce
code that parses, but does the wrong thing. For example
a naive implementation without parentheses could produce the following,
which fails because of operator precedence:

    times(add("a", "b"), "c") == "a + b * c"

You can also have problems where variable names start binding
to different things in different places, if anything is
available at all (dynamic scope). You also
don't get any guarantees on the code
that you presumably could figure out at compile time,
such as type correctness.

Quasiquotation is one helpful tactic, where you work
with abstract syntax trees instead of strings.
Ultimately, this only gets you that the resulting
code will certainly be syntactically valid,
but many other problems can remain.

Additionally, you end up with one huge question
remaining which is, "Should the host language and
the code it manipulates be the same language?"
If they are the same, it helps with interop
and a lot else. But generally you would prefer
to be able to work with other languages.

In exploring the various attempts out there to deal
with these problems (which are often associated with the term
"multistaging") I've made the following
progression which seems to get more powerful
at each level:

1. Abstract syntax trees
2. Template Haskell: Monadic quasiquotation. Difficult to be sure of correctness.
3. MetaML: Language built for type-safe code generation. Generated code must be in the same language as host.
4. Lightweight modular staging: Library-level code manipulation. Type safety, minimal syntactic overhead. Generated code does not have to be in the same language as host, but still manages some reuse of features between them.

Lightweight modular staging is billed as a means to produce "abstraction without regret." That is, the best of both
worlds in terms of DSLs with high-level abstractions, but also performance since those abstractions are
compiled away. However, in terms of my project, I would especially like to explore
the ways it can be used for verification and things like that. Thus, the language work
involves how to use LMS in that way (among others).

If I feel like I can reimplement LMS with a different interface, or perhaps in a different language,
then that would be a project I would be satisfied with. However, until such time,
I intend to use LMS in order to do some simple units calculations and verifications,
and in particular attempt to make that implementation as simple and striaghtforward as possible.
The language will evolve out of that.


## Language implementation

It would be ideal if I managed to implement a small version of LMS in another language, perhaps Python.
Python does not satisfy the needs of LMS (not even Scala does, without some minor modification), but
it seems it might not be impossible. There is already a very full-featured implementation of LMS in Scala.

Given an implementation of that backend, the remaining implementation work is not huge -
it amounts to the implementation of a small internal DSL to make some specific use cases _slightly_ easier.


