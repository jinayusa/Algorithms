# Counting Set Bits in an Integer

def count_set_bits_naive(n):
    """
    Naive approach: Convert number to binary and count '1's.
    Time Complexity: O(k), where k is the number of bits in n.
    Space Complexity: O(k) due to string storage.
    """
    return bin(n).count('1')  # Convert to binary string and count '1's

def count_set_bits_bitwise(n):
    """
    Bitwise AND & Right Shift method.
    Time Complexity: O(k), Space Complexity: O(1).
    """
    count = 0
    while n > 0:
        count += n & 1  # Check last bit
        n >>= 1  # Shift right by 1
    return count

def count_set_bits_brian_kernighan(n):
    """
    Brian Kernighan's Algorithm: Directly removes set bits.
    Time Complexity: O(number of set bits).
    Space Complexity: O(1).
    """
    count = 0
    while n:
        n &= (n - 1)  # Removes the rightmost set bit
        count += 1
    return count

# Example Usage
num = 29  # Binary: 11101, Set Bits: 4

print("Naive Approach:", count_set_bits_naive(num))  # Output: 4
print("Bitwise Shift Approach:", count_set_bits_bitwise(num))  # Output: 4
print("Brian Kernighan's Approach:", count_set_bits_brian_kernighan(num))  # Output: 4
