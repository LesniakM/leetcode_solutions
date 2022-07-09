"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Result:
Runtime: 99 ms, faster than 60.76% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 95.39% of Python3 online submissions for Two Sum.
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
