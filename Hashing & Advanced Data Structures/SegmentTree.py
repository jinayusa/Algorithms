# Segment Tree for Range Sum Queries

class SegmentTree:
    """Segment Tree implementation for range sum queries."""
    
    def __init__(self, nums):
        """
        Initializes the segment tree.
        Time Complexity: O(N) (Building the tree)
        Space Complexity: O(2N) (Tree storage)
        """
        if not nums:
            self.nums = []
            self.tree = []
            return

        self.n = len(nums)
        self.tree = [0] * (2 * self.n)  # Segment tree array
        self.build(nums)

    def build(self, nums):
        """Builds the segment tree."""
        # Copy input array to the leaves of the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        # Fill the rest of the tree (Bottom-up approach)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]  # Parent stores sum of children

    def update(self, index, value):
        """
        Updates a value at the given index.
        Time Complexity: O(log N)
        """
        index += self.n  # Move index to the leaf
        self.tree[index] = value  # Update leaf node

        # Update parents
        while index > 1:
            index //= 2  # Move to parent node
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]  # Update sum

    def query(self, left, right):
        """
        Queries the sum in the range [left, right].
        Time Complexity: O(log N)
        """
        left += self.n  # Shift index to leaves
        right += self.n  # Shift index to leaves
        sum_val = 0  # Store sum
        
        while left <= right:
            if left % 2 == 1:  # If left is a right child
                sum_val += self.tree[left]
                left += 1
            if right % 2 == 0:  # If right is a left child
                sum_val += self.tree[right]
                right -= 1
            left //= 2  # Move to parent
            right //= 2  # Move to parent
        
        return sum_val

# Example Usage
nums = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(nums)
print("Range Sum (2, 5):", seg_tree.query(2, 5))  # Output: 5+7+9+11 = 32
seg_tree.update(3, 10)  # Update nums[3] = 10
print("Range Sum (2, 5) after update:", seg_tree.query(2, 5))  # Output: 5+10+9+11 = 35
