# Project plan

## Language evaluation

The bare minimum implementation that has to be done is:

* Specify tiles, put them in layers, and construct a map
* Have a working debug map of some sort
* Allow for freeform tiles to be placed using anchors
* Fill in specified right-angle areas with specified tiles

To test this, tiles will be constructed and a test map will be made with these specifications.

First, an intermediate representation that is compatible with the image library needs to be made, along with a more formal grammar.

As each piece of implementation is added, translation to the AST will be added with it so that it can be tested asap. Though it would be easier for me to create the IR, then parsing, and then semantics separately, this is very bad for debugging.

Outputting debugging maps (and potentially actual output maps) along the way will evaluate the implmentation. Comparing between the actual code that can be written and the ideal code can serve as a measure for language design evaluation.
Another possibility is having others try to make maps to see how intuitive using the language is.

And, of course, someone will read over the documentation to make sure everything is clear.

Additional implementation would be:

* Adding borders (unless implementation turns out to be quicker than expected)
* Specifying non-right-angle areas for tiling (supplying a list of points to specify a shape rather than opposite corners of multiple rectangles)
* Changing the orientation of the map
* Some way to have tiles that repeat in a non-square shape (ex: hexagonal tiles)

Though if any of these seem easier to add at any earlier point, they will be.

## Implementation plan

At each checkpoint: fill in notebook entries, add documentation as necessary.

###11/1/15:

>Create a few tiles for future testing; finish deliverables

###11/8/15:

>Have a fully-formed grammar, AST, and an understanding of how the host IP library will use the AST

>Work on design_and_implementation.md, integrating feedback.

>Have scala files set up, work on implementation for the simplest map: read in a single tile, output a map of that tile's size made of just that tile.

###11/15/15:

>Finish implementation for the simple map, add layers and ``fill`` for just a single layer.

>Add in freeform tiles and placement.

>At this point, potentially have outside user test for how intuitive it is to use.
Have some sort of prototype ready by Monday.

###11/22/15:

>Work on ``fill`` for specified areas, potentially add in borders and/or the non-right-angle areas for tiling.

>Definitely have outside user test the code.

>Work on evaluation.md at the end.

###12/6/15: 

>Finish any implementation, add in extras if there's time.

>Make sure all documentation is complete and understandable.

>Have another round of testing done.

>Have the demo ready for Monday.

###12/11/15:

>Finalize testing.

>Work on final.md.
