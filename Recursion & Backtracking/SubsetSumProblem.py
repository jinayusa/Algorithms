# Subset Sum Problem using Recursion and Dynamic Programming

def subset_sum_recursive(nums, target, index=0):
    """
    Recursively checks if a subset sum exists.

    Time Complexity: O(2^N) (Exponential)
    Space Complexity: O(N) (Recursive stack)
    """
    # Base Cases
    if target == 0:
        return True  # Found a subset
    if index >= len(nums) or target < 0:
        return False  # Out of bounds or negative sum

    # Choice 1: Include the current element
    include = subset_sum_recursive(nums, target - nums[index], index + 1)

    # Choice 2: Exclude the current element
    exclude = subset_sum_recursive(nums, target, index + 1)

    return include or exclude  # Return True if either choice leads to success

def subset_sum_dp(nums, target):
    """
    Dynamic Programming approach to check if a subset sum exists.

    Time Complexity: O(N × Target)
    Space Complexity: O(Target)
    """
    dp = [False] * (target + 1)  # Initialize DP array
    dp[0] = True  # Base case: Subset sum of 0 is always possible

    for num in nums:
        for j in range(target, num - 1, -1):  # Traverse backward to avoid overwriting
            dp[j] = dp[j] or dp[j - num]

    return dp[target]  # Final answer is whether target sum is possible

# Example Usage
nums = [3, 34, 4, 12, 5, 2]
target = 9

# Using Recursion
print("Using Recursion:", subset_sum_recursive(nums, target))  # Output: True

# Using DP
print("Using Dynamic Programming:", subset_sum_dp(nums, target))  # Output: True
