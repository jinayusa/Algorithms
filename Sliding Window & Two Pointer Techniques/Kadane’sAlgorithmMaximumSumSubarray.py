# Maximum Sum Subarray using Kadane's Algorithm

def max_subarray_sum(nums):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Time Complexity: O(N) (Single pass through array)
    Space Complexity: O(1) (Only two variables used)
    """
    max_sum = float('-inf')  # Stores the maximum sum found
    current_sum = 0  # Tracks the running sum

    for num in nums:  # Iterate over array elements
        current_sum += num  # Add current element to running sum
        max_sum = max(max_sum, current_sum)  # Update maximum sum if needed

        if current_sum < 0:  # Reset if current sum drops below 0
            current_sum = 0

    return max_sum  # Return the largest sum found

# Example Usage
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [5, 4, -1, 7, 8]
nums3 = [-1, -2, -3, -4]

print("Max Subarray Sum (Example 1):", max_subarray_sum(nums1))  # Output: 6
print("Max Subarray Sum (Example 2):", max_subarray_sum(nums2))  # Output: 23
print("Max Subarray Sum (Example 3):", max_subarray_sum(nums3))  # Output: -1
