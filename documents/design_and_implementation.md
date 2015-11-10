# Language design and implementation overview

## Language design

A user will use the DSL by writing a script and ideally putting it into a GUI. Initially though, the user will use command line 
arguments to set the file that the language will evaluate. The DSL then evaluates the language by converting it into ical4j 
which will then be converted into an ICalendar file.

Data Structures:

The three basic data structures that my DSL contains are ```Calendars, Sections``` and ```Events```. Calendars can contain Sections and Events, Sections can contain Sections and Events. Events are just definitions though. The Language looks like this

```
Calendar := name Dates Filler

Section := Dates Filler

Filler := Section | Event | Section Filler | Event Filler

Event := name Times EventComponents
```

There is a bit more to this but this is the overall jist. 

The control flow of the DSL is dictated by the scoping of events. Since sections can be part of other sections, the dates
that define an event can be quite complex with different date ranges defined as included or excluded. Users are able to define
this complex date definitions by their use of scoping.

There are no errors possible currently, since the language just follows definitions, but there are opportunities for warnings 
given to users in the future.

Other DSLs in the domain include icalendar which is a file format that defines calendars and is used by the majority of 
popular calendar hosts as a type of import and export for calendar data. Since it is widely used, I will be exporting to it,
making my DSL a wrapper for ICalendar.

## Language implementation

I chose external because of the similarity my language has to the picobot external my team created, and so that when others 
use this DSL in the future, it can be made in a way that they won't even have to deal with Scala. Host language was chosen 
because of the same reason. I have used it to create an external DSL and the one I created with it is pretty similar to 
calendarscript.

Since date definitions can overlap, I have decided to make it so definitions closest to the event have priority over those 
made farther away from the event, scope wise. To do this, we can't just make a recursive definition of these Sections, the
sections must pass their dates to the events and sub-sections contained within, so that it is known which definitions are
the most important. This increases the complexity of the implementation but should allow for most expressibility for the 
user.
