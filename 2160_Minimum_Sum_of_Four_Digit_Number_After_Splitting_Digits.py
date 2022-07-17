"""
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

You are given a positive integer num consisting of exactly four digits.
Split num into two new integers new1 and new2 by using the digits found in num.
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3.
Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.


Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.

Result:
<Results are VERY inaccurate for this problem>
Runtime: 46 ms, faster than 50.33% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
Memory Usage: 13.8 MB, less than 56.27% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        return int(digits[0])*10 + int(digits[2]) + int(digits[1])*10 + int(digits[3])


solver = Solution()
assert solver.minimumSum(2932) == 52
