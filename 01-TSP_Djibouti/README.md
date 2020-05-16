# Discrete Optimization: Travelling Salesman Problem (Djibouti - 38 cities)


![djibouti_web](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/Screenshots/djibouti_web.png)

**Code in Python available** [here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/TSP_Djibouti.py)

**Results**

I used the pre-implemented TSP functions and genetic algorithm from the mlrose package to solve the TSP problem. Unfortunately, after several iterations it doesn't seem to behave properly regarding problems with a large number of cities (<20). The next steps would be to try a simulated annealing algorithm from the pygmo package. Computational time remains high and should drastically decrease with a more appropriate algorithm.

![djibouti38_res](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/Screenshots/djibouti38_res.png)

![TSP_convergence_djibouti38](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/Screenshots/TSP_convergence_djibouti38.png)

![TSP_route_djibouti38](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/Screenshots/TSP_route_djibouti38.png)

**Computed solutions available** [here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/Djibouti38_sol.csv)
