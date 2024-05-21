"""
35. Search Insert Position
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
"""

# Solution :(using Binary search tree)


def searchInsert(nums, target):
    # Initialize the left and right pointers
    left, right = 0, len(nums) - 1
    
    # Binary search algorithm
    while left <= right:
        # Calculate the index of the middle element
        mid = (left + right) // 2
        
        # If the middle element is the target, return its index
        if nums[mid] == target:
            return mid
        # If the middle element is less than the target,
        # update the left pointer to search in the right half
        elif nums[mid] < target:
            left = mid + 1
        # If the middle element is greater than the target,
        # update the right pointer to search in the left half
        else:
            right = mid - 1
            
    # If the loop exits without finding the target,
    # return the left pointer as the index where the target should be inserted
    return left

print(searchInsert([2,3,4,5,6,7,9],8))
print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))