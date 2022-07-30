"""
https://leetcode.com/problems/largest-number/
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Result:
Runtime: 132 ms, faster than 9.07% of Python3 online submissions for Largest Number.
Memory Usage: 13.9 MB, less than 21.36% of Python3 online submissions for Largest Number.
"""


class Solution:
    @staticmethod
    def largestNumber(nums: list[int]) -> str:
        nums = Solution.bruteforce_bubble_sort(nums)
        out = "".join(str(x) for x in nums)
        if out[0] == "0":
            return str(int(out))
        return out

    @staticmethod
    def bruteforce_bubble_sort(nums: list[int]) -> list[int]:
        input_len = len(nums)
        swapped = True
        for i in range(input_len - 1):
            if not swapped:
                break
            swapped = False
            for j in range(input_len - i - 1):
                mid1 = str(nums[j]) + str(nums[j+1])
                mid2 = str(nums[j+1]) + str(nums[j])
                if int(mid1) < int(mid2):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
        return nums


assert Solution.largestNumber([3, 30, 34, 5, 9]) == "9534330"
assert Solution.largestNumber([9, 5, 34, 30, 3]) == "9534330"
assert Solution.largestNumber([34323, 3432]) == "343234323" # 343234323
                                            #   "343233432"   343233432