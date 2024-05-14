"""20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s) :
        stack = []
        b_mapping = {'(': ')', '[': ']', '{': '}'}
        
        for bracket in s:
            
            if bracket in b_mapping:
                # If there is an opening bracket , add it to the stack.
                stack.append(bracket)
            # If there is a closing bracket , check it  against the corresponding opening bracket at the top of the stack
            # if they match, the opening bracket is removed from the stack
            # if they don't match or the stack is empty, the string in invalid
            elif  len(stack) == 0 or b_mapping[stack.pop()] != bracket:
                return False
            
        return len(stack) == 0
                
            
        
print( isValid("()[]{}}") )
print( isValid("()]{}})") )
print( isValid("()") )
print( isValid("(])"))