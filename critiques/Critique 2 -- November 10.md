# Critique: 9 November 2015

Alex Ozdemir

## Response to Questions

Offline, Anna presented the following questions:

   1. How might a 'tile set' system be flushed out. 
   1. What extra funcitonality would tiling functions provide? How would they
      actually help the user.


### On Tile Sets

What is a tile set? A tile set is when a user combines some [small] tiles in a
particular way, and then wants to take the group and treat it as a tile in the
context of a [larger] map.

How might this be handled?

In my mind a natural solution is for tiles and maps to essentially be the same
thing. In this world the user would define tilesets in the same way that they
define maps, and tiles could be taken from out of program images or in-program
maps.

If this were to be done then it would also be useful for the user to be able to
define multiple maps in the same file. They would probably only render one, but
they could include the others as tiles.

### On Tiling Actions

In some sense a tiling action is fairly similar to a tile set. It allows the
user to easily repeat some microstructure. The difference is that tiling
actions are parameterizable by the input tiles. In some sense tiling actions
are strictly more powerful then tile sets.

Anna raised the good point that realistically the users can just copy-paste and
modify to produce the same affect. My initial reaction to this was negative - I
thought that any time users might want to copy-paste something the language
should do something to make that easier.

However, perhaps users are happy doing the copy-pasta, and it might be simpler
to just not implement tiling actions. Tile sets are useful, provide a lot of
functionality, and don't require a lot of extra implementation.
