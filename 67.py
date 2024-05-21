"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

# Solution:

def addBinary(a, b):
    result = []  # Initialize an empty list to store the result
    carry = 0    # Initialize a variable to store the carry
    i, j = len(a) - 1, len(b) - 1  # Initialize pointers to the rightmost digits of both strings
    
    # Iterate through both strings from right to left
    while i >= 0 or j >= 0 or carry:
        total = carry  # Initialize total as the carry from the previous iteration
        
        # Add the corresponding digits from both strings if they exist
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        
        # Append the least significant bit of the total to the result
        result.append(str(total % 2))
        
        # Update the carry for the next iteration
        carry = total // 2
    
    # Return the result as a binary string by joining the list and reversing it
    return ''.join(result[::-1])

# Example usage:
a = "1010"
b = "1011"
print(addBinary(a, b))  # Output: "10101"