# Trapping Rain Water using Two Pointers

def trap_rain_water(heights):
    """
    Calculates the total trapped rainwater between buildings.

    Time Complexity: O(N) (Single pass using two pointers)
    Space Complexity: O(1) (Constant space used)
    """
    if not heights or len(heights) < 3:
        return 0  # Not enough bars to trap water

    left, right = 0, len(heights) - 1  # Two pointers
    left_max, right_max = heights[left], heights[right]  # Track max heights
    water_trapped = 0  # Total trapped water

    while left < right:
        if left_max < right_max:
            left += 1  # Move left pointer
            left_max = max(left_max, heights[left])  # Update left max
            water_trapped += max(0, left_max - heights[left])  # Add trapped water
        else:
            right -= 1  # Move right pointer
            right_max = max(right_max, heights[right])  # Update right max
            water_trapped += max(0, right_max - heights[right])  # Add trapped water

    return water_trapped  # Return total trapped water

# Example Usage
heights1 = [0,1,0,2,1,0,1,3,2,1,2,1]
heights2 = [4,2,0,3,2,5]
heights3 = [1,1,1,1]

print("Trapped Rain Water (Example 1):", trap_rain_water(heights1))  # Output: 6
print("Trapped Rain Water (Example 2):", trap_rain_water(heights2))  # Output: 9
print("Trapped Rain Water (Example 3):", trap_rain_water(heights3))  # Output: 0
