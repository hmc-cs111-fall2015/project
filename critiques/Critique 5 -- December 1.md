Sorry this is a little late.

#### evaluation.md

I don't think that it being dynamic is unreasonable - while staticly checked languages
have their own advantages, the ease of using a dynamically typed language is pretty
much unmatched.  This is especially true when considering the time constraints of this
project.

I don't really understand the part about groups that is immediately following that point.

I tend to agree that this is probably not well suited for an internal DSL - it seems that
what you want is pretty hard to accomplish in a meaningful way that also masks the host
language flavor.  Best of luck with implementation!

#### Notebook for 11/22/15

I'm not sure how much I understand the example.  I get what they're supposed to be
doing (except for the `@child` relationship - what parent-child relationship is that
representing?), but I don't get why you're making them 'open' - what benefit does that
provide?

What purpose does the self-dependent `Lam#scope` serve?  Why is that desirable? How 
would you implement that? What happens if the value always changes?

Overall, I guess what it is doing sort of makes sense, I think I'm just rather hung up
on what the whole language is supposed to do (still, sorry).  Maybe I missed it in one
of the old project evaluations or notebooks, but I'm still not clear on the intended
functionality of the project (and evaluation.md seemed to indicate that you aren't
either).

I notice that you still don't have anything in your compilang repository - is this because
you haven't implemented anything for the external DSL? Are you going to put stuff in there?

_Dan Obermiller_
