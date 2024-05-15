"""

28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
"""

#Solution 1

def strStr1(haystack, needle):
# Run a loop i from 0 to length of the string in haystack
    # If needle is empty, return 0
    if not needle:
        return 0
    for i in range(0,len(haystack)):
        # Run the second loop from j to length of the string in needle
        for j in range(i,len(haystack)):
            # Slice the string using haystack[i:j+1]
            # print(haystack[i:j+1])
            # if the string are equal return i
            if (haystack[i:j+1] == needle):
                return i
    return -1
                
            
print(strStr1("sadbutsad", "sad"))
print(strStr1("leetcode", "leeto"))


#Solution 2
def strStr2(haystack, needle):
    # If needle is empty, return 0
    if not needle:
        return 0
    
    # Iterate through haystack
    for i in range(len(haystack)):
        # If the current character matches the first character of needle
        if haystack[i] == needle[0]:
            # Check if the substring starting from i matches needle
            if haystack[i:i+len(needle)] == needle:
                return i
    
    # If needle is not found in haystack, return -1
    return -1

print(strStr2("sadbutsad", "sad"))
print(strStr2("leetcode", "leeto"))