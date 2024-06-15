from edgegraph import *

def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    # Check for None inputs
    if graph is None or start is None or end is None:
        return []

    # Initialize distances for all vertices
    distances = {v.name: float('inf') for v in graph.vertices()}
    distances[start.name] = 0

    # Iterate over all edges |V| - 1 times
    for _ in range(len(graph.vertices()) - 1):
        for edge in graph.edges():
            u, v, weight = edge._vertex1.name, edge._vertex2.name, edge.get_value()
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for edge in graph.edges():
        u, v, weight = edge._vertex1.name, edge._vertex2.name, edge.get_value()
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            # Negative-weight cycle detected, return an empty list
            return []

    # Construct shortest path
    path = [end]
    while path[-1] != start:
        current_vertex = path[-1]
        min_neighbor = min(graph.adjacent(current_vertex), key=lambda v: distances[v.name])
        path.append(min_neighbor)

    return list(reversed(path))
