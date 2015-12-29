> I managed to write compiling but untested code

Uh oh.  Have you tried writing tests, or do you think that they will require a robot
to run on?  Can you think of a way to abstract those details away so you could at least
write some simple unit tests?

After reading further in your notebook, I see that you have thought about it to some extent.
In my mind, having unit tests that simulate a robot are going to be helpful - not because
they are actually interesting, but because they let you test that everything behaves as it
should.

I think the work to build an actual robot may be more than is worthwhile for this class - if
you want to continue this project in the future it is definitely worthwhile, but I think
unless you want that to be your final presentation it isn't worthwhile.

The Python bindings would be cool, however depending on how you do them they could be a pain
(if you're directly interacting with the C Python API then bleh, if you're just calling a C
module then you should use [cffi][1]).

> Substates will probably be useful to users, but I'd rather get a core version of my language
> working before I start adding auxiliary features.

I agree. I think getting a working product, that is reasonably extensible, makes the most sense
given our time constraints.

### Questions
To address your questions, I think that the example is mostly straightforward.  I have specific
comments about your code here, in no particular order.

Where is `Rover5.h` coming from?  Is this something the user is expected to have installed? That
would be a nice thing to mention in the documentation.

Where did you get the milliradians for the directions?  It seems that degrees might be easier for
the reader to understand, and then perform the appropriate conversion as needed.

Implementing a `printf` like method in `Serial` might be nice as well, or giving it a stream-like
interface, instead of the Java-esque `Serial.print();Serial.println();`.

I think that `every` might be better off with a type signature like

```c++
every(unsigned int interval, TimeUnitsEnum unit)
```

and then use that appropriately, instead of defining constants like `100_ms`.

In general, I found the code to be a little unclear without any explanatory comments, however I 
think I was able to get the gist of it in most cases.

I found the `StateOfTheRobot` files a little hard to read, but I think that has more to do with
my discomfort using macros than anything else.  It seemed to make sense, however I wonder if 
maybe breaking it up into more files for the sake of modularity might be worthwhile.

`using namespace _SOTR_Private;` Naughty, naughty.  If you're going to just use the namespace openly
like that, why bother with the namespace?

I'm also a little uncomfortable by the amount of global scope you use - this couldn't be wrapped in
a struct or class?  Then you could conceivably extend this to work with multiple robots.


### features.md

I didn't find this file very useful.  

For example, in the overall assumptions, you say that you assume that the program is 
singly-threaded - is there any way that in the future it could be safely multithreaded? 
Is there a way for users to safely use multithreading in their own state functions?

What about "every function is fast"?  How fast?  What happens if it isn't fast enough?

In general I felt that this documentation could benefit greatly from expansion.


- Dan Obermiller



  [1]: https://cffi.readthedocs.org/en/latest/

