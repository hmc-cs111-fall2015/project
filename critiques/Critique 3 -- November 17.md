# Notebook Critiques
For modifications, I think you could work towards using a decorator design pattern.
Each type of ingredient is a little object (or class) and then your pre-specified drinks have these objects perhaps with the quantity somehow stored within your data model. This should make the design of your code fit intuitively to how your drinks are being forms.
For the syntax, I don't think you have to worry about the specific words for now. You can build in syntactic sugar later, and just use some placeholder words for now or choose a syntax that is easy to implement.
As a suggestion for syntax, I think you should parse it the same way as a command, but modifications will have to come before the command to make a latte or add half a latte to the drink. (Kind of like drink 'states' and changing the latte 'state' to being without coffee.
Or in the parser, you can recognize another set of classes that modify drinks and have them modify the drink object, add the drink object, then reverse the changes to the drink object.
So, I think what you ultimately need is a data model that represents different drinks, and a way in the langauge to define new drinks.

Try to get in your 9 hours! 
It's like getting 8 hours of sleep everyday. 
(Though, I would hope you prioritize the sleep and not work).
Hope your next week goes better :-)

# Project Submission Critiques
_No submission due this week_

# Code Critiques
There isn't much to say here -- Everything looks pretty tidy and it's easy to understand.
If you want to start modifying drinks, I think your parser will have to be able to recognize when a line is modifying a drink.
I am unsure where drinks are actually defined -> is that for your backend to do? How do users define what different ingredients are and how is that consolidated with what your backend/final output will decide what each ingredient is?
Do you plan on enabling users to define mixtures of ingredients?
Do you plan on building an ir that includes a data model or is the langauge stritly for parsing commands into a set of instructions?
