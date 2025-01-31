# Longest Common Subsequence using Space-Optimized DP

# Instead of storing an entire DP table, we store only two rows.
# Time Complexity: O(m * n)
# Space Complexity: O(n) (reduced from O(m * n))

def lcs_space_optimized(X, Y):
    """
    Function to compute LCS using a space-optimized DP approach.
    :param X: First string
    :param Y: Second string
    :return: Length of LCS
    """
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)  # Previous row
    curr = [0] * (n + 1)  # Current row

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev  # Swap rows

    return prev[n]  # Final result


# Example Usage:
X = "AGGTAB"
Y = "GXTXAYB"
print(f"LCS Length using Space Optimization: {lcs_space_optimized(X, Y)}")
