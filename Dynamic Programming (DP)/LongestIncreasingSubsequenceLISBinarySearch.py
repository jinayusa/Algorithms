# Longest Increasing Subsequence using Binary Search (O(n log n))

# Instead of maintaining a DP array, we use a list (`sub[]`) that gets updated using Binary Search.
# Time Complexity: O(n log n) (Binary Search in `sub[]`)
# Space Complexity: O(n) (for `sub[]` list)

from bisect import bisect_left

def lis_binary_search(arr):
    """
    Function to compute LIS using Binary Search.
    :param arr: Input sequence
    :return: Length of LIS
    """
    sub = []  # List to store LIS
    for num in arr:
        idx = bisect_left(sub, num)  # Find position in sub[] where num fits
        if idx == len(sub):
            sub.append(num)  # Append if num extends LIS
        else:
            sub[idx] = num  # Replace to maintain the smallest possible LIS

    return len(sub)  # Length of sub[] gives LIS length


# Example Usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(f"LIS Length using Binary Search: {lis_binary_search(arr)}")
