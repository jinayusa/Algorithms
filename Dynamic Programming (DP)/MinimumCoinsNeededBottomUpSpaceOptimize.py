# Space-Optimized DP for Minimum Coins

# Time Complexity: O(n * amount)
# Space Complexity: O(amount)

def min_coins_optimized(coins, amount):
    """
    Function to compute the minimum number of coins needed using space-optimized DP.
    :param coins: List of coin denominations
    :param amount: Target amount
    :return: Minimum number of coins required (or -1 if not possible)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Example Usage:
coins = [1, 2, 5]
amount = 11
print(f"Minimum coins required (Optimized): {min_coins_optimized(coins, amount)}")
