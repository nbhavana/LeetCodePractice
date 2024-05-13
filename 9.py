"""
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, 
it becomes 121-. 
Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""

# Solution

    
def isPalindrome1(x):
    str_x = str(x)

    if str_x == str_x[::-1]:
        return True
    else:
        return False
    

print(isPalindrome1(1211))


def isPalindrome2(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    rev_num = 0
    org_num = x
    while (x > 0):
        digit = x % 10
        rev_num = rev_num * 10 + digit
        x //= 10
    print(rev_num)
    print(x)
    return rev_num == org_num
        
    
print(isPalindrome2(121))