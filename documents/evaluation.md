# Preliminary evaluation

I'm way behind.
Thus far, the code doesn't actually run. Everything is set up correctly; the only problem is that it won't parse.
Given this, there isn't much feedback on the user experience that can be done.

One thought is that the output is saved as an image; I should look into ways to make it display the output as well, so that when the user runs the program they don't have to go in an open the file.

It would also be good to make sure that it will overwrite files automatically if the map is being saved to the same name, or that users can toggle a warning for this. It is possible users will want to iteravely build the map, and so would want to continually overwrite the image file, and it is also possible users will want to keep different versions of the map and would want a reminder that they need to change the name of the file being written to if they don't want to lose previous data.

Much of the error handling should theoretically be caught by the parser (though evaluating this is difficult...).
The AST is also robust enough to handle some of the other cases mentioned, like calling `fill` on a `freeform` tile.
As it is, multiple maps can't be declared using the same map description. The odds of a user wanting multiple copies of the same map, however, is small, and it wouldn't be worth implementing since making copies of image files is trivial.

Some problems came up along the way, and most of these were solved by adding complexity to the AST. This complexity ended up not going overboard - at least, it is still fairly simple to follow what is going on, and additions generally made things clearer (or no less clear).

Alex's suggestion to describe shapes as fill areas rather than depending on points helped put me on track to add this complexity, which now makes extending the language to have more complex fill areas much easier. Tile composition is another suggestion I hope to implement, though with the time remaining this doesn't look too likely.

Robin suggested hexagons, which would also be very useful. Originally, I considered adding more tile-able shapes like this, or having them be a workable tiling schema in the language. These suggestions have helped me keep extensibility in mind while developing the language.

For the rest of the project, I plan on dedicating Thanksgiving break (four solid days, give or take) to getting parsing to work and adding in the rest of the implementation.
Filling in rectangular areas is the next most important thing to implement, followed by borders and non-rectangular area specifications. Debugging maps, if it comes down to it, can be removed.
