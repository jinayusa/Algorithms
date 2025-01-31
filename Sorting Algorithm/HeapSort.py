# Heap Sort Implementation in Python

# Heap Sort works by first building a Max Heap and then sorting the array
# Time Complexity: O(n log n) (heapify takes log n, and it's done for each element)
# Space Complexity: O(1) (in-place sorting)

def heapify(arr, n, i):
    """
    Function to maintain the heap property by pushing the largest element to the root.
    :param arr: List of numbers
    :param n: Size of heap
    :param i: Index of root node
    """
    largest = i  # Assume current node (i) is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


def heap_sort(arr):
    """
    Heap Sort function to sort an array.
    :param arr: List of numbers
    """
    n = len(arr)

    # Step 1: Build a Max Heap from the input array
    for i in range(n // 2 - 1, -1, -1):  # Start from last non-leaf node
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max element) with last element
        heapify(arr, i, 0)  # Heapify the reduced heap


# Example Usage:
arr = [10, 7, 8, 9, 1, 5]
heap_sort(arr)
print("Sorted Array:", arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
