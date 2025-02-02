# Disjoint Set Union (Union-Find) with Path Compression and Union by Rank

class DisjointSet:
    """Disjoint Set Union (DSU) / Union-Find with Path Compression"""
    
    def __init__(self, size):
        """
        Initializes DSU with `size` elements (0 to size-1).
        Time Complexity: O(N) (for initialization)
        Space Complexity: O(N) (stores parent and rank arrays)
        """
        self.parent = [i for i in range(size)]  # Each node is its own parent
        self.rank = [1] * size  # Rank (height) of trees

    def find(self, node):
        """
        Finds the root of the set containing `node` using path compression.
        Time Complexity: O(α(N)) ≈ O(1) (Almost constant time)
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path Compression
        return self.parent[node]

    def union(self, node1, node2):
        """
        Merges two sets containing `node1` and `node2` using union by rank.
        Time Complexity: O(α(N)) ≈ O(1)
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:  # Attach smaller tree to larger tree
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:  # Same rank: Merge and increase rank
                self.parent[root2] = root1
                self.rank[root1] += 1

    def connected(self, node1, node2):
        """
        Checks if `node1` and `node2` belong to the same set.
        Time Complexity: O(α(N)) ≈ O(1)
        """
        return self.find(node1) == self.find(node2)

# Example Usage
dsu = DisjointSet(6)  # Initialize DSU with 6 elements (0 to 5)
dsu.union(1, 2)
dsu.union(3, 4)
dsu.union(2, 4)  # Connect components {1,2} and {3,4}

print("Are 1 and 3 connected?", dsu.connected(1, 3))  # Output: True
print("Are 1 and 5 connected?", dsu.connected(1, 5))  # Output: False
