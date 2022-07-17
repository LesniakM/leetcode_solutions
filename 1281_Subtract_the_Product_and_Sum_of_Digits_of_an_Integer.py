"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Result:
<Results are very inaccurate for this problem>
Runtime: 28 ms, faster than 96.73% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 13.8 MB, less than 52.55% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        prod = 1
        for digit in digits:
            prod = prod * digit
        return prod - sum(digits)


solver = Solution()
assert solver.subtractProductAndSum(234) == 15

