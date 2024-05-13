"""
14. Longest Common Prefix

Write a function to find the longest common prefix 
string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    # find the smallest string in the list
    strs.sort(key=len)
    smallest_common_prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(smallest_common_prefix) != 0:
            smallest_common_prefix = smallest_common_prefix[0:len(smallest_common_prefix)-1]
            if smallest_common_prefix == "":
                return ""
    return smallest_common_prefix


print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["flower","flow","flight"]))
