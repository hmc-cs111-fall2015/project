I guess my first question is whether or not you have any implementation using LMS that you can show
in your [project repository][1] - I would have liked to be able to see what you're working on to 
have a better idea of the practical implementation details.

To address your question about

> it might be an OK result if my project turned out to be a tutorial of sorts on those paradigms, 
> if I was unable to actually make using them easier.

I think that would be okay, but I would also really enjoy hearing about why you were unable to make
using them easier - what sort of things you tried, why they didn't work, and what you learned from
them.  I don't know if I believe that something can never be improved - but seeing evidence of how
you were unable to improve it would help a lot.

I'm also not sure I understand the [design and implementation][2] document.  You said:

> The first and most obvious way to deal with code is to use strings directly. For example,

> ```
> def power(x, n):
>    return "1.0" if n==0 else "("+x+" * "+power(x, n-1)+")"
> ```

and I guess this is not at all the most obvious way to deal with code.  I guess it seems that you're
trying to enhance the functionality here, to allow CompiLang to improve something, but I'm having
a hard time seeing what.

I like the point about the host language and manipulated languages being the same.  I think if I 
were using this tool I wouldn't care about the host language nearly as much as my ability to use
it to modify my programs in a wide variety of languages.

I would appreciate if there were some examples of how Template Haskell, MetaML, and LMS work and
why they're used - I think I'm still having a hard time visualizing what your language is intended to
do and how.

That being said, after finishing this document I think I have a better idea of why you picked the goal 
you did - I think that it could be very hard to improve on LMS, especially in the context of a few weeks.


- Dan Obermiller


  [1]: https://github.com/MatthewValentine/compilang
  [2]: https://github.com/MatthewValentine/project/blob/master/documents/design_and_implementation.md
  
