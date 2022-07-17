"""
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.


Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.

Result:
<Results are very inaccurate for this problem>
Runtime: 64 ms, faster than 75.50% of Python3 online submissions for Final Value of Variable After Performing Operations.
Memory Usage: 13.8 MB, less than 54.80% of Python3 online submissions for Final Value of Variable After Performing Operations.
"""


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        output = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                output -= 1
            else:
                output += 1
        return output


solver = Solution()
assert solver.finalValueAfterOperations(["--X", "X++", "X++"]) == 1, "1st"
assert solver.finalValueAfterOperations(["++X", "++X", "X++"]) == 3, "2nd"
assert solver.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0, "3rd"
