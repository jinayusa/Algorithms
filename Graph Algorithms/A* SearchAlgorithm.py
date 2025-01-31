# A* Search Algorithm Implementation in Python

# A* finds the shortest path using heuristic estimates.
# Time Complexity: O(E) in the worst case.
# Space Complexity: O(V) (For storing paths)

import heapq  # Import heapq for priority queue (min-heap)

def a_star_search(graph, start, goal, heuristic):
    """
    Function to perform A* Search Algorithm.
    :param graph: Dictionary representing adjacency list of the graph with weighted edges
    :param start: Starting node
    :param goal: Goal node
    :param heuristic: Dictionary containing estimated cost to reach the goal from each node
    :return: Shortest path from start to goal
    """
    priority_queue = []  # Min-heap priority queue
    heapq.heappush(priority_queue, (0 + heuristic[start], 0, start, []))  # (f, g, node, path)
    
    visited = set()  # Set to track visited nodes

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)  # Pop node with lowest f(x)

        if current in visited:
            continue  # Ignore already visited nodes

        path = path + [current]  # Update the path
        visited.add(current)  # Mark node as visited

        if current == goal:
            return path  # Goal reached, return path

        # Explore neighbors
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                g_new = g + weight  # Update cost to reach neighbor
                f_new = g_new + heuristic[neighbor]  # Compute f(x)
                heapq.heappush(priority_queue, (f_new, g_new, neighbor, path))  # Push to queue

    return None  # No path found


# Example Graph (Adjacency List with Weights)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 10)],
    'C': [('E', 3)],
    'D': [('F', 3)],
    'E': [('F', 4)],
    'F': []
}

# Heuristic Estimates (Straight-line distance to goal 'F')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0  # Goal node heuristic is always 0
}

# Perform A* Search from 'A' to 'F'
shortest_path = a_star_search(graph, 'A', 'F', heuristic)
print("Shortest Path from 'A' to 'F':", shortest_path)

# Edge Cases Considered:
# 1. Graph with cycles
# 2. Graph with multiple possible paths
# 3. Graph with disconnected components
# 4. Empty graph
# 5. Single-node graph
