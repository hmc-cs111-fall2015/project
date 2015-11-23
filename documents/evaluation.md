# Preliminary evaluation

_What works well? What are you particularly pleased with?_

Technically, nothing works at all. That's because I spent so much time last week muddling through implementation,
that this time my deliverable is just the test file that I'm going to use, which shows the syntax I'm going.
I have put tons of research into implementation so far, though, so I'm confident that I can
make a (version) of the syntax I have work. In particular, I've got a small start on doing that.

I think that the syntax is really clean, expressive, and readable! I would like to know if you think the same!
Otherwise I'm in big doo-doo!

_What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive?_

In order to avoid boilerplate, essentially nothing is statically checked in this language.
It is ridiculously dynamic.
For example, suppose you have a class with a default-valued field

    A
        name =?= "hello"
  
and you want to set it from a different class

    B
        @child a
        naem = "goodbye"

but you misspell it, well, now you've got both `name` and `naem`.

Another not-cohesive thing. I have two syntaxes for groups. Namely,

    A
        @child a, b
  
defines `a` and `b` as members of the `child` group in `A`.
But, I also have a group syntax for classes,

    A : Expr

which defines `A` as part of the group `Expr`. I don't know if perhaps
there's a good way to merge these. It is true that the basic idea is a little different,
since class groups cause a subclassing-type relationship.

_Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests?_

My evaluation has been _awful_. I did not follow any of the strategies I suggested in my evaluation plan.
On the other hand, for this project, I was never able to treat the implementation backend as a "black box",
because certain approaches might or might not even be usable. The way I planned to implement the backend,
and as a result the sorts of things I was able to put into the language at all, has changed radically
nearly every week.

I wanted to make this an internal DSL very badly. However, in the end, I've had to go with an external DSL.
If only Scala had true monkeypatching like Ruby or Python, I would be a happy camper.

(_Hint hint_, if you happen to know how to accomplish that. I think that it miiight be possible with, like,
 chained implicits? But whatever. I'll just ignore all that for now. Sigh.)

_Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?_

My trouble so far has been almost entirely in terms of "how the f do I implement this," in terms of the very
most basic, fundamental approach. One such problem was how to simultaneously support bottom-up and top-down computations.
The current approach based on attribute grammars is a solution, but it is still comparatively inconvenient for
top-down.

_What's left to accomplish before the end of the project?_

IMPLEMENTING IT. Also, if anybody has any feature requests ...
Actually, I have a bunch of extra features in mind. So I think I'll implement a main set,
and then perhaps just describe all the rest and how you'd go about implementing them.




