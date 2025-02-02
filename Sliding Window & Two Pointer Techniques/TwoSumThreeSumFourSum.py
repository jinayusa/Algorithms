# Optimal Solutions for Two Sum, Three Sum, and Four Sum

def two_sum(nums, target):
    """
    Finds two numbers that add up to the target using a hashmap.

    Time Complexity: O(N) (Single pass)
    Space Complexity: O(N) (Hashmap storage)
    """
    num_map = {}  # Stores number and its index
    for i, num in enumerate(nums):
        complement = target - num  # Find the complement
        if complement in num_map:  # If found, return indices
            return [num_map[complement], i]
        num_map[num] = i  # Store current number with its index
    return []  # No solution found

def three_sum(nums):
    """
    Finds all unique triplets that sum up to zero using sorting + two pointers.

    Time Complexity: O(N²) (Sorting + Two Pointers)
    Space Complexity: O(1) (No extra space used)
    """
    nums.sort()  # Sort the array
    result = []
    n = len(nums)
    
    for i in range(n - 2):  # Fix one element and use two pointers
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:  # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                    right -= 1
            elif total < 0:  # Move left pointer to increase sum
                left += 1
            else:  # Move right pointer to decrease sum
                right -= 1

    return result

def four_sum(nums, target):
    """
    Finds all unique quadruplets that sum up to target using sorting + two pointers.

    Time Complexity: O(N³) (Sorting + Two Pointers)
    Space Complexity: O(1) (No extra space used)
    """
    nums.sort()  # Sort the array
    result = []
    n = len(nums)
    
    for i in range(n - 3):  # First element
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue
        for j in range(i + 1, n - 2):  # Second element
            if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                        right -= 1
                elif total < target:
                    left += 1  # Move left pointer to increase sum
                else:
                    right -= 1  # Move right pointer to decrease sum

    return result

# Example Usage
nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [-1, 0, 1, 2, -1, -4]
nums3 = [1, 0, -1, 0, -2, 2]
target3 = 0

print("Two Sum:", two_sum(nums1, target1))  # Output: [0, 1]
print("Three Sum:", three_sum(nums2))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print("Four Sum:", four_sum(nums3, target3))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
