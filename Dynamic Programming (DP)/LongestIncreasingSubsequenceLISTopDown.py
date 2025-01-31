# Longest Increasing Subsequence using Memoization (Top-Down DP)

# Memoization avoids redundant calculations by storing results.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2) (for memoization table)

def lis_memoization(arr, n, prev_index, memo):
    """
    Function to compute LIS using Top-Down Memoization.
    :param arr: Input sequence
    :param n: Current index in arr
    :param prev_index: Index of previous element in LIS
    :param memo: Dictionary to store computed results
    :return: Length of LIS
    """
    if n == 0:
        return 0

    if (n, prev_index) in memo:
        return memo[(n, prev_index)]

    # Exclude the current element
    exclude = lis_memoization(arr, n - 1, prev_index, memo)

    # Include the current element if it forms an increasing subsequence
    include = 0
    if prev_index == -1 or arr[n - 1] > arr[prev_index]:
        include = 1 + lis_memoization(arr, n - 1, n - 1, memo)

    memo[(n, prev_index)] = max(include, exclude)
    return memo[(n, prev_index)]


# Example Usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
memo = {}
print(f"LIS Length using Memoization: {lis_memoization(arr, len(arr), -1, memo)}")
