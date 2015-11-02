# Project description



## Motivation

Extensibility is a great thing. However, in most languages, there is a fundamental barrier
to extensibility: that barrier is compile-time behavior. In some languages it is possible,
and in a few rare examples even mildly _feasible_ to directly control compile-time behavior
(especially those languages that have some form of quasi-quotation, i.e. LISP, Haskell, Scala.)
But it is almost never easy, encouraged, and first-class. CompiLang is an attempt to make a language with
full compile-time control.

## Language domain

I suppose that if there is a domain, it is code manipulation. That is, programming
where the data is almost always code (in the form of abstract syntax and semantics).
People who would benefit from this would be people trying to learn about various
compile-time benefits, or people interested in
exploring the possibilities of language extensibility.
I categorically reject attempting to make something _practically_ useful.


## Language design

Compilation is essentially a process of conversion. An example might follow this path:

    String -> Tokens -> Abstract Syntax -> Abstract Semantics -> ... -> Bytecode

__Abstract semantics__ refers mostly to abstract syntax along with semantic information.
For example, variable types and scopes. A compiler may go through several stages of abstract
semantics. This is where the most interesting behavior happens, in the `...` section.

CompiLang encourages users to break compilation into several different stages at this point,
each with access to increasing information. Just as a brainstorm, here are some of the kinds of forms
these stages might take:

- Mutation: As with syntactic sugar, implicit conversions, and constant expression evaluation
- Inference: Calculating specific semantic properties
- Verification & Analysis: Checking semantic comprehensibility
- Optimization: Black magic

Other than optimization, doing these kinds of things to code will be first-class.

You can imagine that a particular stage is implemented much like a function. (Probably syntactically too.)
It takes in some kind of abstract semantics, and produces another. 
The final step is producing a final
product - which could be bytecode, or perhaps code in a different language, or a mathematical
form like System F - but that part is beyond the scope of this project.

## Example computations

The most obvious is to implement various different type systems of varying complexity. 
Another would be to implement units with automatic conversions, as a compile-time feature.
Or, to do code verification as with Hoare logic.

