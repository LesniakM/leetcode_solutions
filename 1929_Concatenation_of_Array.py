"""
https://leetcode.com/problems/concatenation-of-array/
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.



Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Result:
<For this problem, runtime is very inaccurate.>
Runtime: 108 ms, faster than 71.83% of Python3 online submissions for Concatenation of Array.
Memory Usage: 14.3 MB, less than 23.32% of Python3 online submissions for Concatenation of Array.
"""
from timeit import timeit


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums


solver = Solution()
assert solver.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert solver.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]

print(timeit(lambda: solver.getConcatenation([0, 2, 1, 5, 3, 4]), number=1000000))
