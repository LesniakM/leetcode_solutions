"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# Memory efficient solution:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        maxi = max(nums)
        mini = min(nums)
        for index in range(length):
            number = nums[index]
            if number + mini > target or number + maxi < target:
                continue
            for i in range(length-1-index):
                if number + nums[i+1+index] == target:
                    return [index, i+1+index]


solver = Solution()
assert solver.twoSum([3, 2, 4], target=6) == [1, 2]
