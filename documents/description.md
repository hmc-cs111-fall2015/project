# Project description and plan

This project serves a group of people who share a set of spaces and need to use the spaces at various times. Examples include kitchens, lab spaces, and study room. This language would be good for any user to reserve a space or designate the space as 'occupied'. The project involves three main components, an intermediate representation, a front-end and a back-end. The plan is to develop in that order as well. The intermediate representation will take the front-end language and convert it into object relations for the back-end. The front-end will be the outer language for users to interact with space and event management. The back-end will hold the persistent objects and information about rooms.

## Motivation

This project is interesting to me because it solves one of my frustrations at Harvey Mudd. When I try to organize events, I find it frustrating to check multiple dates and times or try to do multiple reservations. A DSL is an appropriate solution because the management system needs to be intuitive so that any user will be able to use the system without burdensome training.

## Language domain

The domain of this project is the event management domain.

## Language design

The design of this language is a text-based query system.

A program in this language is a clause or set of clauses that query or change the data model.

When a program runs, the program is interpreted into the data model and which then translates the database info into the desired information. Or translates changes in the data model to database changes.

The program takes string inputs, such as room names and times, and produce string outputs.

Syntax errors are possible, which will need to be caught in the parser. Compile-time errors will likely not be an issue, but run-time issues may occur since there may be discrepancies between the data model and the database. These errors should be handled with comparisons between the data model and the assumed data model.
I will need to design the language to catch foreseeable errors and also prevent users from changing data models in an inconsistent matter.

## Example computations

When asked for when a room is open, the program should check the schedule for that room and then return the schedule.

When asked for what rooms are open at some time, the program should check the schedule for that time period and then return the rooms that are open.

When asked for the schedule, the program should show a list of rooms and their availabilities. 

When a room is requested, the program should check the schedule for availability and then return whether the reservation was successful or not.

Each of these requests could be combined to automate looking for an open room.

