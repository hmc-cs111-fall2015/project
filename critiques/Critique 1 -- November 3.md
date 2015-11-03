# Critique: 3 November 2015

## Response to Questions

You mentioned that you were looking for feedback regarding the syntax of the
language.

You provided two ways of specifying that a debug map should be produced, the
opening `debug = True` and the close `generate debug map as PATH`. I think the
second meshes better with the way that the users exports normal maps. If we
accept a debug map as a special type of map it makes sense to export in in the
same way. An interesting alternative is to have an interactive visualization
mode where the user types and sees the map change in real time. That would be
sort of neat too.

I also want to pick on the `from (x1, y1) to (x2, y2) fill ...` syntax a bit.
This is used to fill in a rectangular pattern (as I understand), but that is
somewhat implicit. Especially if you intend to add other patterns I would make
the rectangle-ness explicit, for example `rectangle (x1, y1) (x2, y2) fill
...`, or something like that. Then you could imagine swapping the rectangle bit
with some fancy area description.

The `freeform` keyword seems a bit weird to me. Perhaps `placeable` or
`floating`? This is a very small thing though.

## Language features

While this is a bit early, it might be worth starting to think about what types
of language features you might want to include, and if so in what order.

Some that come to mind are...

Should there be names? Should I be able to compose tiles and give the result a
new name which can in turn be composed? This seems pretty useful to me.

Should there be tiling action functions? Should I be able to combine/sequence
tiling actions (fill this rectangle, and that one, and that one...) into a
single action with a name that I can later use. This seems less useful, but
potentially neat.

Should there be custom area definition? Should I be able to add Ellipse (like
rectangle) even though it's not built-in? This seems less useful, but
potentially neat.

## Next Steps

What to do next? I agree that thin-slicing is the way to go here. Get a minimal
end-to-end system set up with tile import, a simple tile instruction (place
tile in corner, or something like that) and map export.

This will most likely be a good way to get used to the image processing
library and set up a rudimentary parser.
