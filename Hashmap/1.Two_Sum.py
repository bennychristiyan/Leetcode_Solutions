#Problem
"""Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target. You may assume 
that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

# 1.Using Hashmap(dictionary) to find the difference of the target and the element in the list in each iteration. If the difference is in the 
# dictionary, return the index of the current element and the index(value) of the difference element(key) in the dictionary; else store the 
# element as the key and the index as the value in the dictionary

# Time complexity = O(n). Runtime = 41ms
class Solution:
    def twoSum(self, nums, target):
        dic = {} #element(key) : index(value)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            dic[n] = i
        return

# 2.Using 2 for loops to iterate through the list and check if the sum is equal to the target and are not same indices. If it is, return the 
# indices of the 2 numbers.

# Time complexity = O(n^2). Runtime = 3755ms
class Solution:
    def twoSum(self, nums, target):
        for i_x, x in enumerate(nums):
            for i_y, y in enumerate(nums):
                if (i_x != i_y) and (x + y == target):
                    return [i_x, i_y]