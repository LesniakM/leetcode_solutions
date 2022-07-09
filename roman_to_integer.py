"""
https://leetcode.com/problems/roman-to-integer/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Result:
Runtime: 51 ms, faster than 90.08% of Python3 online submissions for Roman to Integer.
Memory Usage: 14 MB, less than 30.70% of Python3 online submissions for Roman to Integer.
"""

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
          "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}


class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        index, value = 0, 0
        keys = VALUES.keys()
        str_len = len(s)
        while index < str_len:
            char = s[index]
            if index == str_len - 1:
                value = value + VALUES[char]
            else:
                pair = char + s[index+1]
                if pair in keys:
                    value = value + VALUES[pair]
                    index = index + 1
                else:
                    value = value + VALUES[char]
            index = index + 1
        return value


solver = Solution()
assert solver.romanToInt("IXCD") == 409
