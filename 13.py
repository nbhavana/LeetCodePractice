
"""
13. Roman to Integer

Roman numerals are represented by seven
 different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written 
as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number 
four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine,
 which is written as IX. There are six instances 
 where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]."""


# Solution 1
def romanToInt1(s):
    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                         'C': 100, 'D': 500, 'M': 1000}
    total_int = 0
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')

    for char in s:
        total_int += roman_to_int_dict[char]
    return total_int


print(romanToInt1('MCMXCIV'))


def romanToInt2(s):
    # Dictionary to map Roman numerals to their integer values
    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                         'C': 100, 'D': 500, 'M': 1000}

    # Initialize total to store the integer equivalent of the Roman numeral
    total = 0

    # Initialize prev_value to keep track of the value of 
    # the previous Roman numeral
    prev_value = 0

    # Iterate through each character in the Roman numeral
    for char in s:
        # Get the integer value of the current Roman numeral character
        value = roman_to_int_dict[char]

        # If the value of the current Roman numeral is
        # greater than the previous one,
        # it means it's a subtractive pair, so subtract
        # twice the previous value
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            # Otherwise, add the current value to the total
            total += value

        # Update prev_value for the next iteration
        prev_value = value

    # Return the total integer value of the Roman numeral
    return total
    

print(romanToInt2('MCMXCIV'))
