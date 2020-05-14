# Discrete Optimization: Travelling Salesman Problem
# Djibouti - 38 cities

# Import all the necessary packages
import mlrose
import pandas as pd
import time










start_time = time.time() # To evaluate computational time

# Download data
cities = pd.read_csv("E:\DataScience\DSTI\Metaheuristic\Exam\TSP\Djibouti_38.csv")


# Create 2D matrix containing x,y coordinate of all the cities
cities_list = cities[['X','Y']].values.tolist()

# Initialize fitness function object
fitness_coords = mlrose.TravellingSales(coords=cities_list)
problem_fit = mlrose.TSPOpt(length = 38, fitness_fn = fitness_coords,
                            maximize=False)

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)

print()
print('The best state found is: ', best_state)
print()
print('The fitness at the best state is: ', best_fitness)
print()
print("Computational time: {:.3f} seconds".format(time.time()-start_time))




















# # Import necessary packages
# import pandas as pd
# import numpy as np
# import tsplib95 as tsplib
# import matplotlib.pyplot as plt
# import time
# import mlrose
# import re
# import random
#
# import math
# import random
# import copy
# import random
# import matplotlib.pyplot as plt
# from celluloid import Camera
#
#
# def dist(city1, city2):
#     return abs(math.sqrt((city1.x-city2.x)**2+(city1.y-city2.y)**2))
#
#
# def eval_all_edges_length(data):
#     all_edges = []
#     for i, first in enumerate(data):
#         all_edges.append([])
#         for j, second in enumerate(data):
#             all_edges[i].append(dist(first, second))
#     return all_edges
#
#
# def total_length(sequence, all_edges):
#     total = 0
#     for i, num in enumerate(sequence):
#         total += all_edges[num][sequence[i - 1]]
#     return total
#
#
# def find_neighbour(sequence, all_edges):
#     [item1, item2] = random.sample(sequence, k=2)
#     index1 = sequence.index(item1)
#     index2 = sequence.index(item2)
#     new_sequence = copy.deepcopy(sequence)
#     new_sequence[index1], new_sequence[index2] = new_sequence[index2], new_sequence[index1]
#     new_total_distance = total_length(new_sequence, all_edges)
#     return new_sequence, new_total_distance
#
#
# def plot_graph(data, sequence, plt, camera):
#     data_x = [_.x for _ in data]
#     data_y = [_.y for _ in data]
#     plt.scatter(data_x, data_y, c='#ff0000')
#     for i, num in enumerate(sequence):
#         if i is 0:
#             plt.plot([data[sequence[0]].x, data[sequence[-1]].x], [data[sequence[0]].y, data[sequence[-1]].y])
#         else:
#             plt.plot([data[num].x, data[sequence[i - 1]].x], [data[num].y, data[sequence[i - 1]].y])
#     camera.snap()
#
#
# def acceptance(new, curr, t):
#     if t is 0:
#         return 0
#     else:
#         return math.exp((curr - new) / t)
#
#
# class Coor:
#     def __init__(self, index, x, y):
#         self.index = index
#         self.x = x
#         self.y = y
#
#
# def from_file(file_path):
#     with open(file_path, 'r') as f:
#         line = f.readline()
#         output = []
#         while line:
#             line = line.replace('\n', '').split(' ')
#             #line = [float(x) if '.' in x else x for x in line]  # convert decimals
#             #line = [int(x) if type(x) is str and x.isdigit() else x for x in line]  # convert integers
#             #if type(line[0]) is int:
#                 #output.append(Coor(line[0] - 1, line[2], line[1]))
#             line = f.readline()
#     return output
#
#
#
# fig = plt.figure()
# camera = Camera(fig)
# data = from_file('../Resources/dj38.tsp')
# all_edges = eval_all_edges_length(data)
# sequence = random.sample(range(0, len(data)), len(data))
# current_total_distance = total_length(sequence, all_edges)
# list_length = len(sequence)
#
# for t in range(500, -1, -1):
#     for i in range(10000):
#         new_sequence, new_total_distance = find_neighbour(sequence, all_edges)
#         if new_total_distance < current_total_distance:
#             # always accept move when new distance is shorter
#             sequence = new_sequence
#             current_total_distance = new_total_distance
#         elif acceptance(new_total_distance, current_total_distance, t) > random.uniform(0, 1):
#             # accept move by chance based on acceptance probability e^(delta E / T) where delta E is non-positive
#             sequence = new_sequence
#             current_total_distance = new_total_distance
#     # print data to console and plot graph by step of 100
#     if t % 10 is 0:
#         print(f"T: {t}")
#         print(f'Best Sequence So Far: {sequence}')
#         print(f'Shortest Distance So Far: {current_total_distance}')
#         plot_graph(data, sequence, plt, camera)
#
# animation = camera.animate()
# animation.save('wi29.mp4')  # change output video name here



















# # Set timer
# start = time.time()
#
# # Import TSP data and explore file structure
# filepath = '../Resources/dj38.tsp'
# with open(filepath, 'r') as f:
#     dataset = tsplib.read(f)
#
# print(type(dataset))
# print(dataset.render())
#
# # Convert the problem to a networkx graph
# graph_data = dataset.get_graph()
# # print(graph_data.nodes)
# # print(graph_data.graph)
#
# print(list(dataset.get_nodes()))
# print(dataset.node_coords[1])
#
#
# # creating an instance of a TSP problem
# tsp_instance = tsp(dataset)


# if __name__ == "__main__":
#     main()

# # Create list of city coordinates
# dict = tsp.models.Problem.as_dict(dataset)
# print(dict)
#
# # Initialize fitness function object using coords_list
# fitness_coords = mlrose.TravellingSales(coords = dict)
#
# problem_fit = mlrose.TSPOpt(length = 38, fitness_fn = fitness_coords, maximize=False)


#__________________________________________________________________________________

