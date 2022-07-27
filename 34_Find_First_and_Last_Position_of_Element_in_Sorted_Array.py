"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Result:
Runtime: 88 ms, faster than 94.07% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 93.21% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""
from timeit import timeit
import matplotlib.pyplot as plt
from random import randint
import numpy as np


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]

        list_length = len(nums)
        sub_length = list_length // 2
        check_point_index = sub_length  # start in the middle
        starting = -1
        ending = -1
        visited_indexes = []

        while starting == -1 and ending == -1:
            check_value = nums[check_point_index]
            change = max(1, round(sub_length / 2))

            if target > check_value:
                check_point_index = check_point_index + change
            elif target < check_value:
                check_point_index = check_point_index - change
            elif target == check_value:
                starting = check_point_index
                ending = check_point_index
            sub_length = round(sub_length / 2)

            # Oscillation prevention
            if check_point_index in visited_indexes and check_value != target:
                return [-1, -1]
            else:
                visited_indexes.append(check_point_index)

        if starting > 0:
            while nums[starting - 1] == target and starting > 0:
                starting -= 1
        if ending < list_length - 1:
            while nums[ending + 1] == target:
                ending += 1
                if ending == list_length - 1:
                    break
        return [starting, ending]


# Test area
solver = Solution()

assert solver.searchRange([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5], 0) == [0, 1]
assert solver.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert solver.searchRange([1, 2, 3], 3) == [2, 2]
assert solver.searchRange([0, 0, 2, 3, 4, 4, 4, 5], 5) == [7, 7]
assert solver.searchRange([0, 1, 2, 3, 4, 4, 4], 2) == [2, 2]
assert solver.searchRange([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 9, 9, 10], 7) == [15, 15]


# O(log n) runtime complexity validation below.
# Let's make 1000 lists with lengths from 1 to ~10000 and vals within +/- 10^9
min_val = -10 ** 9
max_val = 10 ** 9
test_lists = []
for x in range(1000):
    start = randint(min_val, max_val * 0.9)
    end = randint(start, max_val)
    step = (end - start) // (100*(x+1))
    new_list = np.arange(start, end, step)
    new_list = list(new_list)
    test_lists.append(new_list)

test_lists = sorted(test_lists, key=len)
print("Lists generated.")

x, y = [], []
number_of_tests = len(test_lists)
for index, test_list in enumerate(test_lists):
    target = test_list[randint(0, len(test_list) - 1)]
    x.append(len(test_list))
    y.append(timeit(lambda: solver.searchRange(test_list, target), number=1000))
    print(f"Done {index * 100 / number_of_tests} %")

plt.plot(x, y)
plt.show()
