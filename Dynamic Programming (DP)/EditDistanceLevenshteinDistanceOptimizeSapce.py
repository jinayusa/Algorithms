# Edit Distance using Space-Optimized DP

# Instead of storing an entire DP table, we store only two rows.
# Time Complexity: O(m * n)
# Space Complexity: O(n) (Reduced from O(m * n))

def edit_distance_space_optimized(word1, word2):
    """
    Function to compute Edit Distance using a space-optimized DP approach.
    :param word1: First string
    :param word2: Second string
    :return: Minimum edit distance
    """
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))  # Previous row
    curr = [0] * (n + 1)  # Current row

    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev  # Swap rows

    return prev[n]


# Example Usage:
word1 = "horse"
word2 = "ros"
print(f"Edit Distance (Space Optimization): {edit_distance_space_optimized(word1, word2)}")
