_Critiquer: Matt Valentine_

I decided to use StateOfTheRobot to implement a mockup of a polite robot
that knows how to pass butter. In doing so, I suppose that I noticed
a few things.

## 1. Substates

I think that the interface you have for substates is excellent.
The only real difficulty is that its impossible to name the substates.
How could you manage to name them? I can't think of anything really,
unfortunately,
except making an unrelated enum that happens to have the right number
of entries.

It also seems to me that though it would be possible to have arbitrarily deep
nestings of state-like structures, and that would solve this problem in a
way, that would be a horrible thing.

So I think it's just about as good as it can be as-is.

## 2. Acutally Doing Things

So, the assumption that function calls are instant is an interesting
one. So I was wondering how you would go about doing something like
telling the robot to turn, for example.
If it was possible to call a function "startTurning", which asynchronously
starts the robot turning,
and then also a function "hasTurned" or something that tells you when
the action is complete,
then you can do something like

    state_func(A, [] {
      startTurning();
      next_substate();
    }, [] {
      if (hasTurned()) {
        next_substate();
      }
    }, [] {
      ...
    });

I don't know if this busy-waiting is the intended way to do this.
But I think it would be good to have a specific idea in mind of how
exactly users should do this kind of thing.
In other words, how should users do actions that take time?

(One problem of this set-up is that there's no
chance to STOP TURNING when an interrupt happens,
unless every interrupt was going to do something like
"if state == turning stop turning".)

## 3. Random stuff

I'm not sure what the purpose of  
`if (sf.substate < sf.subfns.size())`
on line 53 of `StateOfTheRobot.h` is;
or rather, why you just ignore it and do nothing if the
substate happens to overrun its bounds. (Easy to do
since users just put in bare ints.)


