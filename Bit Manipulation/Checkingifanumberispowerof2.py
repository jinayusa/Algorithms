# Checking if a number is a power of 2

def is_power_of_two_naive(n):
    """
    Naive approach: Keep dividing by 2 if n is even.
    If n reaches 1, it's a power of 2; otherwise, it's not.

    Time Complexity: O(log n) (dividing by 2 each step)
    Space Complexity: O(1)
    """
    if n <= 0:
        return False  # Negative numbers and 0 are not powers of 2

    while n % 2 == 0:  # Check if n is divisible by 2
        n //= 2  # Divide by 2

    return n == 1  # If we reach 1, it was a power of 2

def is_power_of_two_bitwise(n):
    """
    Optimal bitwise approach using n & (n - 1).
    A power of 2 has exactly one '1' in binary.

    Time Complexity: O(1) (Single bitwise operation)
    Space Complexity: O(1)
    """
    return n > 0 and (n & (n - 1)) == 0

# Example Usage
numbers = [1, 2, 3, 4, 8, 10, 16, 32, 64, 127, 128]

print("Using Naive Approach:")
for num in numbers:
    print(f"{num}: {is_power_of_two_naive(num)}")

print("\nUsing Bitwise Approach:")
for num in numbers:
    print(f"{num}: {is_power_of_two_bitwise(num)}")
