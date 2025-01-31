# Minimum Coins for Coin Change (Fewest Coins Required)

# Time Complexity: O(n * amount)
# Space Complexity: O(amount)

import sys

def min_coins(coins, amount):
    """
    Function to compute the minimum number of coins needed to make an amount.
    :param coins: List of coin denominations
    :param amount: Target amount
    :return: Minimum number of coins required (or -1 if not possible)
    """
    dp = [sys.maxsize] * (amount + 1)  # Initialize DP array with a large value
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    for coin in coins:
        for i in range(coin, amount + 1):  # Loop through all amounts from coin value to target
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Take the minimum coins needed

    return dp[amount] if dp[amount] != sys.maxsize else -1  # Return -1 if no solution


# Example Usage:
coins = [1, 2, 5]
amount = 11
print(f"Minimum coins required: {min_coins(coins, amount)}")
