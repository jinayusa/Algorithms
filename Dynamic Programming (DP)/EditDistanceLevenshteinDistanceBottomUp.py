# Edit Distance using Bottom-Up DP (Tabulation)

# Tabulation fills a DP table iteratively without recursion.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (for DP table)

def edit_distance_tabulation(word1, word2):
    """
    Function to compute Edit Distance using Bottom-Up Tabulation.
    :param word1: First string
    :param word2: Second string
    :return: Minimum edit distance
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # DP table initialization

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # If first string is empty, insert all characters
            elif j == 0:
                dp[i][j] = i  # If second string is empty, delete all characters
            elif word1[i - 1] == word2[j - 1]:  # If last characters match
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    # Insert
                                   dp[i - 1][j],    # Delete
                                   dp[i - 1][j - 1]) # Replace

    return dp[m][n]  # Minimum edit distance


# Example Usage:
word1 = "horse"
word2 = "ros"
print(f"Edit Distance (Tabulation): {edit_distance_tabulation(word1, word2)}")
