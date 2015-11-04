# November 3rd Critique

_Critiquer: Matt Valentine_

## Response to Questions

_Is this idea to small? Is this suitable for a DSL or more of an API?_

As I understand it, some of the background motivation you have for this project
is real-world experience seeing people struggle coding robots.
If you can build something that would actually be helpful to those people,
then I think it is decidedly _not_ too small.

I would say this would probably end up being an API/library.
That might be because of C++'s limitations as far as creating
internal DSLs goes. However, to be fair, designing an API
in a way that is easy to use, especially for beginners,
is still a very difficult task.

I _do_ think there's a potential for the project to become too small though.
For example, if the state abstraction ends up being really easy to
implement, but not enough to make the general process user-friendly yet.
Or, if you're unable to do certain things you want to simply because of C++.

Thus, I would say, if you think you can accomplish making
a framework that would really be substantially easier/cleaner,
then your project will probably not end up being small.

## Minor points

- You mention that something like `wait` might introduce shadow states.
In general, though, arbitrary computations are already happening inside
of the states, so that may not be necessary.
- I think this is already your intention, but it seems like it would
be better to focus on making <whatever slightly complex robot action
you're thinking up> straightforward to code, and hope that Picobot
falls out of that. (That is, it might be tempting to make your
language conform to Picobot, which might not be good.)
- As far as actually implementing states, it might be good to
look into enums. I think that would also allow you to do
a switch/case block instead of an if/else if, if you felt like it.
- I looked around for promising stuff on C++ internal DSLs,
but I didn't find much that wasn't super heavyweight. So just by virtue
of it being C++, you may be limited to an API/library.
Again, though, I don't think that dooms the project to being
non-linguistic.


