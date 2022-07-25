"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Result:
Runtime: 92 ms, faster than 89.01% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 93.21% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target in nums:
            return [nums.index(target), (len(nums)-1-nums[::-1].index(target))]
        return [-1, -1]
