"""
https://leetcode.com/problems/stone-game/
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.



Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
"""


class Solution:
    @staticmethod
    def stoneGame(piles: list[int]) -> bool:
        alice = 0
        bob = 0
        for _ in range(len(piles) // 2):
            if piles[0] > piles[-1]:
                alice += piles.pop(0)
            elif piles[0] < piles[-1]:
                alice += piles.pop(-1)
            else:
                if piles[1] >= piles[-2]:
                    alice += piles.pop(-1)
                elif piles[1] < piles[-2]:
                    alice += piles.pop(0)

            if piles[0] > piles[-1]:
                bob += piles.pop(0)
            elif piles[0] < piles[-1]:
                bob += piles.pop(-1)
            elif len(piles) == 1:
                bob += piles[0]
            else:
                if piles[1] >= piles[-2]:
                    bob += piles.pop(-1)
                elif piles[1] < piles[-2]:
                    bob += piles.pop(0)
            print(alice, bob)
        print()
        return alice > bob


piles1 = [5, 3, 4, 5]
piles2 = [3, 7, 2, 3]
piles3 = [1, 7, 3, 1, 7, 2]
piles4 = [3, 2, 10, 4]
assert Solution.stoneGame(piles1) is True
assert Solution.stoneGame(piles2) is True
assert Solution.stoneGame(piles3) is False
assert Solution.stoneGame(piles4) is True
