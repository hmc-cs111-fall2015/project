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
Since this is a static language, there aren't really any control structures
in place. 

As mentioned before, the DSL takes in a file containing the text language and outputs an ical file that calendars import. The only
errors that can occur in this process is through incorrect syntax written by the user. Though since PackratParser was used,
syntax errors are nicely shown in the error output by the program. Currently, users using the website don't have an easy way
of seeing errors. They have to look in the file that is returned to them. 

The only other DSL for this domain is [ICal](https://en.wikipedia.org/wiki/ICalendar), which is a very hard to write file format. My DSL is more of a DSL for ICal though,
so I'm not sure if you can consider them in the same domain. 

# Example

## Input

Here is an sample calendar for my spring semester.

```
settings {
	time-format: "hh:mm a",
	date-format: "MM/dd/yyyy"
}

calendar school-calendar {

    section classes {

        dates {
            includes { 1/19/2016 - 5/4/2016 }
            excludes {  3/11/2016 - 3/20/2016,
                        3/25/2016 }
        }

        section mudd-classes {

            dates {
                excludes { 5/1/2016 - 5/4/2016 }
            }
            event algorithms {
                times { weekly( 11:00 am - 12:15 pm MO, WE, FR ) }
            }

            event interaction-design {
                times { weekly( 9:35 am - 10:50 am TU, TH) }
            }

            event macroeconomics {
                times { weekly( 2:45 pm - 4:00 pm MO, WE) }
            }

            event clinic {
                times { weekly( 11:00 am - 12:15 pm TU) }
            }

            event colloquium {
                times { weekly( 4:15 pm - 5:30 pm TH) }
            }
        }

        section other-5c-classes {

            event intro-to-acting {
                times { weekly(1:15 pm - 3:45 pm TU, TH) }
            }

            event squash {
                times { weekly(9:00 am - 9:45 am MO, WE) }
            }
        }
    }

    section finals {
        dates {
            includes { 5/9/2016 - 5/14/2016 }
        }

        event senior-finals {
            times { daily(8:00 am - 5:00 pm)}
        }
    }
}
```

## Output 

Here is the contents of the outputted ical file:

```
BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160120T110000,20160122T110000,20160125T110000,20160127T110000,20160129T110000,20160201T110000,20160203T110000,20160205T110000,20160208T110000,20160210T110000,20160212T110000,20160215T110000,20160217T110000,20160219T110000,20160222T110000,20160224T110000,20160226T110000,20160229T110000,20160302T110000,20160304T110000,20160307T110000,20160309T110000,20160321T110000,20160323T110000,20160328T110000,20160330T110000,20160401T110000,20160404T110000,20160406T110000,20160408T110000,20160411T110000,20160413T110000,20160415T110000,20160418T110000,20160420T110000,20160422T110000,20160425T110000,20160427T110000,20160429T110000
DTSTART:19700101T110000
DTEND:19700101T121500
SUMMARY:algorithms
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160119T093500,20160121T093500,20160126T093500,20160128T093500,20160202T093500,20160204T093500,20160209T093500,20160211T093500,20160216T093500,20160218T093500,20160223T093500,20160225T093500,20160301T093500,20160303T093500,20160308T093500,20160310T093500,20160322T093500,20160324T093500,20160329T093500,20160331T093500,20160405T093500,20160407T093500,20160412T093500,20160414T093500,20160419T093500,20160421T093500,20160426T093500,20160428T093500
DTSTART:19700101T093500
DTEND:19700101T105000
SUMMARY:interaction-design
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160120T144500,20160125T144500,20160127T144500,20160201T144500,20160203T144500,20160208T144500,20160210T144500,20160215T144500,20160217T144500,20160222T144500,20160224T144500,20160229T144500,20160302T144500,20160307T144500,20160309T144500,20160321T144500,20160323T144500,20160328T144500,20160330T144500,20160404T144500,20160406T144500,20160411T144500,20160413T144500,20160418T144500,20160420T144500,20160425T144500,20160427T144500
DTSTART:19700101T144500
DTEND:19700101T160000
SUMMARY:macroeconomics
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160119T110000,20160126T110000,20160202T110000,20160209T110000,20160216T110000,20160223T110000,20160301T110000,20160308T110000,20160322T110000,20160329T110000,20160405T110000,20160412T110000,20160419T110000,20160426T110000
DTSTART:19700101T110000
DTEND:19700101T121500
SUMMARY:clinic
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160121T161500,20160128T161500,20160204T161500,20160211T161500,20160218T161500,20160225T161500,20160303T161500,20160310T161500,20160324T161500,20160331T161500,20160407T161500,20160414T161500,20160421T161500,20160428T161500
DTSTART:19700101T161500
DTEND:19700101T173000
SUMMARY:colloquium
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160119T131500,20160121T131500,20160126T131500,20160128T131500,20160202T131500,20160204T131500,20160209T131500,20160211T131500,20160216T131500,20160218T131500,20160223T131500,20160225T131500,20160301T131500,20160303T131500,20160308T131500,20160310T131500,20160322T131500,20160324T131500,20160329T131500,20160331T131500,20160405T131500,20160407T131500,20160412T131500,20160414T131500,20160419T131500,20160421T131500,20160426T131500,20160428T131500,20160503T131500
DTSTART:19700101T131500
DTEND:19700101T154500
SUMMARY:intro-to-acting
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160120T090000,20160125T090000,20160127T090000,20160201T090000,20160203T090000,20160208T090000,20160210T090000,20160215T090000,20160217T090000,20160222T090000,20160224T090000,20160229T090000,20160302T090000,20160307T090000,20160309T090000,20160321T090000,20160323T090000,20160328T090000,20160330T090000,20160404T090000,20160406T090000,20160411T090000,20160413T090000,20160418T090000,20160420T090000,20160425T090000,20160427T090000,20160502T090000,20160504T090000
DTSTART:19700101T090000
DTEND:19700101T094500
SUMMARY:squash
END:VEVENT
BEGIN:VEVENT
DTSTAMP:20151211T163632Z
RDATE:20160509T080000,20160510T080000,20160511T080000,20160512T080000,20160513T080000,20160514T080000
DTSTART:19700101T080000
DTEND:19700101T170000
SUMMARY:senior-finals
END:VEVENT
END:VCALENDAR
```


