You didn't submit an evaluation.md, which would have been nice to know where you're at.

### Notebook
> Additionally, only comments in the first method named "main" in the first class are parsed.

How often are there classes with more than one `main` method?  I guess they could exist in theory,
but it seems pretty odd to me.  This also seems like it doesn't let you have modular code that
has been cleanly broken up into functions and classes, but still get the flowchart benefits.  Is this
just a temporary decision, or is it likely to remain in your end product? If it is likely to stay, why?

I love that you started using `Optional` - while I agree it can be clunky, in general I find it to be
much clearer than `null`.

I'm glad that you noticed that not all flowcharts will have a single terminal node - I can imagine 
programs with many different terminating states, depending on how thorough they are with their error 
checking.  I think I might like the syntax of `//$<identifier>` or `//$codeviz.<something>` for the
sake of clarity, and also helping reduce potential collisions with other tools you may be unaware of.

Have you tried to use this library?  Is it better (or worse, or both) than the one you originally
planned to use?  What, if any repercussions will there be from this switch?

You didn't enumerate any specific questions you'd like answered, so I won't comment on anything like
that.

### Implementation

You seem to be using tabs, not spaces - why would you do this to yourself?

`getMethod` also seems clunky, but I don't have a better solution.

What are DOT files?  Are they read by graphviz?  Are they your own thing?

_Dan Obermiller_
