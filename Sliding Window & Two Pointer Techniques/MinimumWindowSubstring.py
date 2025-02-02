from collections import Counter

def min_window_substring(s, t):
    """
    Finds the minimum window substring in `s` that contains all characters of `t`.

    Time Complexity: O(N) (Each character is processed at most twice)
    Space Complexity: O(1) (Fixed size of 128 for ASCII characters)
    """
    if not s or not t:
        return ""

    # Dictionary to store character frequency of t
    t_count = Counter(t)
    
    # Dictionary to track current window's character frequency
    window_count = {}
    
    left, right = 0, 0  # Sliding window pointers
    min_length = float("inf")  # Store the minimum window length
    min_window = ""  # Store the minimum window substring
    required = len(t_count)  # Unique characters required
    formed = 0  # Unique characters matched
    
    while right < len(s):
        # Add character at right pointer to window
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if it satisfies frequency in t
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Contract the window from the left while it's valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update the minimum window substring
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]
            
            # Remove left character and move left pointer
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1  # One unique character is no longer fully matched

            left += 1  # Move left pointer

        # Expand window by moving right pointer
        right += 1

    return min_window

# Example Usage
s1, t1 = "ADOBECODEBANC", "ABC"
s2, t2 = "a", "a"
s3, t3 = "a", "aa"

print("Minimum Window Substring (Example 1):", min_window_substring(s1, t1))  # Output: "BANC"
print("Minimum Window Substring (Example 2):", min_window_substring(s2, t2))  # Output: "a"
print("Minimum Window Substring (Example 3):", min_window_substring(s3, t3))  # Output: ""
