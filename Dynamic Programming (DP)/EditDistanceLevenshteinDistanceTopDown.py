# Edit Distance using Memoization (Top-Down DP)

# Memoization avoids redundant calculations by storing results.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (for memoization table)

def edit_distance_memo(word1, word2, m, n, memo):
    """
    Function to compute Edit Distance using Memoization.
    :param word1: First string
    :param word2: Second string
    :param m: Length of word1
    :param n: Length of word2
    :param memo: Dictionary to store computed results
    :return: Minimum edit distance
    """
    if m == 0: return n
    if n == 0: return m
    if (m, n) in memo:  # Check if already computed
        return memo[(m, n)]

    if word1[m - 1] == word2[n - 1]:
        memo[(m, n)] = edit_distance_memo(word1, word2, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = 1 + min(
            edit_distance_memo(word1, word2, m, n - 1, memo),    # Insert
            edit_distance_memo(word1, word2, m - 1, n, memo),    # Delete
            edit_distance_memo(word1, word2, m - 1, n - 1, memo) # Replace
        )

    return memo[(m, n)]


# Example Usage:
word1 = "horse"
word2 = "ros"
memo = {}
print(f"Edit Distance (Memoization): {edit_distance_memo(word1, word2, len(word1), len(word2), memo)}")
