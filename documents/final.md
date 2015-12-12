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
