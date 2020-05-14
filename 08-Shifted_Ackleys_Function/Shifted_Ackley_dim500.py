# Continuous Optimization: Shifted Ackley's Function (F6) with D=500

# Import all the necessary packages
import math
import numpy as np
import pandas as pd
import pygmo as pg
import matplotlib.pyplot as plt
import time

# Read data from csv
raw_data = pd.read_csv("Data/Ackley_data.csv")
ackley = raw_data["val"].tolist()
print(ackley)
print(type(ackley))


# Initialize function parameters
D = 500
bias = -140
lower_bound = -32
upper_bound = 32
popsize = 100


# Define the Shifted Ackley's function with the previous parameters
def function(x, data, dim, f_bias):
    Sum1 = 0
    Sum2 = 0
    for i in range(dim - 1):
        z = x[i] - data[i]
        Sum1 += z ** 2
        Sum2 += math.cos(2 * math.pi * z)
    Sum = -20 * math.exp(-0.2 * math.sqrt(Sum1 / dim)) - math.exp(Sum2 / dim) + 20 + math.e
    res = Sum + f_bias
    return res


# Create User Defined Problem (UDP) class
class ackley_prob:
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
    prob = pg.problem(ackley_prob(dimension, lower_bound, upper_bound, optim, bias))
    algo = pg.algorithm(pg.pso(gen=8000, omega=0.6, eta1=1.5, eta2=2.5, max_vel=0.5, variant=1))
    algo.set_verbosity(1)
    pop = pg.population(prob, popsize)
    pop = algo.evolve(pop)
    log = algo.extract(pg.pso).get_log()
    curve = [x[2] for x in log]
    niter = log[-1][0]
    return prob, algo, pop, log, niter, curve


# Create a function to plot the convergence curve
def plot_fitness(solution):
    fig = plt.figure(figsize=(16, 13))
    plt.plot(solution)
    plt.title("Continuous Optimization: Shifted Ackley's Function (F6) with D=500", fontsize=16)
    plt.xlabel("Time (iterations)", fontsize=12)
    plt.ylabel("Fitness", fontsize=12)
    plt.savefig("Screenshots/Ackley_convergence_curve500.png")
    plt.show()


# Start timer to get computational time
t1 = time.time()

# Solve the problem
solver(D, lower_bound, upper_bound, ackley, bias, popsize)

# Stop timer and compute computational time
t2 = time.time()
comp_time = t2 - t1


# Print parameters and solutions
print("==========================================================================\n")
print("Function: Shifted Ackley's Function (F6)\n")
print("01. Chosen algorithm to solve the problem: PSO from Pygmo\n")
print("02. Parameters:")
print("\nDimension:", D)
print("\nSearch space: [", lower_bound, ",", upper_bound, "]")
print("\nBias:", bias)
print("\nPopulation size:", popsize)
param = algo.get_extra_info()
print("\n", param)
print("\n03. Final results:")
sol_df = pd.DataFrame(pop.champion_x, columns=[''])
sol_df.to_csv("Ackley_sol500.csv", sep=",")
print("\n    - Solutions:", sol_df)
print("\n    - Fitness:", pop.champion_f[0])
print("\nNumber of function evaluations:", pop.problem.get_fevals())
print("\nStopping criterion:", niter, "iterations")
print("\nComputational time:", round(comp_time, 2), "seconds\n")
print("==========================================================================")

# Plot and save convergence curve
plot_fitness(curve)