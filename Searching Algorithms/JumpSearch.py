# Jump Search Implementation in Python

# Jump Search works by dividing the array into blocks of size √n and searching in steps.
# Time Complexity: O(√n) in worst case.
# Space Complexity: O(1) since no extra memory is used.

import math  # Import math for square root calculation

def jump_search(arr, target):
    """
    Function to perform Jump Search.
    :param arr: Sorted list of numbers
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    n = len(arr)  # Length of the array
    block_size = int(math.sqrt(n))  # Optimal block size = √n

    # Step 1: Jump in steps of block_size
    prev = 0
    while prev < n and arr[min(prev + block_size, n) - 1] < target:
        prev += block_size  # Move to next block

    # Step 2: Perform Linear Search in the identified block
    for index in range(prev, min(prev + block_size, n)):
        if arr[index] == target:
            return index  # Target found, return index

    return -1  # Target not found


# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted array
target = 9
result = jump_search(arr, target)
print(f"Element {target} found at index:", result)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return -1
# 2. Single-element array (target present): [5], target = 5 -> Should return 0
# 3. Single-element array (target absent): [5], target = 2 -> Should return -1
# 4. Target at start: [1, 2, 3, 4], target = 1 -> Should return 0
# 5. Target at end: [1, 2, 3, 4], target = 4 -> Should return 3
# 6. Target not present: [1, 3, 5, 7], target = 6 -> Should return -1
