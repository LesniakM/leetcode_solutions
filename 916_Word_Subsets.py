"""
https://leetcode.com/problems/word-subsets/

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.



Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
"""


class Solution:
    @staticmethod
    def wordSubsets(words1: list[str], subs: list[str]) -> list[str]:
        out = []
        for word in words1:
            yep = True
            for substring in subs:
                if substring not in word:
                    yep = False
            if yep:
                out.append(word)
        return out


words = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["amazon", "apple", "facebook", "google", "leetcode"]
subs2 = ["lo", "eo"]
assert Solution.wordSubsets(words, ["e", "o"]) == ["facebook", "google", "leetcode"]
assert Solution.wordSubsets(words2, subs2) == ["google", "leetcode"]
