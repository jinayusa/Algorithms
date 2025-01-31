# Iterative MergeSort in Python (Bottom-Up Approach)

def merge(arr, temp, left, mid, right):
    """
    Function to merge two sorted subarrays into a single sorted subarray.
    :param arr: Original array
    :param temp: Temporary array for merging
    :param left: Left index of subarray
    :param mid: Middle index (end of left subarray)
    :param right: Right index of subarray
    """
    i, j, k = left, mid + 1, left  # i points to left, j points to right, k points to temp

    # Merge both halves into temp[]
    while i <= mid and j <= right:
        if arr[i] < arr[j]:  
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements from left half (if any)
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right half (if any)
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray back to the original array
    for i in range(left, right + 1):
        arr[i] = temp[i]


def merge_sort_iterative(arr):
    """
    Iterative MergeSort (Bottom-Up).
    :param arr: List of numbers
    """
    n = len(arr)
    temp = arr.copy()  # Temporary array for merging

    # Merge subarrays of size 1, then 2, then 4, etc.
    size = 1
    while size < n:
        left = 0
        while left < n - size:
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)
            merge(arr, temp, left, mid, right)
            left += 2 * size
        size *= 2  # Double the subarray size


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
merge_sort_iterative(arr)
print("Sorted Array:", arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
