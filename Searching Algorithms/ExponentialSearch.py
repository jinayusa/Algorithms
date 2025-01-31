# Exponential Search Implementation in Python

# Exponential Search first finds a possible range and then applies Binary Search.
# Time Complexity: O(log n) in worst case.
# Space Complexity: O(1) since no extra memory is used.

def binary_search(arr, left, right, target):
    """
    Function to perform Binary Search.
    :param arr: Sorted list of numbers
    :param left: Left boundary index
    :param right: Right boundary index
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    while left <= right:
        mid = left + (right - left) // 2  # Calculate middle index

        if arr[mid] == target:
            return mid  # Target found at mid
        elif arr[mid] < target:
            left = mid + 1  # Search in right half
        else:
            right = mid - 1  # Search in left half

    return -1  # Target not found


def exponential_search(arr, target):
    """
    Function to perform Exponential Search.
    :param arr: Sorted list of numbers
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    if not arr:
        return -1  # Edge case: Empty array

    # Step 1: Check if target is the first element
    if arr[0] == target:
        return 0

    # Step 2: Find range for binary search
    n = len(arr)
    index = 1  # Start with a small range

    while index < n and arr[index] <= target:
        index *= 2  # Exponentially increase the search range

    # Step 3: Perform Binary Search within the identified range
    return binary_search(arr, index // 2, min(index, n - 1), target)


# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted array
target = 9
result = exponential_search(arr, target)
print(f"Element {target} found at index:", result)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return -1
# 2. Single-element array (target present): [5], target = 5 -> Should return 0
# 3. Single-element array (target absent): [5], target = 2 -> Should return -1
# 4. Target at start: [1, 2, 3, 4], target = 1 -> Should return 0
# 5. Target at end: [1, 2, 3, 4], target = 4 -> Should return 3
# 6. Target not present: [1, 3, 5, 7], target = 6 -> Should return -1
