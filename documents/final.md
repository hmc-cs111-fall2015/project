**Introduction:** 
_A short description of the SimpleEMS project_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project serves website designers who seek to create an event management system, or reservations system. These systems in turn serve a group of people who share a set of spaces and need to use the spaces at various times. Examples include kitchens, lab spaces, and study room. This language would be good for any user to reserve a space or designate the space as 'occupied'. The language also seeks to descibe rooms, so that users can also define a set of rooms. I took on this project because it solves one of my frustrations at Harvey Mudd. When I try to organize events, I find it frustrating to check multiple dates and times or try to do multiple reservations. A DSL is an appropriate solution because the management system needs to be intuitive so that any user will be able to use the system without burdensome training. This langauge draws ideas from SQL, and JSON to provide easy to read descriptions of reservations and rooms while allowing users to query against a constraint solver. SimpleEMS is an appropriate language because it will act as an easy to read intermediate langauge for those who wish to write GUI's for reservation systems.


**Language design details:**
_A high level overview of the SimpleEMS design_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users write 'programs' in SimpleEMS by typing out descriptions of queries and rooms. As part of a larger system, the queries then get information from a local data model that draws information from an external data source such as a database. The requests ask for changes that are then interpreted to changes in the data model which then makes the appropriate changes to the external data source. The syntax allow for users to write code that is easy to understand and alter since we have scoped down the words and data types that users can use. Currently, the language supports ints, strings, and dates as field values. The language currently is set up to parse, and then return a mapping of fields to values. While this language was designed for schedule constraint solving, there was not enough time to implement one for this project (especially considering that I switched the language I was developing). So, the language will simply provide a mapping that can be plugged into a constraint solver library with some wrapping to provide calendar functionality. The basic data structure it the very map that users are manipulating when they write out their program. The DSL requires text inputs in the forms of the example programs shown later. DSL currently outputs a data structure, but the add-on will print out the mappings to show that it works. Because of the late switch, there is no error-checking or development environments. These types of features would be the next step in the process of developing this language. For 'functionality', many JSON libraries provide the same type of functionality because they are showing mappings. However, JSON can syntactically frustrating and this provides a simpler way of describing fields and values. For event management, I do not know of another langauge that provides an intermediate representation between the interface and the constraint-solver.

**Example program(s):** 

Describing rooms:

```
room {
    building : 'Parsons';
    name : '2470';
    open : '8:00AM';
    closed : '5:30PM';
    occupancy : '14';
    type : 'classroom';
}
```

This 'program' would have no output since it is a static description for the back-end to build into its data-model.

Describing a query:

```
reserve {
    start : '8:00AM';
    end : '9:00AM';
    date : '12/8/2015';
    occupants : '11';
    type : 'classroom';
}
```

Ideally, this query would output some sort of success or failure. On failure, it would provide some constraint suggestions, like expanding the list of possible dates.
For now, it simply builds the mapping from fields to values.

**Language implementation:** 
_A description of the language's implementation_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I chose to implement SimpleEMS in Scala because this is not a language I am very familiar with, and I wanted to learn how to use the langauge in depth. SimpleEMS is an external DSL. I chose to implement an external DSL because the built in syntax for Scala is not well suited for describing queries. In addition, I have never written an external DSL, and this was another way to explore how implementation would work. The parsing is done by the PackratParser which translates the program to an abstract syntax tree. The AST is the intermediate representation. The execution is handled recursively, where the map is built by traversing the tree and 'filling in' nodes from the bottom up. Ideally, the execution would also involve some constraint solving on schedules but again I did not quite get to it and I did not prioritize it since it was more of an implementation issue than a language issue.

**Evaluation:** Provide some analysis of the work you did. In
particular:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This language is very DSL-y. It is only capable of describing fields and values. There is no control flow, or a way to have fields interact with one another. This language makes it very easy to describe a few parameters for rooms and reservations. I like that it is easy to read and write. There are a number of ways that it can be improved... I think with another week or two I would implement variables as well as write a wrapper for a constraint solver to deal with making actual reservations. For the user experience, I would implement a GUI since I think that is the most intuitive way for users to interact with dates and times. (A temporal-spatial connection!) My current implementation is a small part of a larger solution to the initial motivation to this problem. Honestly, the biggest set back was learning the langauge and learning how to mold the PackratParser to my needs. I started with a language design that looks more like SQL queries. However, they were hard to read and hard to implement. The queries didn't fit the needs of describing new rooms either. I went with descriptors to make it easier to read, and a syntax I was more familiar with implementing as a language. They make new rooms make much more sense. I think the ideal medium would have been two languages, a descriptor type for room and a query type for reservations. I made large changes to the language after reading back over my critiques and after getting fed up with some of the road blocks I met with implementing the first language. I found the syntax difficult to implement, especially in a language I was unfamiliar with. There were some features that peer critiques said wouldn't be possible, and that is a big reason for switching. 
