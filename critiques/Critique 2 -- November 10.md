### Language choice
While it might be somewhat easier to use Scala than to use Java, I don't think
it's necessary to use the visitor pattern if you were doing java. The nice thing
about the haskell way of doing it which translates into the visitor pattern is
that you can add a new function really easily, and in that function you handle
both kinds of input. With java, though, you'd have to add code in several
different places to add a new function, one in each class. Conversly, to add a
new data type to Haskell requires that you modify every function to add support
for the new possible type.

I feel like the Java way of doing it is actually nicer in your case. In the
`Node` class you can specify methods to draw the node and whatever other
functions you want, and in the process/decision classes you can define these
methods to do the appropriate things. Then if you want to add a new type of
node, you can just add a new class with the right methods.

### Flow Chart AST
I don't think that a `Node` should have a `nextNode` in it: what does `nextNode`
mean for a `Decision`? I think it would make more sense for `Decision` to be as
written, and `Process` to have a `nextNode` and a `description`.

You might also consider having more than 2 cases come out of a `Decision`. For
example, if your code has a switch on an `enum`, it would not be very clear to
have the chain of ifs.

You mentioned that you wanted to be able to "fold" code into subroutines, but
your flow chart AST does not have a way to specify this. Having a `Fold` case
would probably be useful. This brings up another question: when a subroutine is
unfolded, how does the flow chart reader know how to connect the correct nodes
of the subroutine to the caller? So I think you might want to add another type
of node which is something like `Leaf`, that says the code does nothing else.

### Opt-In Nature
I like your idea that CodeVis would be opt-in, so that some parts could have the
special comments and some parts would not be flowcharted. What I'm worried about
is that if someone forgets to add the comments to a certain critical part of
their code, or if the comments aren't formatted correctly and CodeVis doesn't
see them, CodeVis will silently just not print anything for that part of the
code.

Similarly, if people don't comment a section, it seems like other issues could
come up. If a section is uncommented, what does the flow chart show for that
part? What if there's an uncommented if statement, but in each branch there's
some CodeVis comments? I think more thought needs to go into how these
ambiguities are resolved and when it is an error to not comment a section.

-Adam Dunlap
