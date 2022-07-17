"""
https://leetcode.com/problems/running-sum-of-1d-array/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Result:
Runtime: 43 ms, faster than 89.83% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.1 MB, less than 71.01% of Python3 online submissions for Running Sum of 1d Array.
"""
from timeit import timeit


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        out = [nums[0]]
        for i in range(len(nums)-1):
            out.append(out[i] + nums[i+1])
        return out


solver = Solution()
assert solver.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10], "1st"
assert solver.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5], "2nd"
assert solver.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17], "3rd"

print(timeit(lambda: solver.runningSum([3, 1, 2, 10, 1]), number=1000000))
