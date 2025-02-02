# XOR Trick: Finding Missing Number & Single Number Problems

# Function to find the missing number in an array from 0 to n
def find_missing_number(arr):
    """
    This function finds the missing number from an array of size n containing numbers from 0 to n.
    
    Approach:
    - XOR all numbers from 0 to n.
    - XOR all elements of the given array.
    - The missing number is obtained by XORing the above two results.
    
    Time Complexity: O(n) (Single loop over array)
    Space Complexity: O(1) (Only a few integer variables are used)
    """
    n = len(arr)  # Since one number is missing, original range is n+1
    xor_all = 0  # XOR for numbers from 0 to n
    xor_arr = 0  # XOR for numbers in array

    # Compute XOR of all numbers from 0 to n
    for num in range(n + 1):
        xor_all ^= num

    # Compute XOR of all elements in the given array
    for num in arr:
        xor_arr ^= num

    # The missing number is the XOR of the above two results
    return xor_all ^ xor_arr

# Function to find the single number in an array where all other elements appear twice
def find_single_number(arr):
    """
    This function finds the single number from an array where every other element appears twice.

    Approach:
    - XOR all elements of the array.
    - Since a ⊕ a = 0, all duplicate numbers cancel each other out.
    - The remaining number is the single number.

    Time Complexity: O(n) (Single loop over array)
    Space Complexity: O(1) (Only a single integer variable is used)
    """
    result = 0
    for num in arr:
        result ^= num  # XOR all numbers

    return result  # The only number left is the single number

# Example Usage
arr_missing = [3, 0, 1]  # n=3, missing number should be 2
arr_single = [4, 1, 2, 1, 2]  # 4 appears once, everything else appears twice

print("Missing Number:", find_missing_number(arr_missing))  # Output: 2
print("Single Number:", find_single_number(arr_single))  # Output: 4
