# Longest Common Subsequence using Bottom-Up DP (Tabulation)

# Tabulation fills a DP table iteratively without recursion.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (for DP table)

def lcs_tabulation(X, Y):
    """
    Function to compute LCS using Bottom-Up Tabulation.
    :param X: First string
    :param Y: Second string
    :return: Length of LCS
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # Initialize DP table

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # If last characters match
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]  # Return LCS length


# Example Usage:
X = "AGGTAB"
Y = "GXTXAYB"
print(f"LCS Length using Tabulation: {lcs_tabulation(X, Y)}")
