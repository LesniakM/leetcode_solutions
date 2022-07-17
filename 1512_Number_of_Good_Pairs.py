"""
https://leetcode.com/problems/number-of-good-pairs/
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Result:
<Results are VERY inaccurate for this problem>
Runtime: 33 ms, faster than 95.07% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.8 MB, less than 95.66% of Python3 online submissions for Number of Good Pairs.
"""


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = 0
        for index, num in enumerate(nums):
            for i in range(len(nums)-index-1):
                if num == nums[i+index+1]:
                    counter += 1
        return counter


solver = Solution()
assert solver.numIdenticalPairs([1, 2, 3]) == 0
assert solver.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
