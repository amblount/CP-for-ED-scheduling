# Defining the problem

I spoke with a few other scientists in the insights program to try and understand what types of algorithms might be appropriate 
to solve this problem.

Here are a few which were suggested:

- learning algorithms
- genetic algorithms
- diversity algorithms
- linear programming

Thinking through how reinforcement learning could be used to solve the problem:

- If we have residents and shifts defined for a 28 day period or 4 weeks, we can assign residents to shifts one by one looping through 
the set of residents and at each assignment we can create a policy which will interpret how well the system did with that particular assignment
given the system constraints. In this system we would need to define the set of [state, action, rewards] and then interpret how well the system did at each step.

- We could also randomly assign the residents to shifts for a 28 day period and then create a policy for the entire schedule and weight the 
policy according to the way it performed according to the system defined constraints. With this time of set up it would be much more difficult
to determine which exact step violated the constraints. In this situation we could assign a negative reward to every resident shift combination
which violated one of the hourly constraints and then sum up the rewards from each schedule produced by the system.

