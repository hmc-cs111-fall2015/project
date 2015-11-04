**Zoab's comments**

Note: I'll group some of my critiques by the section of the project plan/description that I'm responding to.

## Language evaluation

How do you plan to weigh the three proposed metrics in terms of importance? I would suggest using ease-of-use as the primary metric - 
I think that a smaller DSL which is easier to use is better than a big one with a bad UX.

## Implementation plan

What do you mean when you say that a back-end would be neat? You seem to imply that a back-end isn't necessary 
for the project to be complete. By back-end do you mean something different from the semantics of the language? If not,
I'd argue that having **some** back-end is essential to having a finished product. 

Also, I like your implementation plan! I think error handling would be a good thing to spend time on, it'll give 
the language a more polished feel.

**end Zoab's comments**

**start of Alex's comments**

So I will take a different approach and just talk about your language.

A lot of this language seems dependent on a system Mudd uses to track room availability. 
Is there a current system that you are augmenting or is this brand new? If there is already
a current system, then you already know what you need your backend to fit to, an API of sorts
to work with the current system. As the expressibility of the backend is what really defines 
what your language is able to do, my main question is **why aren't you working on the backend
first?** With picobot, we worked on the middle part first because we already had a well defined 
goal we wanted the backend to achieve. Since it doesn't seem like yours is completely ironed out,
it might help define the language more to define what the backend will be doing. 

For host language, I don't think you should really decide on that until you have a couple sketches 
of what you think the language should look like. Picking a host language before doing sketches is 
picking a method of writing the solution to a problem before having the solution. 

I think your next steps should be more concretely define what you want the language to do and what
system you are dealing with that stores all of the room/schedule information. As we said in class,
the standard direction for a DSL is API -> Internal -> External, so it might be helpful to start 
with the API. 
