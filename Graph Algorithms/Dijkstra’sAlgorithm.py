# Dijkstra's Algorithm Implementation in Python

# Dijkstra's Algorithm finds the shortest path in a weighted graph with non-negative weights.
# Time Complexity: O((V + E) log V) using a min-heap priority queue
# Space Complexity: O(V) for storing distances

import heapq  # Import heapq for priority queue (min-heap)

def dijkstra(graph, start):
    """
    Function to perform Dijkstra’s Algorithm for shortest path.
    :param graph: Dictionary representing adjacency list of the graph with weighted edges
    :param start: Starting node for Dijkstra's Algorithm
    :return: Dictionary containing shortest distances from start node to all other nodes
    """
    priority_queue = []  # Min-heap priority queue
    heapq.heappush(priority_queue, (0, start))  # Push (distance, node) into the queue
    
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start] = 0  # Set start node distance to 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Get node with shortest distance

        if current_distance > distances[current_node]:  # Ignore outdated longer paths
            continue

        for neighbor, weight in graph[current_node]:  # Explore neighbors
            distance = current_distance + weight  # Calculate new distance
            
            if distance < distances[neighbor]:  # Found a shorter path
                distances[neighbor] = distance  # Update shortest distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Push to priority queue

    return distances  # Return shortest distance to all nodes


# Example Graph (Adjacency List with Weights)
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 2), ('E', 5)],
    'C': [('A', 1), ('D', 8)],
    'D': [('B', 2), ('C', 8), ('E', 3)],
    'E': [('B', 5), ('D', 3)]
}

# Perform Dijkstra’s Algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from 'A':", shortest_paths)

# Edge Cases Considered:
# 1. Graph with isolated nodes
# 2. Graph with cycles
# 3. Graph with a single node
# 4. Graph with disconnected components
# 5. Empty graph
