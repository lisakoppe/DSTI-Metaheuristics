# Discrete Optimization: Travelling Salesman Problem (Qatar - 194 cities)


![qatar_web](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/Screenshots/qatar_web.png)

**Code in Python available** [here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/TSP_Qatar.py)

**Results**

I used the pre-implemented TSP functions and genetic algorithm from the mlrose package to solve the TSP problem. Unfortunately, after several iterations it doesn't seem to behave properly regarding problems with a large number of cities (<20). The next steps would be to try a simulated annealing algorithm from the pygmo package. Computational time remains high and should drastically decrease with a more appropriate algorithm.

![qatar194_res](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/Screenshots/qatar194_res.png)

![TSP_convergence_qatar194](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/Screenshots/TSP_convergence_qatar194.png)

![TSP_route_qatar194](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/Screenshots/TSP_route_qatar194.png)

**Computed solutions available** [here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/Qatar194_sol.csv)
