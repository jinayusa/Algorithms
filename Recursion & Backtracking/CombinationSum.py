# Combination Sum using Backtracking

def combination_sum(candidates, target):
    """
    Finds all unique combinations in candidates[] where the numbers sum up to the target.

    Time Complexity: O(2^N) (Exponential, as we explore all subsets)
    Space Complexity: O(N) (Recursion depth)
    """

    result = []  # To store the valid combinations

    def backtrack(start, target, path):
        """
        Backtracking function to explore all possible combinations.
        """
        # Base Case: If target becomes zero, add valid combination
        if target == 0:
            result.append(list(path))  # Append a copy of path
            return
        
        for i in range(start, len(candidates)):  # Iterate over candidates
            if candidates[i] > target:
                continue  # Prune paths where sum exceeds target

            path.append(candidates[i])  # Choose the number
            backtrack(i, target - candidates[i], path)  # Explore with same element
            path.pop()  # Undo the choice (backtrack)

    backtrack(0, target, [])  # Start recursion

    return result

# Example Usage
candidates1 = [2, 3, 6, 7]
target1 = 7

candidates2 = [2, 3, 5]
target2 = 8

print("Combinations for [2, 3, 6, 7], Target = 7:", combination_sum(candidates1, target1))
print("Combinations for [2, 3, 5], Target = 8:", combination_sum(candidates2, target2))
