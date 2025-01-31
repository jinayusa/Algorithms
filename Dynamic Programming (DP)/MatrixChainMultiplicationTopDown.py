# Matrix Chain Multiplication using Memoization (Top-Down DP)

# Memoization avoids redundant calculations by storing results.
# Time Complexity: O(n^3)
# Space Complexity: O(n^2) (for memoization table)

import sys

def mcm_memoization(p, i, j, memo):
    """
    Function to compute MCM using Memoization.
    :param p: List of matrix dimensions
    :param i: Start index
    :param j: End index
    :param memo: Dictionary to store computed results
    :return: Minimum multiplication cost
    """
    if i == j:
        return 0

    if (i, j) in memo:  # Check if already computed
        return memo[(i, j)]

    min_cost = sys.maxsize

    for k in range(i, j):
        cost = (mcm_memoization(p, i, k, memo) +
                mcm_memoization(p, k + 1, j, memo) +
                p[i - 1] * p[k] * p[j])

        min_cost = min(min_cost, cost)

    memo[(i, j)] = min_cost  # Store result
    return min_cost


# Example Usage:
dimensions = [10, 20, 30, 40, 30]
n = len(dimensions) - 1
memo = {}
print(f"Minimum cost using Memoization: {mcm_memoization(dimensions, 1, n, memo)}")
