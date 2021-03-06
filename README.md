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
- 38 cities (Djibouti): [code available here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/01-TSP_Djibouti/TSP_Djibouti.py)
- 194 cities (Qatar): [code available here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/02-TSP_Qatar/TSP_Qatar.py)

Data (in TSPLIB format) can be found on the following link:
http://www.math.uwaterloo.ca/tsp/world/countries.html
The aim is to find the shortest path, so you visit all cities without visiting the same twice.

## 02. Continuous Optimization

Optimize the 6 first functions (F1-F6).
The description of the first 6 functions are available in the [“CEC2008_TechnicalReport.pdf”](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/Resources/CEC2008_TechnicalReport.pdf).

Results are provided for both dimension D=50 and D=500:
- F1: Shifted Sphere Function: [D=50](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/03-Shifted_Sphere_Function/Shifted_Sphere_dim50.py), [D=500](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/03-Shifted_Sphere_Function/Shifted_Sphere_dim500.py)
- F2: Shifted Schwefel’s Problem: [D=50](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/04-Shifted_Schwefels_Problem/Shifted_Schwefel_dim50.py), [D=500](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/04-Shifted_Schwefels_Problem/Shifted_Schwefel_dim500.py)
- F3: Shifted Rosenbrock’s Function: [D=50](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/05-Shifted_Rosenbrocks_Function/Shifted_Rosenbrock_dim50.py), [D=500](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/05-Shifted_Rosenbrocks_Function/Shifted_Rosenbrock_dim500.py)
- F4: Shifted Rastrigin’s Function: [D=50](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/06-Shifted_Rastrigins_Function/Shifted_Rastrigin_dim50.py), [D=500](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/06-Shifted_Rastrigins_Function/Shifted_Rastrigin_dim500.py)
- F5: Shifted Griewank’s Function: [D=50](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/07-Shifted_Griewanks_Function/Shifted_Griewank_dim50.py), [D=500](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/07-Shifted_Griewanks_Function/Shifted_Griewank_dim500.py)
- F6: Shifted Ackley’s Function: [D=50](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/08-Shifted_Ackleys_Function/Shifted_Ackley_dim50.py), [D=500](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/08-Shifted_Ackleys_Function/Shifted_Ackley_dim500.py)

The code of the functions as well as the shifts are available in C in the [cec08](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/tree/master/Resources/cec08) folder.

## Environment setup

In order to run the code, first make sure to install Anaconda:
```
sudo apt-get update -y
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
sudo bash Anaconda3-2019.07-Linux-x86_64.sh
source ~/.bashrc
conda update --all --yes
```

Clone the whole metaheuristics repository to your machine:
```
sudo apt-get install git
git clone https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization.git
```

Create a virtual environment with the required packages available [here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/Resources/requirements.txt):
```
conda create -n nameofyourenv python=3.7
conda install nb_conda
pip install -r requirements.txt
```

Activate the created environment and run .py files:
```
conda activate nameofyourenv
# then run any Python file from repository
```

For more environment creation commands, go to [this repository](https://github.com/lisakoppe/Toolbox/blob/master/Virtual%20environments/Environment_creation_conda.md).

## Initial machine used to run the scripts

Processor: Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz

RAM: 32.0 GB

System type: 64-bit OS, x64-based processor

## Resources used

Resources used are listed [here](https://github.com/lisakoppe/DSTI-Metaheuristics_Optimization/blob/master/Resources/resources.txt).
