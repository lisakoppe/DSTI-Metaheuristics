# DSTI - Solving Optimization Problems with Metaheuristics

**Objective:** solve different problems using metaheuristics:
- 2 discrete optimization problems
- 6 continuous problems

For each function you are expected to report:
- The chosen algorithm and a justification of this choice
- The parameters of the algorithm
- The final results, both solution and fitness
- The number of function evaluations
- The stopping criterion
- The computational time
- The convergence curve (fitness as a function of time)

## 01. Discrete Optimization

2 TSP problems:
- 38 cities (Djibouti): [notebook available here]()
- 194 cities (Qatar): [notebook available here]()

Data (in TSPLIB format) can be found on the following link:
http://www.math.uwaterloo.ca/tsp/world/countries.html
The aim is to find the shortest path, so you visit all cities without visiting the same twice.

## 02. Continuous Optimization

Optimize the 6 first functions (F1-F6).
The description of the first 6 functions are available in the [“CEC2008_TechnicalReport.pdf”](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/Resources/CEC2008_TechnicalReport.pdf).

You should provide results for both dimension D=50 and D=500.
- F1: Shifted Sphere Function: [D=50](), [D=500]()
- F2: Shifted Schwefel’s Problem: [D=50](), [D=500]()
- F3: Shifted Rosenbrock’s Function: [D=50](), [D=500]()
- F4: Shifted Rastrigin’s Function: [D=50](), [D=500]()
- F5: Shifted Griewank’s Function: [D=50](), [D=500]()
- F6: Shifted Ackley’s Function: [D=50](), [D=500]()

The code of the functions as well as the shifts are available in C in the (cec08)[https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/tree/master/Resources/cec08] folder.
