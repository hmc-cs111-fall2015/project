# Project description and plan

## Motivation

Tile-based games are very popular for RPG indie developers (or for any developer that can use tile-based backgrounds for their games), but most software that exists to generate tile maps limit users to square tiles, making it difficult to have more natural looking regions without creating a ton of fixed-size images.

Also, it can be somewhat annoying, if not tedious, to have to create tiles with borders; to have bordered pieces, eleven to sixteen tiles must be created (depending on whether more than 2 sides need to be bordered for the area), and even more than this must be made for diagonal borders.

In its fully-developed form, this product would make it easier to create complex maps with fewer input images, and it would do all the work of cutting up the image into tiles for the user, generating any unique ones as necessary.
Also, it will be easy for users to make small changes to how an area looks without having to change any of their original images.

A text-based DSL is not ideal for this, but once it's in place creating a GUI should be fairly easy (though probably too time-consuming to happen in the scope of this project).

## Language domain

The domain is, essentially, tile mapping. It's very useful for game design, specifically indie game developers interested in making RPG-based games.

There are many tile mapping applications - many with their own external DSLs, a few with internal DSLs in, for example, Python - but none that particularly take into account the variable tile size.

One reason for this is the way that game engines use tile maps. Since storing every single map, or even one giant overworld map, would use up disk space, tile-based games store the maps in pieces, either tiles or tile sets (a grouped collection of tiles in a single image), that are loaded and put together at runtime.

With this in mind, it would be helpful to also include some sort of output that is more useful than just a single image, depending on what tile mapping engine the game developer is using.
For instance, the map could be broken up into tiles again, generating any unique tiles that came about from the specific arrangement of the given pieces.
Similarly, tile sets could be created for more complex objects/tile arrangements.

## Language design

Use keywords to load up some tiles, specify layers and make a map.

This will be text-based, so a program will consist of lines of code. When it runs, there are flags that can be set to define the output.

The main output, for the simplest implementation, is just the final map in a single image.

For debugging purposes (for the user, not just the implementor), there will also be a chance to output an image file with outlines of each area being filled in, as well as freeform tiles with their anchor points. Hopefully, they will be color-coded for each layer; at the least, the lines that are "hidden" under other layers will be a different color than the lines that are "visible". 
here should also be an indication of bordering, perhaps with different line thickness.

There are a handful of Scala image libraries that exist which would be very useful for composing the final output. Additionally, many of the things from the last project will be helpful here, especially using traits to get keywords to work right.

As for errors, besides general syntax errors (using keywords wrong, not supplying enough inputs, not specifying a map, ect.), the main thing that users aren't allowed to do is to overlap specified areas of the map in the same layer. Ideally, this would give a compile-time error.

There really isn't any reason to allow users to make multiple tiles from the same image, since tiles can be using on different layers, but there also isn't any real reason to prevent users from doing so, as the original images won't be edited in any way.

Also for debugging purposes, if a user doesn't actually generate a map, there will be a warning printed at compile time, but it will compile anyways. This way, the user can set debugging to be on and keep making the test maps.


## Example computations

Here's a sample block of code:

'''
#includes go here

debugging = True

tile water1 = SRCPATH
tile ground1 = SRCPATH {
	edge = SRCPATH
}
freeform tile house = SRCPATH
freeform tile peninsula = SRCPATH {
	anchor = (0,200)
}
map {
	width = 750
	height = 750
	origin = bottomLeft

	layer 0 = {
		fill water1
	}
	layer 1 = {
		from (0,250) to (250,750) fill ground1 with border on (right, bottom)
	}
	layer 2 = {
		at (250,250) place peninsula
		at [(100, 650), (250, 600), (400, 300)] place house
	}
}

generate map as FILENAME
generate debug map as FILENAME

'''

This will:
*make the tiles the program will use
*make the layers, 0 with just water, 1 with a chunk of ground, and 2 with the freeform tiles
*generate a map that'll be saved as FILENAME in the current directory
*generate a debug map, as debugging is on
