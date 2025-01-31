# Floyd-Warshall Algorithm Implementation in Python

# Floyd-Warshall finds the shortest paths between all pairs of nodes in a weighted graph.
# Time Complexity: O(V³) (Iterating over all pairs of vertices)
# Space Complexity: O(V²) (For storing shortest distances)

INF = float('inf')  # Representation of infinity

def floyd_warshall(graph):
    """
    Function to perform Floyd-Warshall Algorithm.
    :param graph: 2D matrix representing edge weights (graph[i][j] = weight from i to j)
    :return: Matrix with shortest distances between all pairs of vertices
    """
    num_vertices = len(graph)
    
    # Step 1: Initialize distance matrix
    dist = [row[:] for row in graph]  # Copy the original graph

    # Step 2: Compute shortest paths using dynamic programming
    for k in range(num_vertices):  # Intermediate node
        for i in range(num_vertices):  # Start node
            for j in range(num_vertices):  # End node
                # Update shortest distance if a better path exists
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist  # Return the shortest path matrix


# Example Graph (Adjacency Matrix with Weights)
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

# Perform Floyd-Warshall Algorithm
shortest_paths = floyd_warshall(graph)

# Print Shortest Path Matrix
print("Shortest distances between every pair of vertices:")
for row in shortest_paths:
    print(row)

# Edge Cases Considered:
# 1. Graph with negative weight edges (but no negative cycles)
# 2. Graph with isolated nodes
# 3. Graph with a single node
# 4. Graph with disconnected components
# 5. Empty graph
