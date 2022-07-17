"""
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.


Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation:
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

Result:
<Results are very inaccurate for this problem>
Runtime: 46 ms, faster than 88.20% of Python3 online submissions for Maximum Number of Words Found in Sentences.
Memory Usage: 14 MB, less than 42.53% of Python3 online submissions for Maximum Number of Words Found in Sentences.
"""


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        spaces = [x.count(" ") for x in sentences]
        return max(spaces) + 1


solver = Solution()
assert solver.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]) == 6

