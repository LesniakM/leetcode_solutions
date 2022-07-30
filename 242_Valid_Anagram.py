"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Result:
Time complexity: O(n)
Runtime: 46 ms, faster than 95.22% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 96.92% of Python3 online submissions for Valid Anagram.
"""
from collections import Counter
import matplotlib.pyplot as plt
from random import randint
from timeit import timeit


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        s_chars = Counter(s)
        t_chars = Counter(t)
        return s_chars == t_chars


s1 = "anagram"
t1 = "nagaram"

assert Solution.isAnagram(s1, t1) is True


# Runtime complexity check
alpha = 'abcdefghijklmnopqrstuvwxyz'

test_cases = 40
test_lists = []
min_len = 10
max_len = 10**6

for x in range(test_cases):
    length = int(min_len + x*max_len/test_cases)
    string = "".join([alpha[randint(0, 25)] for x in range(length)])
    test_lists.append((string, string[::-1]))
print("Lists generated.", len(test_lists[0][0]), len(test_lists[-1][0]))

x, y = [], []
number_of_tests = len(test_lists)
for index, test_list in enumerate(test_lists):
    x.append(len(test_list[0]))
    y.append(timeit(lambda: Solution.isAnagram(test_list[0], test_list[1]), number=100))
    print(f"Done {index * 100 / number_of_tests} %")

plt.plot(x, y)
plt.show()
