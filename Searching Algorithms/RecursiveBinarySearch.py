# Binary Search Implementation (Recursive)

def binary_search_recursive(arr, left, right, target):
    """
    Function to perform Binary Search (Recursive).
    :param arr: Sorted list of numbers
    :param left: Left boundary index
    :param right: Right boundary index
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    if left > right:
        return -1  # Base case: Target not found

    mid = left + (right - left) // 2  # Calculate middle index

    if arr[mid] == target:
        return mid  # Element found, return index
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)  # Search right half
    else:
        return binary_search_recursive(arr, left, mid - 1, target)  # Search left half


# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search_recursive(arr, 0, len(arr) - 1, target)
print(f"Element {target} found at index:", result)
