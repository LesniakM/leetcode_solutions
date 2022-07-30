"""
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
You are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.



Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

Result:
Runtime: 255 ms, faster than 60.52% of Python3 online submissions for Number of Good Ways to Split a String.
Memory Usage: 14.6 MB, less than 69.15% of Python3 online submissions for Number of Good Ways to Split a String.
"""
from collections import Counter


class Solution:
    @staticmethod
    def numSplits(s: str) -> int:
        goods = 0
        left = set()                # We don't really care about each char amount here, only if it was encountered.
        right = Counter(s)          # Here we care about amount of encounters.
        unique_chars = len(right)
        for char in s:
            left.add(char)
            right[char] -= 1
            if right[char] == 0:
                unique_chars -= 1
            if len(left) == unique_chars:
                goods += 1
        return goods


assert Solution.numSplits("aacaba") == 2
