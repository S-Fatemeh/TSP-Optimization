import random


def generate_cost_matrix(N, seed=None):
    """
    Generate a random cost matrix for the Asymmetric Traveling Salesperson Problem (ATSP).

    Parameters:
        N (int): Number of cities.
        seed (int, optional): Random seed for reproducibility.

    Returns:
        tuple:
            cities (list): List of city indices.
            cost (dict): Nested dictionary representing the cost matrix.
    """

    # Create city indices from 0 to N-1.
    cities = list(range(N))
    
    # Initialize an empty dictionary to store travel costs.
    cost = {}
    
    # Create a local random number generator for reproducible results.
    rng = random.Random(seed)
    
    # Generate the travel cost between every pair of cities.
    for i in cities:
        cost[i] = {}
        for j in cities:
            
            # Set the cost of traveling from a city to itself to zero.
            if i == j:
                cost[i][j] = 0
                
            # Assign a random cost between 10 and 40 for different cities.
            else:
                cost[i][j] = rng.randint(10, 40)
    
    return cities, cost