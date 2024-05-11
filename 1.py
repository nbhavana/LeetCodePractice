"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.You may assume that each input 
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""

# Solution-1 (Brute force)


def twoSum1(nums, target):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if num1 + num2 == target and i != j:
                return [i, j]
          

# Solution-1 using dictionary


def twoSum2(nums, target):
    # Create a dictionary to store the indices of numbers
    num_indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        print(complement)
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # If found, return the indices of the current number and its 
            # complement
            return [num_indices[complement], i]
        
        # If not found, store the index of the current number in the dictionary
        num_indices[num] = i
        print(num_indices)
    
    # If no solution is found, return an empty list
    return []


print("Solution1:")
print(twoSum1([1, 2, 3, 4], 7))
print("Solution2:")
print(twoSum2([1, 2, 3, 4], 7))