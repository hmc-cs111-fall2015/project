# Project description and plan

## Motivation

Coffee drinks are difficult to make. In the world of the ever-present hipster, it's getting harder and harder to get it just right. In a world where customers actually order a "split-shot, heavy on decaf, 20 oz, soy, extra dry latte, with half pump vanilla & half-pump hazlenut", keeping track of all the modifications to make for a coffee drink is a difficult experience even for a physical barista. On the other hand, automatic coffee machines have a finite amount of settings that a customer can customize, so are not as customizable as ordering from a live barista. 

Introducing CaffeineScript: a standard language by which a customer could specify a drink to an arbitrary level of precision, then you could easily program an automatic coffee machine to make exactly the drink you want. 

We need a DSL for this because we want to enable users to specify their drinks to arbitrary levels of precision. There are so many factors that go into a caffeinated beverage that we need a language (rather than, for instance, an enumerated type), because there are just so many possibilities.

# Language design and implementation overview

## Language design

A user writes programs in CaffeineScript by creating a text file containing the instructions to be executed. In the future, I might build a GUI on top of the language to make it more friendly to non-programmers. I think all of the structure of the language should be translatable into a GUI. 

A program in CaffeineScript has 2 sections: the (optional) header and the body. Within the header, you can define recipes for coffee drinks which you can reference from the body of the program. In the body, you'll write the instructions to make the final drink that you want.

The basic building block of a program is the instruction. There are 4 different kinds of instructions: regular instructions, swap instructions, make instructions, and remove instructions. A regular instruction is used to add a certain quantity of an ingredient. a make instruction adds all the contents of a recipe that you defined in the header to the current drink. A swap instruction swaps every instance of some ingredient for another ingredient of your choosing. Finally, a remove instruction removes all instances of the ingredient in the recipe so far. It's important to note that swap and remove instructions only modify the ingredients that have already been added to the drink when they are executed or, equivalently, only modify instructions that precede them in the program.

Here's the syntax of a program: 
```
{ header } body
```
or 
```
body
``` 

The header consists of 0 or more recipe definitions, whose syntax is as follows:
``` 
RECIPENAME {
  recipebody
}
```
where the recipe name must be in all capital letters, and the body is a series of instructions of the 4 types mentioned above. A recipe should only be defined once in the header - creating 2 recipes with the same name will lead to undefined behaviour. 

Here's the syntax of the 4 basic types of instructions:
  - Regular instruction : `<verb> <quantity> @ <ingredient>`. For example, `scoop 2 spoons @ sugar;`.
  - Make instruction : `make <RECIPENAME>`. For example, `make LATTE`. If you have a `make <RECIPE>` in your program, `RECIPE` should be defined in the header of the program.
  - Swap instruction : `swap <ingredient1> -> <ingredient2>`. For example, `swap water -> espresso;`. This substitues in water for espresso for every instance of espresso that's currently in the drink.
  - Remove instruction : `remove <ingredient>`. This removes all instances of the ingredient specified that have been added before this line.

In an instruction, \<verb\> is any English verb (describing how to add the ingredient in question), \<quantity\> is 
a number followed by a word to specify how much of the ingredient to add, and \<ingredient\> is the name of 
the ingredient. For example, in the line `add 2 shots of espresso`, `add` is the verb, `2 shots` is the quantity, and
`espresso` is the ingredient. It's important to note that while an ingredient can contain multiple words, a quantity must be a number followed by 1 word, and the verb can only be one word. 

It's important to notice that the syntax of the language is very similar to the syntax of a general-purpose programming language, from the use of curly braces to demarcate sections of the program to the use of keywords to denote specific kinds of instructions. As is, the language wouldn't be as easy to use for a layman as for a programmer. My hope is that programmers would build a GUI on top of the language that would allow end users to use the language through a more intuitive interface. That said, the fact that the language is pretty small means that it should be quicker to pick up for a non-programmer than a general purpose language would be. 

One way in which a program can go wrong is if a user uses references a recipe in a make instruction that doesn't exist. In this case, I throw an IllegalArgumentException with an informative error message. I handle errors where the user tries to define two recipes with the same name similarly. Another possible error that I've considered is an error where two recipes reference each other. I haven't explicitly handled this case, instead trusting Scala to throw a StackOverflowException when this occurs. Some of the errors I haven't concerned myself with much are syntatictic errors, where a program doesn't get parsed correctly. The main reason for not considering these errors, or spending more time on semantic error handling was a lack of time - I had to make tradeoffs on which language features I spent more/less time on, and error checking didn't get as much attention as I'd originally thought it might.

