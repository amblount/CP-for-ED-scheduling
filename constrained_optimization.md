# Why optimization?

[About Combinatorial Optimization](https://developers.google.com/optimization/introduction/overview)
Combinatorial optimization seeks to find the best solution to a problem out of a very large set of possible solutions. Here are some examples:

- Vehicle routing: Find optimal routes for vehicle fleets that pick up and deliver packages given constraints (e.g., "this truck can't hold more than 20,000 pounds" or "all deliveries must be made within a two-hour window").

- Scheduling: find the optimal schedule for complex set of tasks, some of which need to be performed before others, on a fixed set of machines, or other resources.

- Bin packing: pack as many objects of various sizes as possible into a fixed number of bins with maximum capacitites.

In most cases, problems like these have a vast number of possible solutions—too many for a computer to search them all. To overcome this, OR-Tools uses state-of-the-art algorithms to narrow down the search set, in order to find an optimal (or close to optimal) solution.
