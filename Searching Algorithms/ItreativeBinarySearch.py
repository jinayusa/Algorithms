# Binary Search Implementation (Iterative)

# Binary Search works by repeatedly dividing the search space into half.
# Time Complexity: O(log n) (because we halve the search space each time)
# Space Complexity: O(1) (since it doesn't use extra memory)

def binary_search(arr, target):
    """
    Function to perform Binary Search (Iterative).
    :param arr: Sorted list of numbers
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    left, right = 0, len(arr) - 1  # Initialize search boundaries

    while left <= right:
        mid = left + (right - left) // 2  # Calculate middle index

        if arr[mid] == target:
            return mid  # Element found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Element not found


# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)
print(f"Element {target} found at index:", result)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return -1
# 2. Single-element array: [5], target = 5 -> Should return 0
# 3. Target at start: [1, 2, 3, 4], target = 1 -> Should return 0
# 4. Target at end: [1, 2, 3, 4], target = 4 -> Should return 3
# 5. Target not present: [1, 3, 5, 7], target = 6 -> Should return -1
