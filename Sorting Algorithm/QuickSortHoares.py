# Optimized QuickSort using Hoare’s Partition Scheme (Iterative Version)

def hoare_partition(arr, low, high):
    """
    Hoare's Partitioning: Uses two pointers moving toward each other.
    :param arr: List of numbers
    :param low: Starting index
    :param high: Ending index
    :return: Pivot index (not necessarily final position)
    """
    pivot = arr[low]  # Choosing the first element as pivot
    i = low - 1  # Left pointer (outside range)
    j = high + 1  # Right pointer (outside range)

    while True:
        # Move i forward until finding an element greater than or equal to pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Move j backward until finding an element smaller than or equal to pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, partition is complete
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort_iterative_hoare(arr):
    """
    Iterative QuickSort using Hoare's partitioning.
    :param arr: List of numbers
    """
    stack = [(0, len(arr) - 1)]  # Initialize stack with the full range of array

    while stack:
        low, high = stack.pop()  # Get range to process

        if low < high:
            pivot_index = hoare_partition(arr, low, high)  # Get pivot index
            
            # Push left subarray to stack
            stack.append((low, pivot_index))

            # Push right subarray to stack
            stack.append((pivot_index + 1, high))


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
quicksort_iterative_hoare(arr)
print("Sorted Array:", arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