The project doesn't provide any tool support, and I don't have any plans to make it do so. That stuff, while useful for a general purpose programming language, doesn't (in my opinion) have much place in a language as small as this. 

There aren't other DSLs for this domain that I know of. Kevin made a good point in one of his critiques that the machine that makes bottled Starbucks frappes could be using a DSL internally, but this is probably a proprietary language (if it exists), which is why I couldn't find it or learn from it when I was searching for other DSLs in this space. 

## Example valid program

### Input

```
{
    MOCHA {
        make LATTE;
        add 2 scoops @ chocolate powder;
    }

    LATTE {
        add 4 shots @ espresso;
        pour 3 oz @ milk;
        scoop 2 spoons @ sugar;
    }
}

make MOCHA;
swap water -> espresso;
remove milk;
```

### Output

```
adding 4.0 shots of water 
scooping 2.0 spoons of sugar
adding 2.0 scoops of chocolate powder
```

## Example invalid program

### Input

```
{
    MOCHA {
        make LATTE;
        add 2 scoops @ chocolate powder;
    }

    LATTE {
        add 4 shots @ espresso;
        pour 3 oz @ milk;
        scoop 2 spoons @ sugar;
    }

    LATTE {
        add 4 shots @ espresso;
        pour 3 oz @ milk;
        scoop 2 spoons @ sugar;
    }
}

make MOCHA;
```

### Output

```
[error] (run-main-0) java.lang.IllegalArgumentException: Recipe with name: LATTE is defined multiple times!
java.lang.IllegalArgumentException: Recipe with name: LATTE is defined multiple times!
	at caffeineScript.semantics.Transformer.package$$anonfun$transform$1.apply(Transformer.scala:15)
	at caffeineScript.semantics.Transformer.package$$anonfun$transform$1.apply(Transformer.scala:14)
	at scala.collection.immutable.List.foreach(List.scala:381)
	at caffeineScript.semantics.Transformer.package$.transform(Transformer.scala:14)
	at caffeineScript.main.Main$.main(Main.scala:22)
	at caffeineScript.main.Main.main(Main.scala)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
[trace] Stack trace suppressed: run last compile:run for the full output.
java.lang.RuntimeException: Nonzero exit code: 1
	at scala.sys.package$.error(package.scala:27)
[trace] Stack trace suppressed: run last compile:run for the full output.
[error] (compile:run) Nonzero exit code: 1
[error] Total time: 1 s, completed Dec 9, 2015 8:43:54 PM
make: *** [all] Error 1
```

## Language implementation

I chose to write an external DSL in Scala. I chose Scala partly to force myself to learn Scala (and functional programming paradigms in general), even though I may have been more comfortable in Java. In addition, I anticipated that many of my classmates might choose to write their languages in Scala, making it easier to go to them for debugging help (Also, Prof Ben knows the language quite well, which was helpful for debugging purposes).

Given that I was going to use Scala, choosing to make an external DSL instead of an internal one was a no-brainer for me. Three major factors shaped this decision:

1. I knew that my language wasn't really related to Scala's domain (ie, there was no need for my language's code to exist alongside regular Scala code). In particular, the language is targeted at a very narrow domain and wouldn't benefit from being in the same environment as regular Scala code.
2. Implementing piconot as an internal DSL was **way** more painful that externalizing it, and I anticipated the features of Scala hindering more than helping for CaffeieneScript as well.
3. CaffeineScript has a very different feel from Scala. The goal was to make a program sound like a recipe. This is not what programs in Scala read like.

As far as syntax goes, the first significant decision I made was designing the structure of an instruction as 
`verb + quantity + ingredient`. I also decided to not allow users to mix words relating to liquid ingredients and relating to solid ingredients (a program that tries to do this will fail to parse!). I think that this decision came from a place of wanting to force programs to be readable. While C may pride itself on allowing you to write obfuscating code, I want to force users to write readable programs in this DSL.

The only major architecture decision I've made so far (that I don't plan to change) is the decision to store a program as a list of Instructions to be executed. I feel like executing the instructions in sequence is true to the spirit of a recipe, and as I've mentioned before instructions in making a coffee drink don't commute in general. As far as factoring my source code goes, I mostly copied the structure that Dan and I used for our piconot-external implementation, which has served me well so far. The only difference so far is that the semantics package will contain multiple different backends, all with the same API (a void function called execute), as opposed to the one in piconot-external.