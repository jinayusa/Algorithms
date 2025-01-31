# Ternary Search Implementation (Iterative)

# Ternary Search works by dividing the search space into three parts.
# Time Complexity: O(log₃ n) (reduces search space by 1/3 each iteration)
# Space Complexity: O(1) (does not use extra memory)

def ternary_search(arr, target):
    """
    Function to perform Ternary Search (Iterative).
    :param arr: Sorted list of numbers
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    left, right = 0, len(arr) - 1  # Initialize search boundaries

    while left <= right:
        mid1 = left + (right - left) // 3  # First mid-point
        mid2 = right - (right - left) // 3  # Second mid-point

        if arr[mid1] == target:
            return mid1  # Target found at mid1
        if arr[mid2] == target:
            return mid2  # Target found at mid2

        if target < arr[mid1]:  # Search in the leftmost part
            right = mid1 - 1
        elif target > arr[mid2]:  # Search in the rightmost part
            left = mid2 + 1
        else:  # Search in the middle part
            left = mid1 + 1
            right = mid2 - 1

    return -1  # Target not found


# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted array
target = 9
result = ternary_search(arr, target)
print(f"Element {target} found at index:", result)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return -1
# 2. Single-element array (target present): [5], target = 5 -> Should return 0
# 3. Single-element array (target absent): [5], target = 2 -> Should return -1
# 4. Target at start: [1, 2, 3, 4], target = 1 -> Should return 0
# 5. Target at end: [1, 2, 3, 4], target = 4 -> Should return 3
# 6. Target not present: [1, 3, 5, 7], target = 6 -> Should return -1
