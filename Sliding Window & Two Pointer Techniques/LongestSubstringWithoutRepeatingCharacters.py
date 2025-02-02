# Longest Substring Without Repeating Characters using Sliding Window

def longest_unique_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Time Complexity: O(N) (Each character is processed at most twice)
    Space Complexity: O(N) (Set stores characters)
    """
    char_set = set()  # Stores unique characters in the current window
    left = 0  # Left pointer for sliding window
    max_length = 0  # Stores the longest unique substring length

    for right in range(len(s)):  # Expand window using right pointer
        while s[right] in char_set:  # If duplicate found, shrink window
            char_set.remove(s[left])  # Remove leftmost character
            left += 1  # Move left pointer forward

        char_set.add(s[right])  # Add new character to window
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length  # Return longest unique substring length

# Example Usage
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print("Longest Unique Substring (Example 1):", longest_unique_substring(s1))  # Output: 3
print("Longest Unique Substring (Example 2):", longest_unique_substring(s2))  # Output: 1
print("Longest Unique Substring (Example 3):", longest_unique_substring(s3))  # Output: 3
