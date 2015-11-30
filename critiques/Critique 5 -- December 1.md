Critiquer: _Justis Allen_

I think the utility of multple states depends on the dependency
of each component of the robot (which likely varies by robot).
If users are forced to use a 'different' state machine for each component,
and the components are dependent on the same conditions,
users might end up repeatng themselves a lot
(e.g., changing the state under the same condition,
all states in each machine have the same names);
however, if users are forced to use a _single_ state machine
for a robot whose components are very independent,
users would also end up repeating themselves
because when one component needs to do something different,
all components enter the new state,
but continue doing the same work (about which users are explicit).

I think ideally there would be flexibility between the two concepts
by allowing the user to declare the names and number of state machines
they'd like to use at the top of the file.
Then it's up to the user to determine how best to divide the components:
maybe the robot has a single state machine,
maybe the wheels and leds often change state at the same time so they share a state,
but the arm is more independent, so it gets a separate state.
My main concern with this format is regulating
that a single component doesn't appear in separate state machines
such that the component is told to do opposing actions, but maybe this can just be user error?
I guess each component could be an object
and each object could only be associated with a single state machine.

I think my main concern with multiple states
was that the states would likely still be interdependent to some extent,
such that when one component enters a specific state,
all or some other states would need to enter a particular state.
I was concerned because I figured there should be some way to indicate
that one component's state machine can affect another
(particualrly in the state machine that can be affected by another
so that when reading this state machine,
it's apparent its state can change from another machine),
but this can already be achieved with `interrupt_func`.
So now I'm leaning more toward multiple states
because I don't think it would look terribly different from the current interface.

On an unrelated note, I must say I'm not fond
of the multiple-function substate syntax&mdash;at least when it's purely used to loop on a condition.
I understand not wanting to put a `while` loop within the implicit loop that is the state machine,
but maybe there could be a `wait_until(bool)` function
since in most cases it seems the substate that just contains an `if` is for sequential logic.
