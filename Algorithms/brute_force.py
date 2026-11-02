from itertools import permutations

def brute_force(cities, cost, start, route_cost):
  """
    Find the optimal tour by evaluating all possible city permutations.

    Parameters:
        cities (list): List of city indices.
        cost (dict): Cost matrix containing travel costs between cities.
        start (int): Fixed starting city.
        route_cost (function): Function used to calculate the total tour cost.

    Returns:
        tuple:
            min_cost (int): Minimum cost among all possible tours.
            min_route (tuple): Optimal tour starting from the specified city.
    """

  # Create a list of cities excluding the fixed starting city.
  other_cities = cities.copy()
  other_cities.remove(start)

  # Generate all possible permutations of the remaining cities.
  all_routes = list(permutations(other_cities))
  
  # Initialize a list to store the cost of each possible tour.
  all_routes_cost = []

  # Calculate the total cost of every possible tour.
  for i in range(len(all_routes)):
    
    # Add the starting city at the beginning of each route.
    complete_route = (start,) + all_routes[i]
    
    # Calculate and store the cost of the complete tour.
    all_routes_cost.append(route_cost(complete_route, cost))

  # Find the minimum tour cost.
  min_cost = min(all_routes_cost)
  
  # Identify the index of the minimum-cost tour.
  min_index = all_routes_cost.index(min_cost)
  
  # Retrieve the optimal route.
  min_route = (start,) + all_routes[min_index]

  return min_cost, min_route
