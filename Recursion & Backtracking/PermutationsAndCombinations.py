# Permutations & Combinations using Backtracking

from itertools import permutations, combinations

def generate_permutations(nums):
    """
    Generates all permutations of the given list.

    Time Complexity: O(N!) (Factorial growth)
    Space Complexity: O(N) (Recursion stack)
    """
    result = []

    def backtrack(path, remaining):
        if not remaining:  # Base case: all elements used
            result.append(path[:])  # Append a copy of the path
            return

        for i in range(len(remaining)):  # Explore all choices
            path.append(remaining[i])  # Choose an element
            backtrack(path, remaining[:i] + remaining[i+1:])  # Explore further
            path.pop()  # Undo the choice (backtrack)

    backtrack([], nums)
    return result

def generate_combinations(nums, r):
    """
    Generates all combinations of r elements from the given list.

    Time Complexity: O(2^N) (Subset exploration)
    Space Complexity: O(N) (Recursion stack)
    """
    result = []

    def backtrack(start, path):
        if len(path) == r:  # Base case: required length reached
            result.append(path[:])
            return
        
        for i in range(start, len(nums)):  # Explore choices without repetition
            path.append(nums[i])  # Choose element
            backtrack(i + 1, path)  # Move to next element
            path.pop()  # Undo choice (backtrack)

    backtrack(0, [])
    return result

# Example Usage
nums = [1, 2, 3]
r = 2

print("Permutations of [1,2,3]:", generate_permutations(nums))
print("Combinations of [1,2,3] choosing 2:", generate_combinations(nums, r))

# Using itertools for verification
print("itertools.permutations:", list(permutations(nums, r)))
print("itertools.combinations:", list(combinations(nums, r)))
