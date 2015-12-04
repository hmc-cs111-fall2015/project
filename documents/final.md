###Introduction

Tile-based games are very popular for RPG indie developers (or for any developer that can use tile-based backgrounds for their games),
but most software that exists to generate tile maps limit users to square tiles,
making it difficult to have more natural looking regions without creating a ton of fixed-size images.

Though a text-based DSL is not ideal for this, making small adjustments to the map is generally easier than with traditional
map-making software, and is possible without users needing to create new tiles or adjusting the tile images.

###Language Design Details

The code currently runs in Eclipse. The user must save a text file with their code in the src directory, and then when
running tilemap.scala type the name of the file in the command line. The specified images are then generated.

The following is a sample map file:

```
tile water = src/Water.jpg
tile ground = src/Ground.jpg
freeform tile river = src/River.jpg {
    anchor = (14, 0)
}
freeform tile house = src/House.jpg

map {
    width = 300
    height = 300
    origin = topLeft
    
    layer 0 {
        fill rectangle (0,0) (300,300) with ground
    }
    layer 1 {
        fill area (300,300) (0,300) (0, 245) (50, 266) 
                  (100, 215) (110, 225) (150, 235) (190, 200)
                  (222, 167) (245, 133) (250, 99) (266, 45) (270, 0) (300, 0) with water
    }
    layer 2 {
        at (55, 0) place river
        at (30, 145) (140, 89) place house
    }
}

generate debug map as BasicDebugMap
generate map as BasicMap
```

The first part of the code is the specification of the tiles.
Tiles lacking a `freeform` keyword can be used with the `fill` command. On the other hand, tiles with the `freeform` keyword can be used with the `place` command.

With freeform tiles, there is also the option of specifying an anchor, which is the point on the tile image that is aligned to the point specified with `place`.
If none is provided, it is assumed that the anchor point is at (0,0).
In the example, specifying
```
anchor = (14, 0)
```
Allows the user to, say, mark the top corner of the river rather than having an anchor on a transparent part of the image.

* Errors: The program will crash and output an error message if
  * The user has two tiles of the same name
  * The user tries to load an image file that doesn't exist
  * There is an improper tile definition (not in the format "(freeform) tile = SRCPATH")
  * There is an improper anchorpoint definition, or one is supplied for a basic tile.
  
Next, a map is specified.
```
map {
    width = 300
    height = 300
    origin = topLeft
    
    layer 0 ...
}
```
Maps have a width, height, and origin, which can be specified in any order. The origin can only be topLeft or bottomLeft for now.
Also, the origin is optional; if none is specified, topLeft is default.

* Errors: The program will crash and output an error message if
  * A width and/or height is not supplied, or comes after layer specifications
  * The width and/or height is not at least 1
  * The map doesn't have any layers or is improperly defined (not in the format "map { CONTENTS }")
  
Then, layers are specified.
```
layer 0 {
        fill rectangle (0,0) (300,300) with ground
    }
    layer 1 {
        fill area (300,300) (0,300) (0, 245) (50, 266) 
                  (100, 215) (110, 225) (150, 235) (190, 200)
                  (222, 167) (245, 133) (250, 99) (266, 45) (270, 0) (300, 0) with water
    }
    layer 2 {
        at (55, 0) place river
        at (30, 145) (140, 89) place house
    }
```
Each layer has a precedence number, and can be specified in any order. The numbers also do not have to be sequential (for example, -3, 4, 100 is allowed).
Layers can also have a mix of instructions, and so do not have to contain only `fill` or only `place` commands.
If there is a mix of commands, areas are filled before freeform tiles are placed. For any placements, they are done in the order specified, so the latest tile placed is above the rest.

The `fill` command is followed by either an `area` or a `rectangle` keyword.
Rectangles can be specified with two, three, or four points. Two points are assumed to be diagonal to each other, while if three points are given, the fourth is inferred.

For the areas, the order that the points are given in matters. For example, (0, 0) (20, 0) (20, 20) (0, 20) produces a square, but (0, 0) (20, 20) (0, 20) (20, 0) produces a sharp hourglass shape.
The order of points does not matter for rectangles.

* Errors: The program will crash and output an error message if
  * Two or more layers have the same precedence number
  * A `fill` is called on a freeform tile or a `place` is called on a basic tile
  * Layers or commands are improperly specified
  * Commands are specified for tiles that don't exist
  
* Warnings and strange behavior:
  * The program will print out a warning if there is a chance that part of the map will be drawn out of bounds. The program won't crash, because perhaps the user wants to use this behavior to, say, not have a freeform tile (like the above river) have to fit within the map.
  * If three or four points are given for the rectangle, but the points make a different shape, the program will interpret this as a rectangle that the shape fits inside, and will fill in that area.
  
Finally, one or more `generate` calls can be given.
```
generate debug map as BasicDebugMap
generate map as BasicMap
```
Either a basic or debug map will be made with the given filename. The images are currently `.png` images.
It is possible to generate the same map kind with different filenames; multiple files will be created.

A debug map provides the outlines of areas and freeform tiles that are placed. These are with lines whose colors are randomly generated for each layer.
Layering is in the proper order, and a small X is placed at the anchor point of each freeform tile.

* Errors: The program will crash and output an error message if
  * The generate call is improperly specified
  
###Language implementation

This is an external DSL whose host language is Scala. With the background the class provided for creating an external DSL, and how far removed from general programming this domain is, it seemed like the best choice.
Additionally, Scala shares many libraries with Java, and there was a Java image processing library that worked well.

The front end is fairly simple; the text file is given, read in as a string, and sent to the parser.

The parser reads in the file and generates an AST object for the semantics to use. A good portion of error handling happens here.
Essentially, the file is read in three chunks: the tile specifications, the map specifications, and the generate calls.
Most of the parsing matches strings and reads in names, with the exception of the parser for the image path, which must use a few more parsing objects to work around the `/` and checks to see if the image file has an acceptable format.

The parser, AST, and semantics are all tuned to work with each other, so some changes to each have been made to compromise between the different parts.

Thus, an AST object takes in three values: a list of (TileName, Tile) tuples, a Map object, and a list of (MapType, String) tuples. The first of these is used to create a hashtable of tilenames and their tiles, stored as tileTable. The second is simply a Map object, and the third is the list of generate calls, where MapType is either `basic` or `debug`.

