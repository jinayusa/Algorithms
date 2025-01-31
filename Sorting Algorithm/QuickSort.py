# QuickSort Implementation in Python

# QuickSort follows the divide and conquer strategy:
# 1. Pick a pivot.
# 2. Partition the array into elements < pivot and > pivot.
# 3. Recursively apply QuickSort to partitions.
# Time Complexity: Best/Average - O(n log n), Worst - O(n^2) [when the pivot is poorly chosen]
# Space Complexity: O(log n) for recursion stack (in-place sorting)

def quicksort(arr):
    """
    Function to perform QuickSort.
    :param arr: List of numbers
    :return: Sorted list
    """
    # Base Case: If the list has 0 or 1 element, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Choosing the pivot as the middle element (better for balanced partitions)
    pivot = arr[len(arr) // 2]

    # Partitioning: Elements < pivot, elements == pivot, elements > pivot
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply QuickSort to left and right parts
    return quicksort(left) + middle + quicksort(right)


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted Array:", sorted_arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
