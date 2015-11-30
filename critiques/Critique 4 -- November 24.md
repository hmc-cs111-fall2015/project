Why did the regex parser need a keyword between quantity and ingrediant if you’re still forcing quantity to be a single word? I think it makes more sense to use a separator, but I don't see why it’s necessary. I also don't see why `of` doesn't still work. The instruction `add 1 can of cream of mushroom soup`, although disgusting in a coffeelike drink, is still unambiguous with single-word quantities. If you want to switch to multi-word quantities then I agree you need a non-alphanumeric separator, but I think you can still use "of" as an alternative and just assume that the first "of" is the separator.

If you’re worried about the parser’s reaction to whitespace, you can force whitespace around the `of` by parsing it as a keyword (which is also a good idea for your other keywords, like `make`). We did this in our Piconot External language with the function
```scala
  def rword(word: String): PackratParser[String] = {
    ident filter {_ == word} withFailureMessage "Expected reserved word <" + word + ">."
  }
```
I think we had some bugs around our failure messages, so you might want to change or get rid of that part, but the general idea here is to use the java `ident` parser, which works well and accounts for whitespace as you’d expect, but force the parsed `ident` to be the keyword you want. You use this as follows:
```scala
verb~quantity~rword("of")~ingredient
```
or
```scala
rword("remove")~ingredient
```
I believe you can just deconstruct it in the case statement as usual (e.g., `case v~q~"of"~i => RegularInstruction(i, q, v)`), but I don’t remember for sure; when we used that parser we also used the `~>` and `<~` operators to selectively ignore the keywords instead.

On a separate note, the README is fairly out-of-date; you should probably update it at some point.
