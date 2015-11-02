# Project plan

## Language evaluation

I'll deem [Codeviz] a success if users can generate simple,
`if`-`else`-based flowcharts without much effort. To evaluate the language _design_,
I'll consider ease of use in the underlying language,
in particular I plan to use the language to generate flowcharts
for solutions to CS 5 or 60 assignments.
To ensure that language _implementation_ is of high quality,
I'll consider how easy it is for other programmers to adapt other programming languages
or flowchart creators to my flowchart abstract syntax.

Critiques will also help with both design and implementation quality. :relaxed:

## Implementation plan

Here's a draft, week-based schedule of what I hope to accomplish each week,
beginning with the week 'ending' (based on course-weeks) on November 8:

1. Create comment parsing proof of concept,
and design flowchart abstract syntax (start with actions and conditions)
2. Map parsed comments (just actions, no conditions) to flowchart abstract syntax,
and find 'fitting' flowchart creation language
3. Map flowchart abstract syntax to flowchart creation language (just actions),
and make Codeviz command line operational
4. Actually parse conditions, map flowchart abstract syntax conditions to flowchart creation language,
and add syntax errors
5. Add support so that whenever a function call appears,
the description for the function is added to the flowchart
6. Allow user to specify what functions should have flowcharts generated
7. Add `for` loop support

[Codeviz]: https://github.com/JustisAllen/Codeviz
