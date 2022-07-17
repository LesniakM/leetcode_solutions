"""
https://leetcode.com/problems/jewels-and-stones/
You're given strings jewels representing the types of stones that are jewels, and stones representing
the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Result:
<Results are very inaccurate for this problem>
Runtime: 37 ms, faster than 80.49% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 58.42% of Python3 online submissions for Jewels and Stones.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for jewel in jewels:
            output += stones.count(jewel)
        return output


solver = Solution()
assert solver.numJewelsInStones("aA", "aAAbbbb") == 3
