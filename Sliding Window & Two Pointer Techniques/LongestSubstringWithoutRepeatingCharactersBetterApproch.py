def longest_unique_substring_optimized(s):
    char_map = {}  # Stores character indices
    left = 0  # Left pointer
    max_length = 0  # Stores max length

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)  # Move left pointer

        char_map[s[right]] = right  # Update character position
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length