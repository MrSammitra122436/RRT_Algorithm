# RRT_Algorithm
This is the git repository where I implement RRT algorithm with python 
In robotic path planning problem is a classic. A robot, with certain dimensions, is attempting to navigate between point A and point B while avoiding the set of all obstacles,
## RRT
The premise of RRT is actually quite straight forward. Points are randomly generated and connected to the closest available node. Each time a vertex is created, a check must be made that the vertex lies outside of an obstacle. Furthermore, chaining the vertex to its closest neighbor must also avoid obstacles. The algorithm ends when a node is generated within the goal region, or a limit is hit.

RequiredRRT.py contains the all the required methods and class to implement the RRT algorithum while RRT.py show the window where RRT is implemented.
