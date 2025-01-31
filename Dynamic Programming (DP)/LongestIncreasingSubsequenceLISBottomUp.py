# Longest Increasing Subsequence using Bottom-Up DP (Tabulation)

# Tabulation fills a DP table iteratively without recursion.
# Time Complexity: O(n^2)
# Space Complexity: O(n) (for DP array)

def lis_tabulation(arr):
    """
    Function to compute LIS using Bottom-Up Tabulation.
    :param arr: Input sequence
    :return: Length of LIS
    """
    n = len(arr)
    dp = [1] * n  # Initialize DP array with 1 (LIS of a single element is 1)

    for i in range(1, n):  # Iterate over each element
        for j in range(i):
            if arr[i] > arr[j]:  # If arr[i] can extend LIS ending at arr[j]
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The longest LIS is the maximum value in dp[]


# Example Usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(f"LIS Length using Tabulation: {lis_tabulation(arr)}")
