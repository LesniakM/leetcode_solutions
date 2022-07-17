"""
https://leetcode.com/problems/add-two-integers/

Given two integers num1 and num2, return the sum of the two integers.


Example 1:

Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

Result:
Runtime: 35 ms, faster than 84.3% of Python3 online submissions for Add Two Integers.
Memory Usage: 13.8 MB, less than 52.99% of Python3 online submissions for Add Two Integers.
"""


class Solution:
    @staticmethod
    def sum(num1: int, num2: int) -> int:
        return num1 + num2


solver = Solution()
assert solver.sum(23, 45) == 68
