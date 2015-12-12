## testscript.caf

So your first request was to go through this and see if there are any features or things being 
left out.

First impressions:

I don't really know whats happening in this script. The top part:

```
{
    LATTE {
        add 4 shots @ espresso;
        pour 3 oz @ chocolate milk;
        scoop 2 spoons @ sugar;
    }
}
```

looks like a list of recipes, but thats not really denoted by any syntax. I feel like it would
be easier to read if this was more clear. There are still questions about the difference between
the verbs but other than that, this syntax looks fine. Why choose ```@``` instead of ```of``` though?
This is personal preference but I don't like having to press shift all the time. 

The second part is what really confuses me:

```
make LATTE;
remove chocolate milk;
swap cinnamon drops -> sugar;
```

I tried going through your notebook entries and commits and READMEs but I can't seem to figure out
what these instructions are really doing. ```make LATTE;``` makes sense. I assume this would just make
a latte for the user. The problem comes in on the next lines. ```remove chococalte milk;``` happens after
the latte is "made", so is this command really doing anything? If it is, why? This seems pretty unintuitive
from a writer and reader perspective. 

I saw in a previous notebook entry that you considered doing ```begin``` and ```end``` when specifying modications
and I think that would be a great idea. something like ```start LATTE;``` and then after you make the modications,
have the user write ```finish``` or something late that. Because, just reading the file, the remove and swap seem
separate from the make. 

The other problem I had reading this syntax is that it took me a bit to understand which side of the arrow meant what
for the swap. Maybe instead of an arrow have the keyword ```for```? This doesn't really on the user having the 
same intuition on what an arrow means. 

## Main File

Honestly this file is pretty confusing to me since there isn't really any documentation telling me what is happening
with the script. Sorry I couldn't give much advice on this. It looks clean though. 

## This week

Error checking and additional features are nice, but I think time would be best spent refining the syntax a bit to
make what is happening behind the scenes a little more transparent. I think it would also be cool to have two different
types of scripts, so that a machine could have one, and the UI could create another one based on a user request that 
actually "makes" the drink. 
