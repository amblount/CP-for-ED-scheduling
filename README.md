# Contraint Programming
Project Description | [Blog Post](https://medium.com/@aliviablount/automating-scheduling-for-ed-residents-at-ucsf-a2aa8b9ab880) | [Deliverable](https://ucsf-er-resident-scheduler.firebaseapp.com/) | [Deck](https://docs.google.com/presentation/d/1smte-YGZOKlLCHbLX0G0h4l_VAnCZLc8aCQ_O2M8Flk/edit#slide=id.p)

Emergency room physicians are specialized medical providers who are only able to work in one section of the hospital; the emergency room. The ER is open 24 hours per day and 7 days per week. In any given network there are a given number of ER physicians available and these physicians must be shared amongst the facilities, we can think of a facility as on particular emergency room in a specific hospital with a full staff requirement. The full staff requirement is met when the target number of physicians per shift is scheduled for a given period of time, say 7 days. The problem is the individual facilities are sharing physicians within the network and by law, physicians are not allowed to work more than 6 consecutive days in a row and for any individual physician, there must be 480 minutes or 8-hours between shifts.

It just so happens this is a very well defined and explored problem domain. [Google-Or Tools](https://developers.google.com/optimization/scheduling/employee_scheduling) | [Emergency Scheduling](https://pdfs.semanticscholar.org/6472/5010acca9c438ea9d205cca30484ab6bf86c.pdf)

### Consulting Project

I worked with the University of California, San Francisco (UCSF) to automate their emergency resident scheduling process given a set of defined constraints.

### Modeling the Problem before consulting with the team
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-09-13%20at%205.53.07%20PM.png)

### The first whiteboard session
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/IMG_3687%20(1).JPG)

I tried to think about all the different ways I could solve this problem given there shifts and residents and using the entity relational diagram above.

### The initial data set
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-09-17%20at%203.19.31%20PM.png)

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

### The dataframe
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-09-27%20at%205.14.03%20PM.png)

### Deliverable | [Link](https://ucsf-er-resident-scheduler.firebaseapp.com/)
![alt text](https://github.com/amblount/CP-for-ED-scheduling/blob/master/public/Screen%20Shot%202018-10-01%20at%203.14.25%20PM.png)
