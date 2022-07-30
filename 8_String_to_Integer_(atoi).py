"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Results:

(myAtoi)
Runtime: 49 ms, faster than 66.96% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 29.14% of Python3 online submissions for String to Integer (atoi).

(myAtoi_using_int)
Runtime: 45 ms, faster than 76.03% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.8 MB, less than 79.50% of Python3 online submissions for String to Integer (atoi).
"""


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        min = -2**31
        max = 2**31 - 1
        striped = s.lstrip()
        if striped:
            first_non_space_char = striped[0]
            negative_number = False
            if first_non_space_char == "-":
                negative_number = True
                striped = striped[1:]
            elif first_non_space_char == "+":
                striped = striped[1:]
            digits = []
            for char in striped:
                code = ord(char)
                if 0 <= code-48 <= 9:
                    digits.append(code-48)
                else:
                    break

            output_int = sum(x*10**i for i, x in enumerate(reversed(digits)))
            if negative_number:
                output_int = -output_int
            if min <= output_int <= max:
                return output_int
            elif output_int < min:
                return min
            elif output_int > max:
                return max
        return 0

    @staticmethod
    def myAtoi_using_int(s: str) -> int:
        min = -2 ** 31
        max = 2 ** 31 - 1
        striped = s.lstrip()
        digits = ""
        sign = 1

        if not striped:
            return 0

        if striped[0] == "-":
            sign = -1
            striped = striped[1:]
        elif striped[0] == "+":
            striped = striped[1:]

        for char in striped:
            if char.isnumeric():
                digits += char
            else:
                break

        if digits.isnumeric():
            output_int = int(digits)*sign
        else:
            output_int = 0

        if min <= output_int <= max:
            return output_int
        elif output_int < min:
            return min
        elif output_int > max:
            return max


assert Solution.myAtoi("  -321124") == -321124
assert Solution.myAtoi("-91283472332") == -2147483648
assert Solution.myAtoi("-5-") == -5
assert Solution.myAtoi("-  ") == 0
