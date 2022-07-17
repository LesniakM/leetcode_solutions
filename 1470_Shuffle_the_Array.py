"""
https://leetcode.com/problems/shuffle-the-array/
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Result:
<Results are very inaccurate for this problem>
Runtime: 69 ms, faster than 83.05% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.1 MB, less than 90.06% of Python3 online submissions for Shuffle the Array.
"""
from timeit import timeit


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[i+n])
        return output

    # Could be done in one line:
    # but it turns out, that it is better to use for/append.
    def shuffle2(self, nums: list[int], n: int) -> list[int]:
        return [nums[x // 2 + n * (x % 2)] for x in range(2 * n)]


solver = Solution()
assert solver.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
assert solver.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
assert solver.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]

print(timeit(lambda: solver.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4), number=1000000))
print(timeit(lambda: solver.shuffle2([1, 2, 3, 4, 4, 3, 2, 1], 4), number=1000000))
