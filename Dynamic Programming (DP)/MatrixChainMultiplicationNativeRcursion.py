# Matrix Chain Multiplication using Recursion

# The naive recursive approach recomputes overlapping subproblems.
# Time Complexity: O(2^n) (Exponential)
# Space Complexity: O(n) (Recursion stack)

import sys

def mcm_recursive(p, i, j):
    """
    Function to compute MCM using naive recursion.
    :param p: List of matrix dimensions
    :param i: Start index
    :param j: End index
    :return: Minimum multiplication cost
    """
    if i == j:
        return 0  # Single matrix, no cost

    min_cost = sys.maxsize  # Initialize with a large value

    for k in range(i, j):  # Try different partitions
        cost = (mcm_recursive(p, i, k) +
                mcm_recursive(p, k + 1, j) +
                p[i - 1] * p[k] * p[j])  # Compute cost

        min_cost = min(min_cost, cost)  # Update minimum cost

    return min_cost


# Example Usage:
dimensions = [10, 20, 30, 40, 30]
n = len(dimensions) - 1
print(f"Minimum cost using Recursion: {mcm_recursive(dimensions, 1, n)}")
