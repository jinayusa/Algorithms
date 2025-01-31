# Merge Sort Implementation in Python

# Merge Sort follows the Divide and Conquer strategy:
# 1. Recursively divide the array into two halves.
# 2. Sort each half and merge them back in sorted order.
# Time Complexity: Best/Average/Worst - O(n log n)
# Space Complexity: O(n) due to temporary arrays used for merging.

def merge_sort(arr):
    """
    Function to perform Merge Sort.
    :param arr: List of numbers
    :return: Sorted list
    """
    if len(arr) <= 1:  # Base Case: If array has 0 or 1 element, it's already sorted
        return arr

    # Find the middle index
    mid = len(arr) // 2

    # Recursively divide the array into two halves
    left_half = merge_sort(arr[:mid])  # Sorting the left half
    right_half = merge_sort(arr[mid:])  # Sorting the right half

    # Merge sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Function to merge two sorted lists.
    :param left: Sorted left half
    :param right: Sorted right half
    :return: Merged sorted list
    """
    sorted_arr = []  # Temporary list for sorted elements
    i = j = 0  # Pointers for left and right halves

    # Compare elements in both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])  # Append smaller element
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If elements are left in either half, append them (they are already sorted)
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
