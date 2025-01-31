# Matrix Chain Multiplication using Bottom-Up DP (Tabulation)

# Tabulation fills a DP table iteratively without recursion.
# Time Complexity: O(n^3)
# Space Complexity: O(n^2) (for DP table)

import sys

def mcm_tabulation(p):
    """
    Function to compute MCM using Bottom-Up Tabulation.
    :param p: List of matrix dimensions
    :return: Minimum multiplication cost
    """
    n = len(p) - 1  # Number of matrices
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # DP table

    for length in range(2, n + 1):  # Chain length
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]  # Minimum cost to multiply all matrices


# Example Usage:
dimensions = [10, 20, 30, 40, 30]
print(f"Minimum cost using Tabulation: {mcm_tabulation(dimensions)}")
