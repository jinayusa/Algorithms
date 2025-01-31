# Linear Search Implementation in Python

# Linear Search works by checking each element one by one.
# Time Complexity: O(n) in worst case, O(1) in best case.
# Space Complexity: O(1) since no extra memory is used.

def linear_search(arr, target):
    """
    Function to perform Linear Search.
    :param arr: List of numbers
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    for index in range(len(arr)):  # Loop through each element in the list
        if arr[index] == target:  # If element matches the target
            return index  # Return the index of the target element

    return -1  # Target not found


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
target = 9
result = linear_search(arr, target)
print(f"Element {target} found at index:", result)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return -1
# 2. Single-element array (target present): [5], target = 5 -> Should return 0
# 3. Single-element array (target absent): [5], target = 2 -> Should return -1
# 4. Target at start: [1, 2, 3, 4], target = 1 -> Should return 0
# 5. Target at end: [1, 2, 3, 4], target = 4 -> Should return 3
# 6. Target not present: [1, 3, 5, 7], target = 6 -> Should return -1
