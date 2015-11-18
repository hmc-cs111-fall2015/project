### Critique for Nov 17th

You asked me to look into the implementation and tell you what I think. After looking at the implementation, I had a few 
observations:

- It looks like you built off the same structure as the piconot-external homework assignment, which is good. Splitting up distinct
parts of the language seems like a good thing.
- Your sugar.scala lists its author as Matt, not you. You may wish to change that
- The code appeared to be pretty well factored. However, due to the sheer number of moving parts
(as well as not particularly informative variable names), it was hard to understand what the semantics was doing. As you near
a final version of the code, you may wish to comment it more.
- How is error checking going to fit into your code? What kinds of errors are you planning to catch, and how will you display
them to the user?
- I like the naming of the package that puts the program together and runs it Engine - that seems quite informative. 
- Filler is not a particularly informative name. You might want to rename it - maybe to CodeBlock or something?
