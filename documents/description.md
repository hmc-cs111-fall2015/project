# Project description and plan

## Motivation

This project is motivated by the lack of complex calendar creation 
tools available today. While most people's schedules might not
change that often throughout the course of the year, a subset of
the world does not have that benefit. Having an event be active 
for two or three date ranges but not another is not an easy task
to achieve in the usual calendar creation tools. We seek to solve
this problem. 

This is an interesting project because it seeks to give users a lot
of expressibility, since the end goal is definitively a complex
calendar. But the project seeks to do this while only requiring the 
user to write the bare minimum required to express their ideas. 
This concept of allowing vast expressibility with a simplistic 
language really intrigues me. 

This isn't a strict limitation of the language but it should be noted
that this language is mostly suited for repeated events rather than
one-off events. The language of different rules and times affecting
events gives a lot of expressiveness to repeated events but almost 
none to one-off events. 

A DSL is an appropriate solution to this problem because DSLs generally
seek to improve expressibility in the simplest way. Not only that,
but having a text based language lends itself to easy reuse of code
and templating that I think would really improve the experience of 
creating a calendar. 

## Language domain

The domain that the language addresses is complex calendars. 
This would be for those that need a complex calendar design and don't
have the time and patients to hand add and remove events in their 
calendar of choice. An example user would  be 
a student who has two different semesters with different classes. 
Each class meets at the same time each week, but there are breaks
and holidays during which class doesn't meet. Finals week also has
a different schedule requiring a different set of events in a 
calendar. The act of making a calendar this complex kind of 
defeats the purpose of making a calendar in the first place,
saving time. So I seek to make a calendar creation tool for people
who have difficult schedules like this. 

There aren't truly any other DSLs in this domain, but the library 
I plan on using [ical4j](https://github.com/ical4j/ical4j) has the 
ability to add events to an icalendar file, which every major calendar
is able to import. SO you could say icalendar is a DSL for representing
calendars. I plan to use icalendar as my output, so that it has the
most functionality for end users. 

## Language design

One sentence:

Calendar events defined by scoped descriptions and repeated inside
their bounded dates. 

The language itself does not take any input. There is room for templates
and multiple document definitions, but no true input is being taken 
in. The ideal output is a calendar format that can be imported by any
calendar client; icalendar seems like the best option for this. 

The error that seems most likely to occur in this domain is overlapping events.
From talking to others though, this shouldn't necessarily be a problem when
creating a calendar, so overlapping should be allowed, unless specified 
otherwise. An error that could occur that is more specific to my DSL is 
date ranges that are defined on an event that don't agree with one another.
The options here are to have a strict definition of what definitions take 
precedent over others or to have errors that warn the users of this happening. 

To help prevent the dates disagreeing with each other for a specific event,
the idea of precendence of the date that was defined the closest to the 
definition of the event, scope wise, allows users to be able to predict which
dates will actually be used. I don't think the problem can be entirely removed
since we are trying to give the user as much expressibility as possible. 

## Example computations

The perfect example of what the DSL should be able to compute is a 
college student's schedule. 

The college student first wants to define the date range that school is in
session for them excluding breaks and holidays. The user then wants to define 
classes that fit inside this schedule, that this date range is applied to. 
Each class has a different time but they all should follow the same date range. 
They define the class on a weekly basis and designate it as a weekly repeated
event. 

The student then runs the DSL and gets an icalendar file that should contain
events for all their classes according the rules they defined. They can import 
this icalendar file into google calendar or any other major calendar client
for convenient use. 


Another example could be a business man that travels between two or more 
different offices. While he works for the same team, he talks to different
people at different times while at each office. He wants to make a calendar
program that can create his schedule with him just putting date ranges for which
he will be at each office. He will define a different section for each office
which each containing the times of each meeting he has at that office. Each
time he gets a new list of dates, he can just put those into the definition of
each section, compute the DSL, and get his calendar for his specified period of
time. This makes the process of creating complicated schedules much easier. 
