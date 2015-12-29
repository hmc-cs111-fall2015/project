# Decisions
While in my first critique I suggested that the `FlowchartNode` class should not have a `nextNode` member, I now think that it should. It seems like there's three cases:
 1. Both branches come back to the main function. The flow chart should have a line come back from each branch to the "main line". The next node on the "main line" will be the `nextNode`
 1. Neither branch terminates. Then `nextNode` is just a terminal node
 1. One branch comes back and one diverges. In this case, there is still a "main line" that `nextNode` should point to. This, however, requires two (three?) different types of terminal nodes. There's the normal "this control structure is done", then there's the "exit() was called, don't draw any lines from this point". There's also some intermediate things if there's something like a `break`, `continue`, or `return`. This could get even more awkward.

This third case is awkward, but I'm not sure if it's solved by getting rid of `nextNode`. On the other hand, dealing with `return` may warrent its removal (I'm not sure). And what even happens with recursion? Is that even flowchartable?

#Evaluation
I wish I had time to install Maven, etc, to actually try out your stuff and see a picture. Actually, it would be really awesome if you could just upload a picture of the flowchart for your code since it sounds like your stuff is mostly working. I continue to be impressed with your demo being the source code of your program.

It would be awesome if this was somewhat language-independent! Using some sort of protocol buffer/json thing would be neat and sounds like a good solution. I'm slightly worried that a generic language may not be able to be expressed in your chosen AST, but if your AST is close enough to the flow chart syntax, you could say that if it's not AST-able, it's not really flowchart-able either (I'm thinking Haskell here). So it sounds like a good thing.

I support your decision to just support Java with `if` statements since getting something working really well is really cool. Other control flow like loops, recursions, `return` statements, and so on sound really tricky to deal with.

#Other

A comment syntax for multi-line comments could just be
```
/*$ Long
 *$ Comment
 *$ Is
 *$ Long
 */
 ````
 
 `Optional` is cool, of course, but I don't feel like `parse` should return one. If there aren't any codevis comments, can't it just return an empty AST?
 
 
