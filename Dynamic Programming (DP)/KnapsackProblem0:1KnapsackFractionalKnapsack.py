# 0/1 Knapsack using Dynamic Programming (Bottom-Up Approach)

# Time Complexity: O(n * W)
# Space Complexity: O(n * W) (for DP table)

def knapsack_01(weights, values, capacity):
    """
    Function to compute the maximum value in 0/1 Knapsack using Dynamic Programming.
    :param weights: List of item weights
    :param values: List of item values
    :param capacity: Maximum knapsack capacity
    :return: Maximum value that can be obtained
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # DP table initialization

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If item fits in knapsack
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]  # Exclude the item

    return dp[n][capacity]  # Maximum value at full capacity


# Example Usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(f"Maximum value in 0/1 Knapsack: {knapsack_01(weights, values, capacity)}")
