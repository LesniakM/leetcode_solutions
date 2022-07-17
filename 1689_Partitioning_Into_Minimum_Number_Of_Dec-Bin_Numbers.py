"""
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Result:
<Results are very inaccurate for this problem>
Runtime: 95 ms, faster than 72.91% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 14.8 MB, less than 44.81% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


solver = Solution()

assert solver.minPartitions("32") == 3
assert solver.minPartitions("82734") == 8
assert solver.minPartitions("27346209830709182346") == 9
