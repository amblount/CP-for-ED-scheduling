# Contraint Programming
Project Description | [Blog Post](https://medium.com/@aliviablount/automating-scheduling-for-ed-residents-at-ucsf-a2aa8b9ab880)

Emergency rooms are open 24 hours a day, 7 days each week and need to be scheduled around the clock. There are only so many physicians working in a particular network who can cover those shifts. The emergency department is specialized and therefor only physicians specialized in this area are able to take these shifts.

### Consulting Project

I worked with the University of California, San Francisco (UCSF) to automate their emergency resident scheduling process given a set of defined constraints.

### Modeling the Problem before consulting with the team
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-09-13%20at%205.53.07%20PM.png)

### Reinforcement Learning solution case statement

I am very interested in diving into the field of reinforcement learning and I wanted to play around in the open AI gym and explore solutions to the scheduling process using reinforcement learning. I started the process with the following case statement:

Currently, rules (control policy) for the mechanical operations (control loops) of most sophisticated machinery are set by human experts, which require tremendous time and domain expertise. If we can teach machine to learn these rules and reduce the reliance on scarce human experts, that has far-reaching impacts across all manufacturing fields.

The complexity and diversity of control loops in hard technologies like metal 3D printing makes them a good candidate for Reinforcement Learning (RL). RL algorithms usually require a lot of trials and it is expensive and dangerous to run physical trials. But combining RL with simulation will not only optimize the control policy for more efficiency and time saving, it also can disrupt manufacturing by developing new methods that require less complicated machinery.

Use case:

- Scheduling of emergency medicine doctors in inner city hospitals

Deliverable:

Deep reinforcement learning as a service platform that can learn a policy using a specific simulation environment or existing dataset. The service needs to interfaces with the engineer to gather the model and objective function and potentially take advantage of imitation learning and off-policy learning to improve the speed of convergence and gather bounds on each parameter to help reduce search space. The service should take advantage of asynchronous and parallel deep RL techniques to speed up the learning process as well. The accuracy of policy should exceed human generated policy. 

### Scheduling Constraints
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-09-19%20at%204.13.07%20PM.png)

### Deliverable | [Link](https://ucsf-er-resident-scheduler.firebaseapp.com/)
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-10-01%20at%203.14.25%20PM.png)
