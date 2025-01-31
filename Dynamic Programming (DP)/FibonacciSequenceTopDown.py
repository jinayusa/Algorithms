# Fibonacci Sequence using Top-Down Approach (Memoization)

# Memoization stores results of subproblems to avoid redundant calculations.
# Time Complexity: O(n) (each Fibonacci value is computed once)
# Space Complexity: O(n) (for storing results in memo dictionary)

def fibonacci_memo(n, memo={}):
    """
    Function to compute Fibonacci sequence using Top-Down (Memoization).
    :param n: Fibonacci index (nth Fibonacci number)
    :param memo: Dictionary to store computed Fibonacci values
    :return: nth Fibonacci number
    """
    if n in memo:  # Check if already computed
        return memo[n]
    if n <= 1:  # Base case
        return n

    # Recursive computation with memoization
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Example Usage:
n = 10
print(f"Fibonacci({n}) using Memoization:", fibonacci_memo(n))

# Edge Cases Considered:
# 1. Fibonacci(0) -> Should return 0
# 2. Fibonacci(1) -> Should return 1
# 3. Large Fibonacci values (e.g., Fibonacci(50)) -> Should be computed efficiently
