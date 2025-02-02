def min_window_substring_optimized(s, t):
    if not s or not t:
        return ""
    
    t_count = [0] * 128
    window_count = [0] * 128
    
    for char in t:
        t_count[ord(char)] += 1
    
    left, right, min_length, min_window = 0, 0, float('inf'), ""
    required, formed = len(set(t)), 0
    
    while right < len(s):
        char = s[right]
        window_count[ord(char)] += 1
        
        if t_count[ord(char)] and window_count[ord(char)] == t_count[ord(char)]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]
            
            window_count[ord(char)] -= 1
            if t_count[ord(char)] and window_count[ord(char)] < t_count[ord(char)]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return min_window
