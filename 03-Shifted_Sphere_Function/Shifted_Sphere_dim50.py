# Continuous Optimization: Shifted Sphere Function (F1) with D=50

# Import all the necessary packages
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import time


# Read data from csv
raw_data = pd.read_csv("Data/Sphere_data.csv")
sphere = raw_data["val"].tolist()
print(sphere)
print(type(sphere))


# Initialize function parameters
D = 50
bias = -450
lower_bound = -100
upper_bound = 100
sol_list = []


# Define the Shifted Sphere function with the previous parameters
def function(x, data=sphere, dim=D, f_bias=bias):
    F = 0
    for i in range(dim - 1):
        z = x[i] - data[i]
        F += z**2
    res = F + f_bias
    return res


# Create a function to gather all the solutions computed. To be used in callback
def sol_set(xk):
    sol_res = function(xk)
    sol_list.append(sol_res)
    return sol_res


# Create a function to compute the initial guess with random uniform distribution
def sol_init(dim, lower_bound, upper_bound):
    xmin = lower_bound * np.ones(dim)
    xmax = upper_bound * np.ones(dim)
    x0 = np.random.uniform(min(xmin), max(xmax), dim)
    return x0


# Create a function to solve this problem
def solver(dimension, lower_bound, upper_bound):
    global sol
    # Compute the initial guess
    x0 = sol_init(dimension, lower_bound, upper_bound)
    # Minimize the function thanks to the BFGS algorithm
    sol = minimize(sol_set, x0, bounds=(lower_bound, upper_bound), method='BFGS', callback=sol_set)
    return sol, sol_list


# Create a function to plot the convergence curve
def plot_fitness(solution):
    fig = plt.figure(figsize=(16, 13))
    plt.plot(solution)
    plt.title("Continuous Optimization: Shifted Sphere Function (F1) with D=50", fontsize=16)
    plt.xlabel("Time (iterations)", fontsize=12)
    plt.ylabel("Fitness", fontsize=12)
    plt.savefig("Screenshots/Sphere_convergence_curve50.png")
    plt.show()


# Start timer to get computational time
t1 = time.time()

# Solve the problem
solver(D, lower_bound, upper_bound)

# Stop timer and compute computational time
t2 = time.time()
comp_time = t2 - t1


# Print parameters and solutions
print("==========================================================================\n")
print("Function: Shifted Sphere Function (F1)\n")
print("01. Chosen algorithm to solve the problem: BFGS from SciPy\n")
print("02. Parameters:")
print("\nDimension:", D)
print("\nSearch space: [", lower_bound, ",", upper_bound, "]")
print("\nBias:", bias)
print("\n03. Final results:")
sol_df = pd.DataFrame(sol.x, columns=[''])
sol_df.to_csv("Sphere_sol50.csv", sep=",")
print("\n    - Solutions:", sol_df)
print("\n    - Fitness:", round(sol.fun, 2))
print("\nNumber of function evaluations:", sol.nfev)
print("\nStopping criterion:", sol.nit, "iterations")
print("\nComputational time:", round(comp_time, 2), "seconds\n")
print("==========================================================================")

# Plot and save convergence curve
plot_fitness(sol_list)
