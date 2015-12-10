# Critique: 1 December 2015

Alex Ozdemir

## Project Status

Great work! After a bit of twiddling (see Project Structure below) I was able
to run your code, and it was awesome!

I played around a bit with the sample program, putting things in different
locations and looking at the output. I also turned on the thing that outputs
the basic version of the map, as well as the debug.

All in all I thought it was cool :).

The one user experience comment I have is that the Debug map felt sort of
crytic at first. I wonder if there would be a way to communicate what source
file each time comes from. I liked the touch with the origin though!

## Project Structure

This is a bit of a side-note, but `sbt` expects to find scala source files
under `src/main/scala/...` instead of just `src/...`. Doing things that way
might make it a bit easier to have other people run your code.

Given that layout I think you can an `sbt` command to generate project files
which tell Eclipse where to look for things.

## Parsing

It seems that you have resolved your parsing troubles, so I won't address this.
If I am incorrect in this assumption, let me know.

For what its worth, you can define String parsers from a Regular Expression
like so:

```
lazy val time: Parser[String] = """\d{2}:\d{2}""".r
```

## Next Steps

This is more of a question for you - but what do you intend to do next? How can
we support you in that?
