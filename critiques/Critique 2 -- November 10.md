This week, Kevin asked me to examine and make suggestions pertaining to the API of SimpleEMS. 
Below are a list of suggestions, questions I had, or things to think about as I read through the code (in no particular order)

- It seems like your scheduler is only capable of handling one week's worth of scheduling. Is this something you plan to 
change in the future? In particular, the 7 in `val days = Array.fill[Schedule](7)(Schedule());` feels like a magic number, and
limiting the user's options like that seems unfortunate.
- It looks like the RoomManager is in charge of handling incoming requests from the user. Should the function to reserve a room 
be in the RoomManager instead of Schedule? Alternatively, if Schedule is the entry point for queries, I'd put the "top-level 
functions" like getSchedule or getAvailableRooms in there. 
- More generally, have you thought about what the entry point for the semantics of the language will be? 
- Do you have any intention to explore concurrency? You could imagine multiple people querying the EMS at the same time
(this is certainly not a necessary feature, but might be cool to explore if you end up with extra time on your hands).
- It seems that your implementation makes the hour an atomic unit of time. I feel like this isn't easily extensible - you could 
imagine someone trying to schedule a room for shorter meetings. Would it be possible to allow the user to specify the smallest
time interval that the system will handle, and then do some math to figure out how many slots to schedule? 
- A nice feature I thought of: a lot of times, when a room isn't available at a particular time, you might want to reserve that 
room at a similar time (maybe a bit before, or after). Many scheduling systems resolve this with a calendar-like visual interface,
where you can see a room's availability for a day all at once. Would there be a way to build in 
the capacity to say `room unavailable during desired time, but available near desired time.`
- Another important consideration for EMSes is the capacity of a room. Do you plan to add capacities as a consideration in the EMS?
(I imagine that this would affect the Room class and how much info the user needs to specify, at the very least). 
- Will you implement a functionality that enables users to override someone else's reservation of a room? 
(this would require the concept of user priority) You could imagine, for instance, at Mudd the administration has the 
power to override a student group's reservation of a space (this happened to DUCK! last ASP). 
- Another relevant piece of room metadata: Location. You could imagine people wanting to reserve a room in the Shanahan building
specifically, or needing a room to be on the first floor for disabled students.
- Since your computational model is basically a constraint satisfaction one, how could you implement priority for constraints?
(for instance, maybe you want a room on the first floor and in the Shanahan, but being on the first floor is more important)
- Do you plan to write things disk? Which things? I assume that having data be volatile would 
be very bad for an event management system. 

Note: I've tailored most of my suggestions to an EMS for a school like Harvey Mudd's facilities. You mentioned in your 
notebook entry for this week that the EMS isn't necessarily aimed at replacing F&M's current one, so my suggestions may be
missing features that EMSes for non-school systems might require, but I'm sure some of these things are generalizable. 
