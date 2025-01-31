# Fibonacci Sequence using Bottom-Up Approach (Tabulation)

# Tabulation computes Fibonacci iteratively from the base cases.
# Time Complexity: O(n) (each Fibonacci value is computed once)
# Space Complexity: O(1) (stores only two variables)

def fibonacci_tabulation(n):
    """
    Function to compute Fibonacci sequence using Bottom-Up (Tabulation).
    :param n: Fibonacci index (nth Fibonacci number)
    :return: nth Fibonacci number
    """
    if n <= 1:  # Base case
        return n

    prev2, prev1 = 0, 1  # F(0) = 0, F(1) = 1
    for _ in range(2, n + 1):  # Compute iteratively
        current = prev1 + prev2
        prev2, prev1 = prev1, current  # Update previous values

    return prev1


# Example Usage:
n = 10
print(f"Fibonacci({n}) using Tabulation:", fibonacci_tabulation(n))

# Edge Cases Considered:
# 1. Fibonacci(0) -> Should return 0
# 2. Fibonacci(1) -> Should return 1
# 3. Large Fibonacci values (e.g., Fibonacci(50)) -> Should be computed efficiently
