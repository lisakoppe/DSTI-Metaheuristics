# Continuous Optimization: Shifted Ackley's Function (F6) with D=500

# Import all the necessary packages
import math
import numpy as np
import pandas as pd
from scipy.optimize import minimize
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


# Define the Shifted Ackley's function with the previous parameters
def function(x, data=ackley, dim=D, f_bias=bias):
    Sum1 = 0
    Sum2 = 0
    for i in range(0, dim):
        z = x[i] - data[i]
        Sum1 = z**2
        Sum2 = math.cos(2*math.pi*z)
        Sum1 += Sum1
        Sum2 += Sum2
    F = -20 * math.exp(-0.2*math.sqrt(Sum1/dim)) - math.exp(Sum2/dim) + 20 + math.e + f_bias
    return F


# Create a function to gather all the solutions computed. To be used in callback
def sol_set(xk):
    sol_list.append(function(xk))
    return sol_list


# Create a function to solve this problem
def solver(dimension, func):
    global sol
    global sol_list
    sol_list = []
    # Compute the initial guess
    x0 = np.random.uniform(lower_bound, upper_bound, dimension)
    # Minimize the function thanks to the Nelder-Mead algorithm
    sol = minimize(func, x0, bounds=(lower_bound, upper_bound), method='Powell', callback=sol_set)
    return sol


# Create a function to plot the convergence curve
def plot_fitness(solution):
    fig = plt.figure(figsize=(16, 13))
    plt.plot(solution)
    plt.title("Continuous Optimization: Shifted Ackley's Function (F6)")
    plt.xlabel("Time (iterations)")
    plt.ylabel("Fitness")
    plt.savefig("Screenshots/Ackley_convergence_curve500.png")
    plt.show()


# Start timer to get computational time
t1 = time.time()

# Solve the problem
solver(D, function)

# Stop timer and compute computational time
t2 = time.time()
comp_time = t2 - t1


# Print parameters and solutions
print("==========================================================================\n")
print("Function: Shifted Ackley's Function (F6)\n")
print("01. Chosen algorithm to solve the problem: Nelder-Mead Simplex from SciPy\n")
print("02. Parameters:")
print("\nDimension:", D)
print("\nSearch space: [", lower_bound, ",", upper_bound, "]")
print("\nBias:", bias)
print("\n03. Final results:")
sol_df = pd.DataFrame(sol.x, columns=[''])
sol_df.to_csv("Ackley_sol500.csv", sep=",")
print("\n    - Solutions:", sol_df)
print("\n    - Fitness:", round(sol.fun, 2))
print("\nNumber of function evaluations:", sol.nfev)
print("\nStopping criterion:", sol.nit, "iterations")
print("\nComputational time:", round(comp_time, 2), "seconds\n")
print("==========================================================================")

# Plot and save convergence curve
plot_fitness(sol_list)