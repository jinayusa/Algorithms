# Counting Sort Implementation in Python

# Counting Sort is an efficient sorting algorithm when the range of input data is known and small.
# It works by counting the occurrences of each unique element in the input array and using this 
# information to place the elements in the correct sorted order.
# Time Complexity: O(n + k), where n is the number of elements in the array and k is the range of the input values
# Space Complexity: O(k), where k is the range of the input values (size of the count array)

def counting_sort(arr):
    """
    Function to perform Counting Sort on an array.
    :param arr: List of numbers (array to be sorted)
    :return: Sorted list of numbers
    """
    if not arr:  # Edge case: Empty array
        return arr

    # Step 1: Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)

    # Step 2: Initialize a count array with zeroes for all possible values
    range_of_elements = max_val - min_val + 1  # Range of the numbers in the array
    count = [0] * range_of_elements  # Create count array of size "range_of_elements"
    
    # Step 3: Store the count of each element in the count array
    for num in arr:
        count[num - min_val] += 1  # Decrease by min_val to shift to zero-based index

    # Step 4: Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_of_elements):
        sorted_arr.extend([i + min_val] * count[i])  # Append each number based on its frequency

    return sorted_arr


# Example Usage:
arr = [10, 7, 8, 9, 1, 5, 10, 7]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)

# Edge Cases Considered:
# 1. Empty array: [] -> Should return []
# 2. Single-element array: [5] -> Should return [5]
# 3. Already sorted: [1, 2, 3, 4, 5] -> Should return [1, 2, 3, 4, 5]
# 4. Reverse sorted: [5, 4, 3, 2, 1] -> Should return [1, 2, 3, 4, 5]
# 5. Duplicates present: [3, 1, 2, 3, 3, 4] -> Should return [1, 2, 3, 3, 3, 4]
