# Ternary Search Implementation (Recursive)

def ternary_search_recursive(arr, left, right, target):
    """
    Function to perform Ternary Search (Recursive).
    :param arr: Sorted list of numbers
    :param left: Left boundary index
    :param right: Right boundary index
    :param target: Number to find
    :return: Index of target if found, else -1
    """
    if left > right:
        return -1  # Base case: Target not found

    mid1 = left + (right - left) // 3  # First mid-point
    mid2 = right - (right - left) // 3  # Second mid-point

    if arr[mid1] == target:
        return mid1  # Target found at mid1
    if arr[mid2] == target:
        return mid2  # Target found at mid2

    if target < arr[mid1]:  # Search in leftmost part
        return ternary_search_recursive(arr, left, mid1 - 1, target)
    elif target > arr[mid2]:  # Search in rightmost part
        return ternary_search_recursive(arr, mid2 + 1, right, target)
    else:  # Search in middle part
        return ternary_search_recursive(arr, mid1 + 1, mid2 - 1, target)


# Example Usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 9
result = ternary_search_recursive(arr, 0, len(arr) - 1, target)
print(f"Element {target} found at index:", result)
