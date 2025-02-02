# Fenwick Tree (BIT) Implementation

class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) for Range Sum Queries"""
    
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i, num in enumerate(nums):
            self.add(i, num)

    def add(self, index, value):
        """
        Updates the Fenwick Tree at a given index.
        Time Complexity: O(log N)
        """
        index += 1  # Fenwick Tree is 1-based
        while index <= self.n:
            self.tree[index] += value
            index += index & -index  # Move to next index

    def sum(self, index):
        """
        Returns the prefix sum from 0 to index.
        Time Complexity: O(log N)
        """
        index += 1
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & -index  # Move to parent index
        return sum_val

    def range_sum(self, left, right):
        """
        Returns the sum in range [left, right].
        Time Complexity: O(log N)
        """
        return self.sum(right) - self.sum(left - 1)

# Example Usage
nums = [1, 3, 5, 7, 9, 11]
fenwick = FenwickTree(nums)
print("Range Sum (2, 5):", fenwick.range_sum(2, 5))  # Output: 32
fenwick.add(3, 3)  # Increment nums[3] by 3 (7 → 10)
print("Range Sum (2, 5) after update:", fenwick.range_sum(2, 5))  # Output: 35
