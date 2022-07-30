"""
https://leetcode.com/problems/number-of-lines-to-write-string/
You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.


Example 1:

Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.

Result:
Runtime: 47 ms, faster than 61.19% of Python3 online submissions for Number of Lines To Write String.
Memory Usage: 13.9 MB, less than 66.60% of Python3 online submissions for Number of Lines To Write String.
"""


class Solution:
    @staticmethod
    def numberOfLines(widths: list[int], s: str) -> list[int]:
        row_counter = 1
        width_counter = 0
        for char in s:
            width = widths[ord(char)-97]
            if width_counter + width <= 100:
                width_counter += width
            else:
                row_counter += 1
                width_counter = width
        return [row_counter, width_counter]


widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
s = "abcdefghijklmnopqrstuvwxyz"

assert Solution.numberOfLines(widths, s) == [3, 60]
