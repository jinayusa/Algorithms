# Edit Distance using Recursion

# The naive recursive approach recomputes overlapping subproblems.
# Time Complexity: O(3^n) (Exponential)
# Space Complexity: O(n) (Recursion stack)

def edit_distance_recursive(word1, word2, m, n):
    """
    Function to compute Edit Distance using naive recursion.
    :param word1: First string
    :param word2: Second string
    :param m: Length of word1
    :param n: Length of word2
    :return: Minimum edit distance
    """
    if m == 0: return n  # If first string is empty, insert all characters
    if n == 0: return m  # If second string is empty, delete all characters

    if word1[m - 1] == word2[n - 1]:  # If last characters match, ignore them
        return edit_distance_recursive(word1, word2, m - 1, n - 1)

    # Try insert, delete, and replace operations
    return 1 + min(
        edit_distance_recursive(word1, word2, m, n - 1),    # Insert
        edit_distance_recursive(word1, word2, m - 1, n),    # Delete
        edit_distance_recursive(word1, word2, m - 1, n - 1) # Replace
    )


# Example Usage:
word1 = "horse"
word2 = "ros"
print(f"Edit Distance (Recursive): {edit_distance_recursive(word1, word2, len(word1), len(word2))}")
