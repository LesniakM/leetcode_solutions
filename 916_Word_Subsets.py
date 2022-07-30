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

Result:
Runtime: 755 ms, faster than 91.00% of Python3 online submissions for Word Subsets.
Memory Usage: 18.6 MB, less than 54.67% of Python3 online submissions for Word Subsets.
"""
from collections import Counter


class Solution:
    @staticmethod
    def wordSubsets(words: list[str], subs: list[str]) -> list[str]:
        # Minimize all the substrings to only one counter, which is max of all subs.
        universal_substring_counter = Counter()
        for substring in subs:
            substring_counter = Counter(substring)
            universal_substring_counter |= substring_counter

        out = []
        for word in words:
            word_is_ok = True
            for char in universal_substring_counter:
                if universal_substring_counter[char] > word.count(char):
                    word_is_ok = False
                    break
            if word_is_ok:
                out.append(word)
        return out


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["amazon", "apple", "facebook", "google", "leetcode"]
subs2 = ["lo", "eo"]
words3 = ["amazon", "apple", "facebook", "google", "leetcode"]
subs3 = ["oo", "gle", "g", "gg", "e"]
assert Solution.wordSubsets(words1, ["e", "o"]) == ["facebook", "google", "leetcode"]
assert Solution.wordSubsets(words2, subs2) == ["google", "leetcode"]
assert Solution.wordSubsets(words3, subs3) == ["google"]
