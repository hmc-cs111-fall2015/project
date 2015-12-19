
_Anna Pinson_

One thing that comes to mind, with respect to the two different models, is that if the positions/topic areas have to be specified by the instructor, it may be possible to have a simple spellchecker that can use the words given by the instructor as the "dictionary" to check against.
But then, on the other hand, if the users can input the positions/topic areas, that gives them more freedom.
One possibility is to go with the first implementation and also output a list of any words that can't be successfully caught by the spellchecker;
for example, the "error" of each word is calculated, and if it's small enough then it's matched to the word it's probably trying to be. Otherwise, add it to a list of "student-generated positions/topics."

Of course, since this is going to be a giant CSP DSL, the easiest route is just to let the instructor specify things and print out the words that don't make sense.
Besides, if a GUI is ever implemented, it might be possible to just have the students pick things from a dropdown list populated from the instructor's specifications.

I'm not quite sure how, but producing a conflict level along with a solution would also be good.

Something to consider: suppose students think they don't have a preference, but they actually do when presented with different options (which is definitely something that happens).
Should your DSL give all possible solutions? Or perhaps the instructor can say how many solutions they want, and then pick between them.
Also, could the instructor also add some general constraints? Say Jake and Josh are best friends and want to work together, but the instructor knows that they're liable to slack off and do no work if they're on the same team.
Perhaps the DSL could filter out any solutions that violate the constraint if there is at least one that does not, and if there are none then warn the instructor that this is the only solution that works.

Essentially, if there was a way to get second or third best solutions as well as optimal solutions, this may be useful, both for the case above and for cases with no solution.
