# Word Break Problem using Recursion (with Memoization) and Dynamic Programming

def word_break_recursive(s, wordDict, memo={}):
    """
    Recursive approach with memoization to check if the word can be broken.
    
    Time Complexity: O(N^2) (Worst case when checking multiple substrings)
    Space Complexity: O(N) (For memoization storage)
    """
    if s in memo:  # Return already computed results
        return memo[s]
    
    if s in wordDict:  # If the whole string is a word, return True
        return True

    for i in range(1, len(s)):  # Try different partitions
        prefix = s[:i]
        if prefix in wordDict and word_break_recursive(s[i:], wordDict, memo):
            memo[s] = True
            return True  # Found a valid segmentation
    
    memo[s] = False
    return False  # No valid segmentation found

def word_break_dp(s, wordDict):
    """
    Dynamic Programming approach to solve the word break problem.

    Time Complexity: O(N^2) (Checks all substrings)
    Space Complexity: O(N) (DP array stores results for each substring)
    """
    n = len(s)
    dp = [False] * (n + 1)  # dp[i] represents whether s[:i] can be segmented
    dp[0] = True  # Base case: an empty string is always segmentable

    for i in range(1, n + 1):  # Iterate through the entire string
        for j in range(i):  # Check possible partitions
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break  # Found a valid segmentation, no need to check further

    return dp[n]  # The final answer is whether the full string is segmentable

# Example Usage
s1 = "leetcode"
wordDict1 = {"leet", "code"}  # Using a set for O(1) lookups

s2 = "catsandog"
wordDict2 = {"cats", "dog", "sand", "and", "cat"}

# Using Recursion
print("Using Recursion with Memoization:", word_break_recursive(s1, wordDict1))  # Output: True
print("Using Recursion with Memoization:", word_break_recursive(s2, wordDict2))  # Output: False

# Using DP
print("Using Dynamic Programming:", word_break_dp(s1, wordDict1))  # Output: True
print("Using Dynamic Programming:", word_break_dp(s2, wordDict2))  # Output: False
