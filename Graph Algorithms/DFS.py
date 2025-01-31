# Depth-First Search (DFS) Implementation in Python

# DFS is a traversal algorithm that explores as deeply as possible before backtracking.
# Time Complexity: O(V + E) (Visiting all vertices and edges)
# Space Complexity: O(V) (Storing visited nodes)

def dfs_recursive(graph, node, visited, dfs_order):
    """
    Recursive function to perform DFS traversal.
    :param graph: Dictionary representing adjacency list of the graph
    :param node: Current node being visited
    :param visited: Set of visited nodes
    :param dfs_order: List to store DFS traversal order
    """
    if node not in visited:
        visited.add(node)  # Mark node as visited
        dfs_order.append(node)  # Store traversal order
        
        for neighbor in graph.get(node, []):  # Explore each neighbor
            dfs_recursive(graph, neighbor, visited, dfs_order)


def dfs(graph, start):
    """
    Function to perform DFS traversal using recursion.
    :param graph: Dictionary representing adjacency list of the graph
    :param start: Starting node for DFS
    :return: List of nodes in DFS order
    """
    visited = set()  # Track visited nodes
    dfs_order = []  # Store DFS traversal order
    dfs_recursive(graph, start, visited, dfs_order)
    return dfs_order


# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from node 'A'
dfs_result = dfs(graph, 'A')
print("DFS Traversal Order:", dfs_result)

# Edge Cases Considered:
# 1. Graph with isolated nodes
# 2. Graph with cycles
# 3. Graph with a single node
# 4. Graph with disconnected components
# 5. Empty graph
