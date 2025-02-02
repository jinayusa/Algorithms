# Using HashMap for frequency counting
def count_frequencies(nums):
    """
    Counts occurrences of elements using a HashMap (Dictionary).

    Time Complexity: O(N) (Iterates through the list once)
    Space Complexity: O(N) (Stores counts for each unique number)
    """
    frequency_map = {}  # HashMap to store counts
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1  # Update count
    return frequency_map

# Using HashSet for fast lookups
def contains_duplicates(nums):
    """
    Checks if a list contains duplicates using a HashSet.

    Time Complexity: O(N) (Each element is inserted once)
    Space Complexity: O(N) (HashSet stores unique elements)
    """
    seen = set()  # HashSet to store unique values
    for num in nums:
        if num in seen:  # Fast O(1) lookup
            return True
        seen.add(num)
    return False  # No duplicates found

# Example Usage
nums1 = [1, 2, 3, 1, 2, 3, 3, 4]
nums2 = [4, 7, 9, 2]

print("Frequency Count:", count_frequencies(nums1))  # Output: {1: 2, 2: 2, 3: 3, 4: 1}
print("Contains Duplicates (Example 1):", contains_duplicates(nums1))  # Output: True
print("Contains Duplicates (Example 2):", contains_duplicates(nums2))  # Output: False
