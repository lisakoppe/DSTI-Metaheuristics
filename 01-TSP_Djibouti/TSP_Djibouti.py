# Discrete Optimization: Travelling Salesman Problem
# Djibouti - 38 cities

# Import all the necessary packages
import mlrose
import pandas as pd
import matplotlib.pyplot as plt
import time

# Read data from csv
cities_raw = pd.read_csv("Data/dj38.csv")
print(cities_raw)
print(type(cities_raw))

# Create a matrix of city coordinates from the DataFrame
cities_list = cities_raw[['x','y']].values.tolist()
print(cities_list)
print(type(cities_list))

# Initialize function parameters
nb_cities = int(len(cities_list))
print(nb_cities)
population = 5000

# Initialize fitness function object
fitness_coords = mlrose.TravellingSales(coords=cities_list)

# Define an Optimization Problem Object with TSPOpt()
problem_fit = mlrose.TSPOpt(length=nb_cities,
                            fitness_fn=fitness_coords,
                            maximize=False)

# Start timer to get computational time
t1 = time.time()

# Solve the problem using the genetic algorithm
best_state, best_fitness, fitness_curve = mlrose.genetic_alg(problem=problem_fit,
                                                             pop_size=population,
                                                             mutation_prob=0.1,
                                                             max_attempts=1000,
                                                             max_iters=10000,
                                                             curve=True)

# Stop timer and compute computational time
t2 = time.time()
comp_time = t2 - t1

# Print parameters and solutions
print("==========================================================================\n")
print("Travelling Salesman Problem: Djibouti - 38 cities\n")
print("01. Chosen algorithm to solve the problem: Genetic Algorithm from mlrose\n")
print("02. Parameters:")
print("\nNumber of cities:", nb_cities)
print("\nPopulation:", population)
print("\nMutation prob: 0.1")
print("\nMax attempts: 1000")
print("\nMax iterations: 10000")
print("\nNumber of cities:", nb_cities)
print("\n03. Final results:")
sol_df = pd.DataFrame(best_state, columns=[''])
sol_df.to_csv("Djibouti38_sol.csv", sep=",")
print("\n    - Solutions:", sol_df)
print("\n    - Fitness:", round(best_fitness, 2))
print("\nStopping criterion: 3000 iterations")
print("\nComputational time:", round(comp_time, 2), "seconds\n")
print("==========================================================================")

# Plot the convergence curve
fig = plt.figure(figsize=(16, 13))
plt.plot(-(fitness_curve))
plt.title("Convergence curve: Travelling Salesman Problem: Djibouti - 38 cities", fontsize=16)
plt.xlabel("Time (iterations)", fontsize=12)
plt.ylabel("Fitness", fontsize=12)
plt.savefig("Screenshots/TSP_convergence_djibouti38.png")
plt.show()

# Plot route
fig = plt.figure(figsize=(16, 16))
plt.plot([cities_list[best_state[i % nb_cities]][0] for i in range(nb_cities+1)], [cities_list[best_state[i % nb_cities]][1] for i in range(nb_cities+1)], 'ro-', linewidth=1)
plt.title("Best route: Travelling Salesman Problem: Djibouti - 38 cities", fontsize=16)
plt.xlabel("x coord", fontsize=12)
plt.ylabel("y coord", fontsize=12)
plt.savefig("Screenshots/TSP_route_djibouti38.png")
plt.show()