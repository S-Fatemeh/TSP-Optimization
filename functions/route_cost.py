def route_cost(route, cost):
  """
    Calculate the total cost of a tour, including the return to the starting city.

    Parameters:
        route (list): The sequence of cities in the tour.
        cost (dict): The cost matrix containing travel costs between cities.

    Returns:
        int: The total cost of the complete tour.
    """
  total = 0
  
  # Calculate the cost of traveling between consecutive cities.
  for i in range(len(route) - 1):
    total = total + cost[route[i]][route[i+1]]
    
  # Add the cost of returning from the last city to the starting city.
  total = total + cost[route[-1]][route[0]]
  return total
