# Introduction

The domain that the language addresses is complex calendars. 
This would be for people that need a complex calendar design and don't
have the time and patients to hand add and remove events in their 
calendar of choice. An example user would  be 
a student who has two different semesters with different classes. 
Each class meets at the same time each week, but there are breaks
and holidays during which class doesn't meet. Finals week also has
a different schedule requiring a different set of events in a 
calendar. The act of making a calendar this complex kind of 
defeats the purpose of making a calendar in the first place, 
so calendarscript seeks to allow those calendar users the ability
to create a fit-all calendar for their complex lives. Since most
calendar programs have import capabilities for ical files, my DSL
outputs that. 

The three basic data structures that calendarscript contains are 
```Calendars, Sections``` and ```Events```. Calendars can contain 
Sections and Events, Sections can contain Sections and Events. 
Events are just definitions though. This basically allows users to
scope different events into several levels of sections. 

This is a good language in this domain because it has a high level
of user customizability. Since the ```includes``` and ```excludes```
are basically just Ands and Ors for times, their inclusion in the
logic of the language allows for very complex date range combinations.
Users that will be using calendarscript hopefully don't need to make
easy calendars, so the ammount of overhead required to create a single
calendar is well worth it for the intended audience. 

# Language Design

Users write the language as a simple code. The syntax is simple enough
that users should be able to see code from the sample program and copy
and paste it into their program, if they are not use to programming. 
There are basically 2-3 different types in the language, which makes it
rather easy to read and understand. By restricting the users to these
2 or 3 types, it should restrict the way they think about creating the
program. 

The computational model of this language is just a static set of date
definitions that are evaluated against each other. So the computation 
being ran is a static scan of events and each set of dates that it is
associated with. 

The three basic data structures that my DSL contains are ```Calendars, Sections``` and ```Events```. Calendars can contain Sections and Events, Sections can contain Sections and Events. Events are just definitions though. The Language looks like this

```
Calendar := name Dates Filler

Section := Dates Filler

Filler := Section | Event | Section Filler | Event Filler

Event := name Times EventComponents
```

The main way that users can manipulate these structures are through scoping 
different events with different dates. That is the main purpose of the language.
The DSL also contains user settings, but those are just defined as strings. 
