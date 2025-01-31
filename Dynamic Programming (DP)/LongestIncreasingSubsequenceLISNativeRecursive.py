# Longest Increasing Subsequence using Recursion

# The naive recursive approach recomputes overlapping subproblems.
# Time Complexity: O(2^n) (Exponential)
# Space Complexity: O(n) (Recursion stack)

def lis_recursive(arr, n, prev=float('-inf')):
    """
    Function to compute LIS using naive recursion.
    :param arr: Input sequence
    :param n: Current index in arr
    :param prev: Previous element in LIS
    :return: Length of LIS
    """
    if n == 0:
        return 0

    # Exclude the current element
    exclude = lis_recursive(arr, n - 1, prev)

    # Include the current element if it is larger than prev
    include = 0
    if arr[n - 1] > prev:
        include = 1 + lis_recursive(arr, n - 1, arr[n - 1])

    return max(include, exclude)


# Example Usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(f"LIS Length using Recursion: {lis_recursive(arr, len(arr))}")
