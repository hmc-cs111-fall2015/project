# Project description and plan

## Motivation

Coffee drinks are difficult to make. In the world of the ever-present hipster, it's getting harder and harder to get it just right. In a world where customers actually order a "split-shot, heavy on decaf, 20 oz, soy, extra dry latte, with half pump vanilla & half-pump hazlenut", keeping track of all the modifications to make for a coffee drink is a difficult experience even for a physical barista. On the other hand, automatic coffee machines have a finite amount of settings that a customer can customize, so are not as customizable as ordering from a live barista. 

If there was a standard language by which a customer could specify a drink to an arbitrary level of precision, then you could easily program an automatic coffee machine to make exactly the drink you want. 

We need a DSL for this because we want to enable users to specify their drinks to arbitrary levels of precision. There are so many factors that go into a caffeinated or alcoholic beverage that we need a language (rather than, for instance, an enumerated type), because there are just so many possibilities.

## Language domain

This language addresses the domain of automated coffee drink specification. The domain is useful because it seems to me like automated drink machines will never be able to attain the quality of a human barista or bartended until you can specify your drinks as much as you want. 

I don't believe there are any other DSLs in this domain. The closest thing I could find while searching for similar languages was [this](https://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol). 

## Language design

A program in the language is going to look like a list of instructions to execute, in order. We require the language to be imperative instead of declarative because it makes a difference the order in which ingredients are added to what the final product will look/taste like. Thus, we should allow the user to control the order in which things happen. For instance, most baristas add shots of coffee to the milk in a latte, and not the other way around. When a program runs, depending on the backend attached to the language, you could get as a result:

1. A physical coffee drink. (this would be ideal, but is too much work to implement for this class)
2. A sequence of print statements corresponding to the steps taken to produce the drink.
3. A visual rendering of the coffee drink.
4. Analysis of the recipe to see what ingredients you need to make the drink, and in what quantity. 

I'm not sure what kinds of control structures/data structures might be useful yet, except for a mutable list in which to keep the steps to execute that come out of the parser. When I decide exactly what the syntax of a program will look like, anything that doesn't match that syntax will throw an error because the parser won't be able to parse it. As far as compile or runtime errors go, I think figuring out what these will be will happen organically as I start to write the language. One possible semantic error I thought of is trying to add 0 parts of something - though you deal with this by ignoring the instruction, for the sake of readable code it would probably be better to not allow the user to do that. 

## Example computations

Initially, I had thought that an program could look like this:
```
Begin LATTE:
1. 2 shots espresso
2. Add 10 oz 2% milk
3. Add 2 oz foam
4. Add 4 pumps sugar
End LATTE:
```
However, during the first peer review of my project pitch, it was suggested that I specify the amount of each ingredient to use in terms of weights. This is so that you could calibrate the machine to produce a drink of a particular size based on the size of cups available. 
So instead of specifying quantities as `2 shots espresso`, you could specify `10% espresso` and the machine would deal with figuring out the exact quantity to produce based on the cup size. In this case, we'd need the programmer to have a way to specify the cup size as well (if, for instance, they're using their own cup), maybe at the top of the file. 

So instead an example program might look like this:
```
Begin LATTE:
1. 7 parts 2% milk.
3. Add 1.5 parts foam
3. Add 1 part espresso
4. Add 0.5 parts sugar
End LATTE:
```
When this program runs, the following things should happen:

1. The parser parses the program into a list of rules to execute sequentially.
2. Each rule should be parsed to extract 2 key pieces of data - the name of the ingredient used and the quantity of that ingredient to add. 
3. Once the program is fully parsed, it will be executed by iterating over the list of rules and executing each one. 
4. A rule will be executed by calling the appropriate API function of the backend (the idea is that each of the possible backends I mentioned above implement the same interfact).
5. Depending on which backend is in place at the time, an output of some type will be created 

# Language design and implementation overview

## Language design

A user writes programs in my language by creating a text file containing the instructions to be executed. 

The computational model being used depends on which backend is hooked up to the language, in my opinion. For instance, the backend described later in this document does constraint satisfaction, while the printing backend I've currently enabled just iterates over the instructions and evaluates them. I'm not even sure what computational model you'd use to describe the ideal backend, which executes instructions to actually produce a beverage.

The basic data structure is the instruction. An instruction contains an ingredient (the ingredient being used in this instruction), a verb (add, pour, sprinkle, etc), and a quantity specifying the quantity of the ingredient to add (eg, 2 scooops). A program is simply a list of instructions. 

