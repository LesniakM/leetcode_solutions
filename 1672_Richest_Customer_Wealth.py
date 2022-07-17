"""
https://leetcode.com/problems/richest-customer-wealth/
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.


Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Result:
<Results are very inaccurate for this problem>
Runtime: 67 ms, faster than 74.54% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14 MB, less than 32.13% of Python3 online submissions for Richest Customer Wealth.
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sums = [sum(x) for x in accounts]
        return max(sums)


solver = Solution()
assert solver.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
assert solver.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
