# 0/1 Knapsack using Space-Optimized DP

# Time Complexity: O(n * W)
# Space Complexity: O(W) (Reduced from O(n * W))

def knapsack_01_optimized(weights, values, capacity):
    """
    Function to compute the maximum value in 0/1 Knapsack using space-optimized DP.
    :param weights: List of item weights
    :param values: List of item values
    :param capacity: Maximum knapsack capacity
    :return: Maximum value that can be obtained
    """
    n = len(weights)
    dp = [0] * (capacity + 1)  # 1D DP array

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):  # Traverse backwards to prevent overwriting
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


# Example Usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(f"Maximum value in Space-Optimized 0/1 Knapsack: {knapsack_01_optimized(weights, values, capacity)}")
