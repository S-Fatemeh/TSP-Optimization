# Computational Comparison of Brute Force and Nearest Neighbor Algorithms for the Asymmetric Traveling Salesperson Problem

A Python-based computational research project comparing an exact algorithm and a heuristic algorithm for the **Asymmetric Traveling Salesperson Problem (ATSP)**.

## Overview

The Traveling Salesperson Problem (TSP) is a combinatorial optimization problem in which the objective is to find the minimum-cost tour that visits every city exactly once and returns to the starting city.

This project investigates the trade-off between solution quality and computational efficiency by comparing two algorithms:

- **Brute Force:** An exact algorithm that evaluates all possible tours and guarantees an optimal solution.
- **Nearest Neighbor:** A greedy heuristic that constructs a tour by repeatedly selecting the nearest unvisited city.

The experiments use randomly generated asymmetric cost matrices, where travel costs from city *i* to city *j* may differ from the costs in the opposite direction.

## Project Objectives

- Implement exact and heuristic algorithms for ATSP.
- Compare solution quality and computational runtime.
- Investigate the effect of the starting city on solution quality.
- Evaluate the optimality gap of the Nearest Neighbor algorithm.
- Conduct reproducible computational experiments using Python.

## Algorithms

### 1. Brute Force

Brute Force enumerates all possible tours and selects the one with the minimum total cost.

- Guarantees an optimal solution.
- Has factorial time complexity.
- Is suitable mainly for small problem instances.

### 2. Nearest Neighbor

Nearest Neighbor constructs a tour by repeatedly visiting the nearest unvisited city.

- Produces a feasible solution efficiently.
- Has much lower computational cost than Brute Force.
- Does not guarantee an optimal solution.
- Its solution quality depends on the starting city.

## Experimental Setup

The experiments are conducted using Python with randomly generated cost matrices.

| Parameter | Configuration |
|---|---|
| Problem sizes | 2–10 cities |
| Random instances | 50 per problem size |
| Starting cities | Every city |
| Total instances | 450 |
| Total starting-city experiments | 2,700 |
| Algorithms compared | Brute Force and Nearest Neighbor |

The off-diagonal matrix entries are independently generated random integers between 10 and 40. Diagonal entries are set to zero.

Each algorithm is evaluated on the same cost matrix and starting city.

## Evaluation Metrics

The algorithms are compared using three main metrics:

- **Tour Cost:** Total cost of the resulting tour.
- **Runtime:** Execution time measured using Python's `time.perf_counter()`.
- **Optimality Gap:** Percentage difference between the Nearest Neighbor solution and the optimal Brute Force solution.

The optimality gap is calculated as:

\[
\text{Gap}(\%) =
\frac{C_{NN}-C_{BF}}{C_{BF}}\times 100
\]

where \(C_{NN}\) is the Nearest Neighbor tour cost and \(C_{BF}\) is the optimal Brute Force tour cost.

## Preliminary Results

The experiments demonstrate a substantial difference in computational runtime.

For instances with 10 cities:

| Metric | Brute Force | Nearest Neighbor |
|---|---:|---:|
| Median runtime | 1,250.8555 ms | 0.0370 ms |

Based on median runtime, Brute Force was approximately **33,807 times slower** than Nearest Neighbor for 10-city instances.

The results also show that Nearest Neighbor does not always produce an optimal solution. Its solution quality varies depending on the cost matrix and the selected starting city.

These findings illustrate the trade-off between computational efficiency and solution optimality.

## Project Structure

```text
TSP-Optimization/
│
├── Algorithms/
│   ├── brute_force.py
│   └── nearest_neighbor.py
│
├── Experiments/
│   └── compare_algorithms.ipynb
│
├── Results/
│   └── tsp_results.csv
│
├── data/
│   ├── cost_matrix.csv
│   ├── starting_city_gap_table.csv
│   └── starting_city_summary.csv
│
├── functions/
│   ├── route_cost.py
│   └── generate_cost_matrix.py
│
├── README.md
└── .gitignore
```

## Technologies

- Python 3.11
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/S-Fatemeh/TSP-Optimization.git
```

2. Navigate to the project directory:

```bash
cd TSP-Optimization
```

3. Install the required Python packages:

```bash
pip install numpy pandas matplotlib jupyter
```

4. Open the experiment notebook:

```bash
jupyter notebook
```

5. Run `Experiments/compare_algorithms.ipynb` to reproduce the computational experiments.

## Future Work

Potential extensions of this project include:

- Investigating larger problem instances.
- Implementing additional heuristic and metaheuristic algorithms.
- Exploring mathematical optimization formulations using tools such as OR-Tools or Pyomo.
- Conducting further statistical analysis.
- Comparing additional optimization methods in terms of runtime and solution quality.

## Project Status

**Implemented:** Brute Force, Nearest Neighbor, and computational experiments.

**Ongoing:** Further analysis, visualization, and exploration of additional optimization methods.