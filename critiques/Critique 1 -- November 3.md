I really like the motivation of your project.  I've definitely experienced
this before, for example when I want to contribute to some new open source 
project.  The overhead of joining a new project has often been enough to
discourage me from contributing entirely.

I do wonder about some of your statements, in particular about the use of
comments.  It seems from your description that you advocate for more
commenting, which [some people vehemently disagree with][1]. Now I by no 
means agree with all of the statements there, but there is certainly an 
argument to be made that more descriptive code is preferable to commented
code.  Would you say that your language would lead to an improvement in 
the readability of the code itself, or induce an increase in comments?

I agree with your description of code2flow.  I didn't really like it. I 
think your point about Flowgen is well-intended, but it seems like ideally
all control-flow structures _should_ be documented this way.  I assume that
no one would run the "Codeviz" program on a source file they didn't want
documented in this fashion.

Would you piggy back on the existing parser for that language, or would
you have to write your own? That seems buggy and like a lot of work.

I think I'd want an error, not a warning, if I only document one branch.
A flowchart without all of the flow(?) seems pretty useless to me.

I also wonder about the languages supported - maybe I missed it but you
didn't specify what language(s) you want Codeviz to work with.  I think
it would be cool if it worked with all* languages, but I realize that 
is by no means practical.

I clearly horribly miscounted my weeks when I planned mine out.  Depending
on the language you implement this in, there may be useful existing libraries
to generate graphs/flow charts in that language. I imagine [graphviz][2] or
one of its many wrapper libraries would be of interest.

This plan seems pretty reasonable - do you have a plan for what you'll do if 
you get bogged down in some details or get off track?  It seems like if you
didn't complete anything after "4" you would have meet your baseline goals.



\* Well, all reasonable languages.




  [1]: http://butunclebob.com/ArticleS.TimOttinger.ApologizeIncode
  [2]: http://www.graphviz.org/
