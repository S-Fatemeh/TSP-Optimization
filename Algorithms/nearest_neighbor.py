def nearest_neighbor(cities, cost, start, route_cost):
  """
    Construct a tour using the Nearest Neighbor heuristic.

    Starting from a specified city, repeatedly visit the nearest
    unvisited city until all cities have been visited.

    Parameters:
        cities (list): List of city indices.
        cost (dict): Cost matrix containing travel costs between cities.
        start (int): Starting city.
        route_cost (function): Function used to calculate the total tour cost.

    Returns:
        tuple:
            min_cost (int): Total cost of the constructed tour.
            route (list): Sequence of visited cities.
    """

  # Create a copy of the cities list to track unvisited cities.
  unvisited = cities.copy()
  
  # Initialize an empty list to store the tour.
  route = []

  # Add the starting city to the tour and remove it from unvisited cities.
  route.append(start)
  unvisited.remove(start)

  # Set the current city to the starting city.
  current_city = start

  # Continue until all cities have been visited.
  while unvisited:
    
    # Assume the first unvisited city is the nearest candidate.
    min_cost = cost[current_city][unvisited[0]]
    next_city = unvisited[0]
    
    # Search for the nearest unvisited city.
    for j in range(1, len(unvisited)):
      candidate = unvisited[j]
      candidate_cost = cost[current_city][candidate]
      
      # Update the nearest city if a lower travel cost is found.
      if candidate_cost < min_cost:
        next_city = candidate
        min_cost = candidate_cost

    # Visit the selected city and update the current city.
    unvisited.remove(next_city)
    route.append(next_city)
    current_city = next_city
    
  # Calculate the total tour cost, including the return to the starting city.
  min_cost = route_cost(route, cost)

  return min_cost, route
