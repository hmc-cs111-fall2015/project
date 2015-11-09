# Language design and implementation overview

## Language design
A user writes programs by writing their robot code in C++ but use my DSL for logic features. The basic computation is to move between states in a state machine and call user-provided functions when they asked them to be called. The only real data structure in my DSL is the state of the robot. The state is primarily modified by the user, but things such as `wait` can create shadow states that are mostly user-hidden.

My DSL has lots of control structures. The biggest one is just functions, which largely act as callbacks. The user defines what to do in each state, what to do when a certain external event happens, and what to do in the background, and my DSL calls the functions at the appropriate time. But there's also some control structures that are harder to understand, such as `wait` which acts like a busy wait but keeps calling background functions and interrupts.

The input to my DSL can be said to be these functions that define what to do in each case. The output is working robot logic code. One could also say that the input and outputs are those of the robot as it moves around. Programs can go wrong with syntax errors or logic errors. I don't really have a way to catch most logic errors, but the robot will just do the wrong thing. Warnings can be thrown when something like an undefined case happens. A development environment is not in the scope of the project. As far as I know, there aren't really any other DSLs in this domain.

## Language implementation
I chose to use an internal DSL with C++ as the host language because the logic interacts very closely with the actual running of the robot, and I wanted to target arduino which is written in C++. Since the C++ syntax is pretty constraining, I haven't gotten to make many syntax decisions, except for when I'm defining things like macros and have to wonder how weird versus nice I should make them.

The architecture of my system will hopefully just be a library that one can include and then link against to get all the features. Users specify some robot-specific things at the top, such as how to get the time, and then define their states and write code for how to deal with each state and how to transition.
