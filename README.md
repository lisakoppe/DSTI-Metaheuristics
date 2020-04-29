# DSTI-Metaheuristics_Optimization

Objective: solve different problems using metaheuristics: 2 discrete optimization problems and 6 continuous problems.

For each function you are expected to report:
- The chosen algorithm and a justification of this choice
- The parameters of the algorithm
- The final results, both solution and fitness
- The number of function evaluations
- The stopping criterion
- The computational time
- The convergence curve (fitness as a function of time)

Codes should be provided in Python and published on a public Github repository with a folder for each function.
A readme.md should be also there describing the required criteria as well as a description on how to execute the code to reproduce the final results.

1. Discrete optimization

2 TSP problems:
- 38 cities (Djibouti)
- 194 cities (Qatar)

Data (in TSPLIB format) can be found on the following link:
http://www.math.uwaterloo.ca/tsp/world/countries.html
Aim is to find the shortest path, so you visit all cities without visiting the same twice.

2. Continuous optimization

Optimize the 6 first functions (F1-F6).
The description of the first 6 functions are available in the “CEC2008_TechnicalReport.pdf”.

You should provide results for both dimension D = 50 and D = 500.
F1: Shifted Sphere Function
F2 : Shifted Schwefel’s Problem 2.21
F3 : Shifted Rosenbrock’s Function
F4 : Shifted Rastrigin’s Function
F5 : Shifted Griewank’s Function
F6 : Shifted Ackley’s Function

The code of the functions as well as the shifts are available in cec08.rar (in C)
