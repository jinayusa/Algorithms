# Count Ways to Make Change

# Time Complexity: O(n * amount)
# Space Complexity: O(amount)

def count_ways(coins, amount):
    """
    Function to compute the total number of ways to make a given amount.
    :param coins: List of coin denominations
    :param amount: Target amount
    :return: Total number of ways to make the amount
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # There's 1 way to make amount 0 (using no coins)

    for coin in coins:  # Process each coin
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]  # Add ways to make `i` using current coin

    return dp[amount]


# Example Usage:
coins = [1, 2, 5]
amount = 5
print(f"Total ways to make change: {count_ways(coins, amount)}")
