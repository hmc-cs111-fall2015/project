# Language design and implementation overview

## Language design

To write a program, simply create a program file and compile the code. Someday, a GUI will exist.

The basic computation that happens is reading the pixel values from the tiles and writing these values in their proper places in the output image.

The data structures are:
Points, which are just tuples of numbers
Tiles, either (a) basic ones which can have an edge and be repeated, or (b) ones that can be placed anywhere, and have have a name, sourcepath to an image file, (a) an optional sourcepath to an edge image file, and (b) an optional Point specifying an anchor
Maps, which have a name, width, height, orientation (either topLeft or bottomLeft), and a list of Layers
Layers, which have a number and specifications of which tiles to place and where
And Areas, which are the specifications of where to fill in the map with basic tiles

The control flow thus far is pretty strict. The parser isn't quite in place yet, but tiles must be declared before the map is, and within the map the width, height, and origin must be specified before any layers are, though the layers may be ordered in any way (if any of them have the same number, though, there will be an error). Tile specifications within a layer can happen in any order.

Because of this, there are quite a few ways that errors can happen, including:
* Invalid filepath
* Repeating any names (for tiles or maps)
* Repeating layer precedence numbers
* Declaring a map before any tiles are declared
* Declaring layers before the orientation and size of the map is declared
* Declaring no layers or no map
* Incorrect declarations (Providing any non-int numbers, giving an anchor to a basic tile or an edge to a freeform tile, not providing a proper keyword for the map's orientation, ect)
* Calling fill on a freeform tile or place on a basic tile
* Declaring multiple maps - (Maybe? if maps now have names, this may be allowed.)

The inputs would be the locations of image files for the tiles, and the outputs are the map and debug map. At this level, there probably won't be much tool support.

There are many DSLs for tile mapping, none of them text based. Because of this, it's difficult to compare them. I'm also not sure how many have layering (outside of non-mapmaking-specific image apps like PS).



## Language implementation

This is an external DSL, since the domain seems isolated from other functionality Scala might have.
It makes the most sense.

The piconot assignment helped with familiarizing myself with creating an external DSL in Scala,
and since I managed to find ways to do IP in Scala this was the best choice for me.
I did end up just using Java to do this, rather than going to a library.

Syntax:

Much of the syntax was sort of explained above.
Using `=` and `{}`, with indentation being optional, seems the most intuitive for users to write programs in.
The `fill` and `place` keywords, again, seemed intuitive, along with "constructors" like `map`, `layer`, and `tile`
Having layers with precedence seemed like the easiest and more familiar way to allow for layering, as well as a way to conceptually split up the map and group tiles/regions of tiles.
In all, the design decisions were made for ease of use.

The system works by:
- Parsing a program file to make a Map object, complete with all information necessary to create an image
- Taking the Map object and, layer by layer, reading each tile and copying over the pixels onto the output image(s)
- Saving the output image(s)