There are no control structures in my DSL, as yet. I don't currently intend to add any control flow structures or allow the user to specify/manipulate control flow (except maybe by defining and using macros, though I wouldn't really consider this manipulating control flow).

A program in the DSL currently requires a sequence of instructions, provided in a ceratin format. Here's an example of a CaffeineScript program:

```
add 4 shots espresso;
pour 3 oz milk;
scoop 2 spoons sugar;
sprinkle 10 grams cinnamon;
```

If I add features where the user can specify additional info (aside from the instructions themselves), such as what ingredients and what quantity are available, or how many cups of the specified drink to make, the program structure will need to include a header of some kind, that's separate from the instruction list. I anticipate this making the parser a lot more... involved, so I may have to ask Prof Ben if he has any tips for how to parse programs with multiple distinct parts (especially if some of these parts are optional!). 

The output that a program produces depends on what backend it's hooked up to. The ideal output would be a nice cup of coffee, but in lieu of that I've created one backend that just prints the instructions being executed in sequence (you'll have to imagine the cup of coffee). The output from this backend looks as follows:

```
adding 4 shots of espresso
pouring 3 oz of milk
scooping 2 spoons of sugar
sprinkleing 10 grams of cinnamon
```

I'm still in the brainstorming stage for other backends that would be interesting to have for this language, but the one that I'm interested in adding analyzes what ingredients you have and in what quantity and tells you whether you have the ingredients you need to make the drink you want in the quantity you asked for. 

One way in which a program can go wrong is if a user uses a liquid verb to modify a solid ingredient: for instance, `pour 3 oz sugar` doesn't make any sense. I remedied this by creating a separate set of solid ingredient related words and liquid ingredient related words, and only let the parser accept an instruction that has all words of one kind. Other ways a program could go wrong are by making the cup the drink is created in runneth over, or not adding any liquid ingredient at all (at that point, is it even a drink?). I haven't done any error handling yet, but I imagine that critical errors will be thrown as exceptions while noncritical issues may be printed as warnings (I haven't decided for sure whether to add warnings yet). 

The project doesn't provide any tool support as yet, and I don't have any plans to make it do so. That stuff, while useful for a general purpose programming language, doesn't (in my opinion) have much place in a language as small as this. 

There aren't other DSLs for this domain that I know of. Kevin made a good point in his critique this week that the machine that makes bottled Starbucks frappes could be using a DSL internally, but this is probably a proprietary language (if it exists), which is why I couldn't find it or learn from it when I was searching for other DSLs in this space. 

## Language implementation

I chose to write an external DSL in Scala. The first choice I made was the choice of language to write it in - I chose Scala partly to force myself to learn Scala (and functional programming paradigms in general), even though I may have been more comfortable in Java. In addition, I anticipated that many of my classmates might choose to write their languages in Scala, making it easier to go to them for debugging help. (Also, Prof Ben seems to know the language quite well, which is a plus).

Given that I was going to use Scala, choosing to make an external DSL instead of an internal one was a no-brainer for me. Three major factors shaped this decision:

1. I knew that my language wasn't really related to Scala's domain (ie, there was no need for my language's code to exist alongside regular Scala code). In particular, the language is targeted at a very narrow domain and wouldn't benefit from being in the same environment as regular Scala code.
2. Implementing piconot as an internal DSL was **way** more painful that externalizing it, and I anticipated the features of Scala hindering more than helping for CaffeieneScript as well.
3. CaffeineScript has a very different feel from Scala. The goal is to make a program sound like natural language, specifically like a recipe. This is not what programs in Scala read like.

As far as syntax goes, the first significant decision I made was designing the structure of an instruction as 
`verb + quantity + ingredient`. I also decided to not allow users to mix words relating to liquid ingredients and relating to solid ingredients (a program that tries to do this will fail to parse!). I think that this decision came from a place of wanting to force programs to be readable. While C may pride itself on allowing you to write obfuscating code, I want to force users to write readable programs in this DSL.

The only major architecture decision I've made so far (that I don't plan to change) is the decision to store a program as a list of Instructions to be executed. I feel like executing the instructions in sequence is true to the spirit of a recipe, and as I've mentioned before instructions in making a coffee drink don't commute in general. As far as factoring my source code goes, I mostly copied the structure that Dan and I used for our piconot-external implementation, which has served me well so far. The only difference so far is that the semantics package will contain multiple different backends, all with the same API (a void function called execute), as opposed to the one in piconot-external.