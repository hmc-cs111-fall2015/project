The question you asked me was how I would design a parser for this language. While I wouldn't consider myself sufficiently well versed 
in your language to be able to tell you how to write your parser, I can tell you some things I learned or wish I had known when 
writing my parser, which will hopefully transfer to yours too:
  1. Don't write your parser all at once; write it in iterations. Think of the simplest possible program that you could write in this
  language, and first build a parser that can handle that. As you think of more complicated expressions to include in the language
  rewrite the appropriate rules (if you're using a PackratParser, which you seem to be doing) to be able to handle the additional 
  complication.
  2. Use example driven development (This relates to my first point somewhat). Write out a concrete program that you want 
  the parser to be able to handle, and use this as a model to build the parser on. You may have to change your program to make it fit the
  constraints of using a PackratParser - for instance, I found that I needed to use special character to separate parts of the program.
  3. Try to avoid using magic constants in your parser when possible; instead, you could specify them as `val`s at the beginning of the
  parser. Since writing a parser is a very iterative process, you may find yourself wanting to change, for instance, a line 
  terminator, and it's much easier to do that by changing a constant than having to find-and-replace every instance of it in your parser
  code. 
  
Here are some more concrete suggestions, or miscellaneous parser-related notes which you may find helpful:
  1. I was looking at your AST.scala, and I noticed something odd: shouldn't the Between class be specified by 2 times, not one 
  (after x but before y)? Or am I misunderstanding what Between means here? 
  2. When talking to Prof Ben, I learned that PackratParsers don't have a tokenizer, which makes making specific tokens keywords if they
  fall under the characters captured by a particular regex isn't really possible. For instance, I wanted to be able to say
  `<quantity> of <ingredient>`, where `of` is a keyword, but I had to change it to `@` because otherwise the quantity and ingredient couldn't
  use the letters "o" or "f".
  3. If you need to capture multiple words in a piece of the AST, `ident`s won't cut it; you may need to use Regular Expresions. Luckily,
  PackratParsers can handle regular expressions; the syntax for these is `"""<your regex here>""".r`. Also, if you want to test your
  regexes to make sure they're capturing the correct part of your code, you can look [here](http://regexr.com/). 
  4. It seems like you've copied some example code from somewhere into Parser.scala as example code. 
  I would recommend against consulting this when building the framework for your parser and instead write the parser "from scratch".
  If you try to write the parser from the ground up, then you're constantly thinking about your vision for the language, which shapes 
  the structure of your parser and lets you catch language design flaws sooner. If you're fitting your parser to the mold of another,
  then you may be too focused on using a similar design to the example to build a parser that's tailored perfectly to your language. 
  After the time I've spent working on my parser, I'm starting to feel like writing a working and understandable parser is very much an art.
