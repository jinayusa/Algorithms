# Bellman-Ford Algorithm Implementation in Python

# Bellman-Ford finds the shortest path in graphs with negative weights and detects negative cycles.
# Time Complexity: O(V * E) (V - 1 relaxations for E edges)
# Space Complexity: O(V) (For storing distances)

def bellman_ford(graph, vertices, start):
    """
    Function to perform Bellman-Ford Algorithm for shortest path.
    :param graph: List of tuples (source, destination, weight)
    :param vertices: Number of vertices in the graph
    :param start: Starting node for Bellman-Ford
    :return: Dictionary containing shortest distances from start node, or detect negative cycle
    """
    # Step 1: Initialize distances
    distances = {node: float('inf') for node in range(vertices)}
    distances[start] = 0  # Distance to the start node is 0

    # Step 2: Relax all edges V-1 times
    for _ in range(vertices - 1):  # Iterate V-1 times
        for src, dest, weight in graph:  # For each edge (u, v, w)
            if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
                distances[dest] = distances[src] + weight  # Update shortest distance

    # Step 3: Check for negative weight cycles
    for src, dest, weight in graph:
        if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
            return "Negative weight cycle detected!"  # Negative cycle exists

    return distances  # Return shortest distance to all nodes


# Example Graph (Edge List with Weights)
graph = [
    (0, 1, 4),  # Edge from 0 to 1 with weight 4
    (0, 2, 1),  # Edge from 0 to 2 with weight 1
    (1, 3, 2),
    (2, 1, 2),
    (2, 3, 5),
    (3, 4, 3),
    (4, 1, -7)  # Negative weight edge
]

vertices = 5  # Number of vertices in the graph

# Perform Bellman-Ford from node 0
shortest_paths = bellman_ford(graph, vertices, 0)
print("Shortest distances from node 0:", shortest_paths)

# Edge Cases Considered:
# 1. Graph with negative weight edges
# 2. Graph with a negative cycle
# 3. Graph with disconnected components
# 4. Single-node graph
# 5. Empty graph
