_Anna Pinson_

A minor suggestion, but could the language be set up to handle spaces? It seems that users would naturally add spaces after each comma.
Some of the keywords, like `DontWantToWorkWith`, seem kind of clunky, but users could get used to it.
I believe parsers should be able to match strings with spaces in them; then again, my parser is broken, so I may be completely wrong.

Your first option seems to be your best bet. You can encode in both ways as you build your dictionary, too.
For instance, `"Math"` maps to `1`, and `1` maps to `"Math"`.
Because (presumably) the user is always supplying strings for constraints, then all keys in the dictionary that are strings are guaranteed to be in the "forward" direction, and all keys that are integers are guaranteed to be in the "backward" direciton.
Of course, building two separate dictionaries works just as well.
