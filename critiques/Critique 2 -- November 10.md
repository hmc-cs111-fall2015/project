I think the sample program is a good first iteration of the syntax/semantics
that offers a sense of the language's potential.
The states definitely provide a good sense of the state machine representing the robot.

Our in-class discussion seemed to culminate around the idea
of supporting states for subsystems of a robot (i.e., wheels, arm, sensors):
each subsystem can operate 'independently',
and it seems like it might be appropriate to provide syntax
so that users can better isolate the logic of each subsystem.
One concern with the idea of providing this isolation through state machines
is that these state machines will likely often need to communicate.
For instance, it might be the case that if one subsystem's state machine enters a certain state,
then _every_ subsystem state machine needs to enter a particular corresponding state;
so in designing the syntax, I'd be careful to make it explicit within a state machine
when its state _can_ be changed rather than having a notification sent to the state machine
that sort of silently changes the state.

I'm actually warming up to this model because one can create a state machine out of the sensors,
wherein the sensor is potentially always reading data and changing state based on the data,
then other state machines just check the state of the sensor.

-Justis Allen
