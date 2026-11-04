import pulp


def mtz_model(cities, cost, start, route_cost):
    
    if start not in cities:
        raise ValueError("Invalid start city or number of cities.")

    model = pulp.LpProblem("ATSP_MTZ", pulp.LpMinimize)
    
    #Decision Variable
    x = pulp.LpVariable.dicts(
        "x",
        [(i,j) for i in cities for j in cities if i != j],
        cat=pulp.LpBinary
    )
    #auxiliary Variable
    u = pulp.LpVariable.dicts(
        "u",
        [i for i in cities if i != start],
        lowBound=1,
        upBound=len(cities) - 1,
        cat=pulp.LpInteger
    )
    
    #Objective Function
    model += pulp.lpSum(
        cost[i][j] * x[i,j]
        for i in cities
        for j in cities
        if i != j
    )
    
    # Each city must have exactly one outgoing edge (one departure)
    for i in cities:
        model += pulp.lpSum(
            x[i, j]
            for j in cities
            if i != j
        ) == 1
    
    # Each city must have exactly one incoming edge (one arrival)
    for j in cities:
        model += pulp.lpSum(
            x[i, j]
            for i in cities
            if i != j
        ) == 1
    
    # MTZ Subtour Elimination Constraints
    for i in cities:
        if i != start:
            for j in cities:
                if j != start and i != j:
                    model+=(
                        u[i] - u[j] + len(cities) * x[i, j]
                                            <= len(cities) - 1
                    )
    
    # Solve the optimization model using CBC
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    
    # Check the solver status
    status = pulp.LpStatus[model.status]
    
    if status != "Optimal":
        print(f"Optimization failed. Solver status:{status}")
        return None, None

    # Extract selected edges
    selected_edges = [
        (i, j)
        for i in cities
        for j in cities
        if i != j and pulp.value(x[i, j]) > 0.5
    ]
    
    # Build the optimal route
    route = [start]
    current_city = start
    
    while True:
        next_city = next(
            j for i , j in selected_edges
            if i == current_city
        )
        
        route.append(next_city)
        
        if next_city == start:
            break
        
        current_city = next_city
        
    total_cost = route_cost(route, cost)
    
    return total_cost, route
