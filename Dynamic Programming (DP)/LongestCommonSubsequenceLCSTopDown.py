# Longest Common Subsequence using Memoization (Top-Down DP)

# Memoization avoids redundant calculations by storing results.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (for memoization table)

def lcs_memoization(X, Y, m, n, memo):
    """
    Function to compute LCS using Top-Down Memoization.
    :param X: First string
    :param Y: Second string
    :param m: Length of X
    :param n: Length of Y
    :param memo: Dictionary to store computed results
    :return: Length of LCS
    """
    if m == 0 or n == 0:
        return 0

    if (m, n) in memo:  # Check if already computed
        return memo[(m, n)]

    if X[m - 1] == Y[n - 1]:  # If last characters match
        memo[(m, n)] = 1 + lcs_memoization(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs_memoization(X, Y, m, n - 1, memo), 
                            lcs_memoization(X, Y, m - 1, n, memo))
    
    return memo[(m, n)]


# Example Usage:
X = "AGGTAB"
Y = "GXTXAYB"
memo = {}  # Dictionary to store results
print(f"LCS Length using Memoization: {lcs_memoization(X, Y, len(X), len(Y), memo)}")
