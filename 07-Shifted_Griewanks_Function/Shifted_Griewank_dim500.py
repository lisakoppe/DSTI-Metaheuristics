# Continuous Optimization: Shifted Griewank's Function (F5) with D=500

# Import all the necessary packages
import math
import numpy as np
import pandas as pd
import pygmo as pg
import matplotlib.pyplot as plt
import time


# Read data from csv
raw_data = pd.read_csv("Data/Griewank_data.csv")
griewank = raw_data["val"].tolist()
print(griewank)
print(type(griewank))


# Initialize function parameters
D = 500
bias = -180
lower_bound = -600
upper_bound = 600
popsize = 50


# Define the Shifted Griewank's function with the previous parameters
def function(x, data, dim, f_bias):
    F1 = 0
    F2 = 1
    for i in range(dim - 1):
        z = x[i] - data[i]
        F1 += z ** 2 /4000
        F2 += math.cos(z / math.sqrt(i + 1))
    F = F1 - F2 + 1
    res = F + f_bias
    return res


# Create User Defined Problem (UDP) class
class griewank_prob:
    def __init__(self, dim, lower_bound, upper_bound, optim, bias):
        self.dim = dim
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.optim = optim
        self.bias = bias

    def fitness(self, x):
        res = [function(x, self.optim, self.dim, self.bias)]
        return res

    def get_bounds(self):
        xmin = self.lower_bound * np.ones(self.dim)
        xmax = self.upper_bound * np.ones(self.dim)
        return xmin, xmax


# Create a function to solve this problem
def solver(dimension, lower_bound, upper_bound, optim, bias, popsize):
    global algo
    global pop
    global niter
    global log
    global curve
    prob = pg.problem(griewank_prob(dimension, lower_bound, upper_bound, optim, bias))
    algo = pg.algorithm(pg.sade(gen=2600, variant=1, variant_adptv=1, ftol=1e-06, xtol=1e-06))
    algo.set_verbosity(1)
    pop = pg.population(prob, popsize)
    pop = algo.evolve(pop)
    log = algo.extract(pg.sade).get_log()
    curve = [x[2] for x in log]
    niter = log[-1][0]
    return prob, algo, pop, log, niter, curve


# Create a function to plot the convergence curve
def plot_fitness(solution):
    fig = plt.figure(figsize=(16, 13))
    plt.plot(solution)
    plt.title("Continuous Optimization: Shifted Griewank's Function (F5) with D=500", fontsize=16)
    plt.xlabel("Time (iterations)", fontsize=12)
    plt.ylabel("Fitness", fontsize=12)
    plt.savefig("Screenshots/Griewank_convergence_curve500.png")
    plt.show()


# Start timer to get computational time
t1 = time.time()

# Solve the problem
solver(D, lower_bound, upper_bound, griewank, bias, popsize)

# Stop timer and compute computational time
t2 = time.time()
comp_time = t2 - t1


# Print parameters and solutions
print("==========================================================================\n")
print("Function: Shifted Griewank's Function (F5)\n")
print("01. Chosen algorithm to solve the problem: SADE from Pygmo\n")
print("02. Parameters:")
print("\nDimension:", D)
print("\nSearch space: [", lower_bound, ",", upper_bound, "]")
print("\nBias:", bias)
print("\nPopulation size:", popsize)
param = algo.get_extra_info()
print("\n", param)
print("\n03. Final results:")
sol_df = pd.DataFrame(pop.champion_x, columns=[''])
sol_df.to_csv("Griewank_sol500.csv", sep=",")
print("\n    - Solutions:", sol_df)
print("\n    - Fitness:", pop.champion_f[0])
print("\nNumber of function evaluations:", pop.problem.get_fevals())
print("\nStopping criterion:", niter, "iterations")
print("\nComputational time:", round(comp_time, 2), "seconds\n")
print("==========================================================================")

# Plot and save convergence curve
plot_fitness(curve)