# Longest Common Subsequence using Recursion

# The naive recursive approach recomputes overlapping subproblems.
# Time Complexity: O(2^n) (Exponential)
# Space Complexity: O(n) (Recursion stack)

def lcs_recursive(X, Y, m, n):
    """
    Function to compute LCS using naive recursion.
    :param X: First string
    :param Y: Second string
    :param m: Length of X
    :param n: Length of Y
    :return: Length of LCS
    """
    if m == 0 or n == 0:  # Base case: If any string is empty
        return 0

    if X[m - 1] == Y[n - 1]:  # If last characters match
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))


# Example Usage:
X = "AGGTAB"
Y = "GXTXAYB"
print(f"LCS Length using Recursion: {lcs_recursive(X, Y, len(X), len(Y))}")
