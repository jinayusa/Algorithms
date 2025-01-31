# Kruskal’s Algorithm Implementation in Python

# Kruskal's Algorithm finds the Minimum Spanning Tree using a greedy approach.
# Time Complexity: O(E log E) (Sorting edges + Union-Find operations)
# Space Complexity: O(V) (For storing parent and rank arrays)

class DisjointSet:
    """Union-Find data structure with path compression and union by rank."""
    
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  # Each node is its own parent
        self.rank = {v: 0 for v in vertices}  # Rank for union by rank

    def find(self, node):
        """Find the representative (root) of a set."""
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        """Union two sets by rank."""
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    """
    Function to perform Kruskal’s Algorithm.
    :param graph: List of tuples (source, destination, weight)
    :return: List of edges forming the Minimum Spanning Tree (MST)
    """
    mst = []  # Store MST edges
    edges = sorted(graph, key=lambda edge: edge[2])  # Step 1: Sort edges by weight
    vertices = set(sum([[edge[0], edge[1]] for edge in graph], []))  # Extract unique vertices
    ds = DisjointSet(vertices)  # Initialize Disjoint Set

    for edge in edges:  # Step 2: Iterate over sorted edges
        u, v, weight = edge
        if ds.find(u) != ds.find(v):  # Check if adding this edge forms a cycle
            ds.union(u, v)  # Union the sets
            mst.append((u, v, weight))  # Add edge to MST

    return mst  # Return MST edges


# Example Graph (Edge List with Weights)
graph = [
    ('A', 'B', 1),
    ('A', 'C', 5),
    ('B', 'C', 4),
    ('B', 'D', 2),
    ('C', 'D', 6),
    ('C', 'E', 3),
    ('D', 'E', 7)
]

# Perform Kruskal’s Algorithm
mst = kruskal(graph)
print("Minimum Spanning Tree using Kruskal's Algorithm:", mst)
