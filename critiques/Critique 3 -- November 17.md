_Critiquer: Matt Valentine_

## NextNode and Building Flowcharts in General

In general, it seems a Node has two things, children and siblings.
The siblings are recorded as a linked-list of "nextNode"s.
That is mostly true: For the last node in a branch, it's  nextNode
actually points outside of that branch, so it isn't always strictly a "sibling."
But still, close enough.

Your code should work for only top-level structures, since it doesn't really have
the nesting required to properly add children, but it does deal with the sibling case.

In other words, ultimately you'll need to handle nesting in some way.
As I see it, you could do that with a stack of nodes, where closing a context pops off the stack
and opening one pushes to it.
But, I've been thinking about the details of that for forty minutes now, and there are certainly
some annoying subtleties.
If I can figure something specific out, I'll tell you.


## GraphViz Output

You're going to have to have a way for a Node to print out the corresponding GraphViz code.
The first step to that is to have each Node have an ID.
All you have to do is have a static counter in Node, and everytime you construct a node
you increment the counter.
Then your identifiers can be "Node1", "Node2", ...

As far as I understand Dot, you have to describe each Node, and then describe each
connection between nodes. So Decision for example would end up being

    <MyID> [text=condition]
    <MyID> -> <IDofTrueBranch>
    <MyID> -> <IDofFalseBranch>

completely regardless of what the children end up getting printed out as.
So that means, each node can print itself out in GraphViz notation independently,
as long as it can access the id of each of its children.
I think that will be doable.

