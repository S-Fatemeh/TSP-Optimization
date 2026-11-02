# TSP-Optimization
A Python-based research project exploring algorithms for the **Traveling Salesman Problem (TSP)**.

## Objectives

- Implement exact and heuristic algorithms for TSP.
- Compare solution quality and computational runtime.
- Explore mathematical optimization formulations.
- Develop reproducible computational experiments.

## Algorithms

- **Brute Force:** Enumerates all tours to find an optimal solution for small instances.
- **Nearest Neighbor:** Constructs a feasible tour using a greedy strategy.
- **Mathematical Optimization:** Planned exploration using optimization solvers.

## Experimental Setup

The project uses cost matrices to represent travel costs between cities. Experiments will evaluate:

- Total tour cost
- Runtime
- Solution quality
- Optimality gap, when a valid reference optimum is available

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- OR-Tools / Pyomo (planned)

## Project Status

Work in progress. Algorithms, experiments, and documentation will be added incrementally.

## Research Note

Brute Force is intended for small instances because its computational requirements grow factorially with the number of cities. Nearest Neighbor provides a faster heuristic solution but does not guarantee optimality.

## License

A license will be added when the project’s distribution terms are decided.
