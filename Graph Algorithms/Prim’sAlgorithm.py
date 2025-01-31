# Prim’s Algorithm Implementation in Python

# Prim's Algorithm finds the Minimum Spanning Tree using a priority queue.
# Time Complexity: O((V + E) log V) using a Min-Heap.
# Space Complexity: O(V) (For storing visited nodes and priority queue)

import heapq  # Import heapq for priority queue (min-heap)

def prim(graph, start):
    """
    Function to perform Prim’s Algorithm.
    :param graph: Dictionary representing adjacency list of the graph with weighted edges
    :param start: Starting node for MST
    :return: List of edges forming the Minimum Spanning Tree (MST)
    """
    mst = []  # Store MST edges
    visited = set()  # Track visited nodes
    priority_queue = [(0, start, None)]  # Min-Heap (weight, node, parent)

    while priority_queue:
        weight, node, parent = heapq.heappop(priority_queue)  # Get the smallest edge

        if node not in visited:
            visited.add(node)  # Mark node as visited
            if parent:
                mst.append((parent, node, weight))  # Add edge to MST

            for neighbor, edge_weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, node))  # Push neighbor

    return mst  # Return MST edges


# Example Graph (Adjacency List with Weights)
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('C', 4), ('D', 2)],
    'C': [('A', 5), ('B', 4), ('D', 6), ('E', 3)],
    'D': [('B', 2), ('C', 6), ('E', 7)],
    'E': [('C', 3), ('D', 7)]
}

# Perform Prim’s Algorithm from 'A'
mst = prim(graph, 'A')
print("Minimum Spanning Tree using Prim's Algorithm:", mst)
