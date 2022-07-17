"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the
number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Result:
<Results are very inaccurate for this problem>
Runtime: 52 ms, faster than 70.17% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.8 MB, less than 62.91% of Python3 online submissions for Kids With the Greatest Number of Candies.
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [kid + extraCandies >= max_candies for kid in candies]


solver = Solution()
assert solver.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
