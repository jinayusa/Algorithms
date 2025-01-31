# Iterative QuickSort in Python using an explicit stack

def partition(arr, low, high):
    """
    Function to partition the array and place pivot in its correct position.
    :param arr: List of numbers
    :param low: Starting index
    :param high: Ending index
    :return: Index of pivot after partitioning
    """
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  # Pointer for smaller elements

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot at correct position
    return i + 1  # Return pivot index


def quicksort_iterative(arr):
    """
    Iterative QuickSort using a manual stack.
    :param arr: List of numbers
    """
    stack = [(0, len(arr) - 1)]  # Initialize stack with full range of array

    while stack:
        low, high = stack.pop()  # Get range to process
        if low < high:
            pivot_index = partition(arr, low, high)  # Get pivot index

            # Push left subarray to stack
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))

            # Push right subarray to stack
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
quicksort_iterative(arr)
print("Sorted Array:", arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
