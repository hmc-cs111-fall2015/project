# Preliminary evaluation

IT WORKS!

I have the program out-putting a I-calendar file that imports into google calendar
and works correctly. I am pleased with the expressibility that the language can 
achieve. It should also be able to add in alternative date and time formats. 

## Things to improve on

So I know there are many different ways to express dates and times around the world. 
I would like to allow users to specify their preffered format or maybe just have the
ability to take in several types. (The problem with the latter is that Month/Day/Year
looks exactly the same as Day/Month/Year for a lot of dates). a

I am also considering changing the syntax to remove some of the curly brace requirements. 
Ideally this would involve some user testing to see how people feel about their differences
and weigh that with the confusion caused from a more simplistic(?) syntax. I think since 
some of the syntax requires commas, the braces become redundant. 

I have one bug. The last date in the date range specified won't have events added to it. This
might be hard to fix, but I know it is definitely possible. 

## Trouble 

I didn't really hit much trouble. It was hard to initially work with the ical4j API but after
I created my function that created events, I didn't really have to deal with it again. 

There was a slight problem in that not all calendars support every aspect of the icalendar 
standard. This means that outlook does not take in my calendar file. I have decided to just 
focus on google docs though as that is what most of my user base uses. 

## Initial Plan

I am track with my initial plan except on the syntax for templenting. I don't really know what
I plan to do with templating though and think that other features have a higher priority. So I
have been working on those and put templating on the back burner for now. 

## Future

I don't plan on changing the basic functionality of the language. I need to decide on how 
to allow users to specify their own settings. I am also considering allowing the possibility
variables to reuse time ranges. 

