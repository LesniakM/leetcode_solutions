"""
https://leetcode.com/problems/matchsticks-to-square/
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.


Example 1:

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.


Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
"""


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4:
            return False

        sides = [0, 0, 0, 0]
        ascending_sticks = sorted(matchsticks)[::-1]
        for stick in ascending_sticks:
            sides[self.get_min_side_index(sides)] = sides[self.get_min_side_index(sides)] + stick
        if sides[0] == sides[1] == sides[2] == sides[3]:
            return True

        sides = [0, 0, 0, 0]
        side_length = total_length//4
        print(ascending_sticks)
        for i in range(4):
            side = ascending_sticks.pop(0)
            if side_length - side in ascending_sticks:
                side = side + ascending_sticks.pop(ascending_sticks.index(side_length - side))
                sides[i] = side
            else:
                pass

        # Let's try harder then
        return False

    @staticmethod
    def get_min_side_index(input_list):
        min_value = min(input_list)
        min_index = input_list.index(min_value)
        return min_index


matchsticks1 = [1, 1, 2, 2, 2]
matchsticks2 = [3, 3, 3, 3, 4]
matchsticks3 = [3, 3, 3, 4]
matchsticks4 = [10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]

solver = Solution()
assert solver.makesquare(matchsticks1) is True
assert solver.makesquare(matchsticks2) is False
assert solver.makesquare(matchsticks3) is False
assert solver.makesquare(matchsticks4) is True
