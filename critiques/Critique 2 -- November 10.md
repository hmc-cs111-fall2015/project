### Your Questions

So you asked me what features are most important to be implemented. As I can see it, 
the most important part of your language is its extensibility to coffee machines. Since
they inherently have different sizes and needs for measurements, I would first work 
on implementing the different measurements and weights. 

Once you have those done, it will allow you to think of new extensions of the DSL. 
Being able to run different measurements at different weights will cause some problems,
so I think that might take some time. 

### Future of the Language

So I think the next major thing you need to think about is how users will be able to call 
drinks inside other drinks. How that will affect the size of drinks and their ratios. 
I think it will be difficult to make this an "easy" addition without also removing a lot
of options from the user. Maybe write out some proposals, give them out to some friends 
and get feedback on how they are read and what people think they mean (This is what we 
are doing for our DSLs clinic, with limited success).

As I think your questions have hinting towards, you need to start scoping what you want
users to be able to do. Since we only have a few weeks, you might have to just make a 
decision right now for an end goal and start working towards it. From your notes, it seems
like you have a lot of things you want to do that its making you a bit indecisive on 
actually implementing concrete parts of the DSL. 

There are also verbs being used in the language and I'm confused on how they are different
in meaning. Is ```scooping``` something different than ```adding``` something? Does it have
to do with the contents that are being actioned on? Having a lot of freedom can be a good 
thing, but if the words are doing the same thing than that might just confuse the user.
I would also think about how these verbs are used by a coffee machine instead of a baurista.
Someone writing caffeinescript knows that the machine is doing the work, so it might be 
unintuitive for them to think from the perspective of a person. (I don't necessarily 
believe this, it might just be a good thing to think about when choosing verbs and nouns.

### Other Stuff

You might want to start writing on the README for your language. It was kind of hard for me 
to understand its current capabilities or even the planned capabilities. 
