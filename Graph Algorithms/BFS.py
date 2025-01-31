# Breadth-First Search (BFS) Implementation in Python

# BFS is a level-wise traversal algorithm that ensures the shortest path in an unweighted graph.
# Time Complexity: O(V + E) (Visiting all vertices and edges)
# Space Complexity: O(V) (Storing visited nodes)

from collections import deque  # Import deque for efficient queue operations

def bfs(graph, start):
    """
    Function to perform Breadth-First Search (BFS).
    :param graph: Dictionary representing adjacency list of the graph
    :param start: Starting node for BFS
    :return: List of nodes in BFS order
    """
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize queue with starting node
    bfs_order = []  # List to store BFS traversal order

    while queue:
        node = queue.popleft()  # Dequeue the front node
        if node not in visited:
            visited.add(node)  # Mark node as visited
            bfs_order.append(node)  # Store traversal order
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order  # Return BFS traversal order


# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from node 'A'
bfs_result = bfs(graph, 'A')
print("BFS Traversal Order:", bfs_result)

# Edge Cases Considered:
# 1. Graph with isolated nodes
# 2. Graph with cycles
# 3. Graph with a single node
# 4. Graph with disconnected components
# 5. Empty graph
