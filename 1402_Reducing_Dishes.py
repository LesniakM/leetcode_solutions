"""
https://leetcode.com/problems/reducing-dishes/
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied
by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.


Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish,
the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

Result:
Runtime: 54 ms, faster than 80.54% of Python3 online submissions for Reducing Dishes.
Memory Usage: 13.9 MB, less than 86.61% of Python3 online submissions for Reducing Dishes.
"""


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1] < 0:
            return 0

        max_score = -99999999999
        dishes = len(satisfaction)
        score_is_ascending = True

        for attempt in range(dishes):
            if score_is_ascending:
                score = 0
                current_satisfaction = 1
                for dish in range(dishes):
                    if dish >= attempt:
                        score = score + satisfaction[dish] * current_satisfaction
                        current_satisfaction += 1
                if score > max_score:
                    max_score = score
                else:
                    score_is_ascending = False
        return max_score


solver = Solution()

assert solver.maxSatisfaction([-1, -8, 0, 5, -9]) == 14
assert solver.maxSatisfaction([-2, 5, -1, 0, 3, -3]) == 35
assert solver.maxSatisfaction([2, -2, -3, 1]) == 6
assert solver.maxSatisfaction([5, -2, 4, -3]) == 25

big_one = [446, 410, -376, -346, -239, -75, 151, -67, 191, 308, -149, -38, 334, -134, 149, -319, -297, -474, -121, 178,
           -392, 204, 274, 93, 155, 113, -166, -148, -73, -467, -417, -197, 106, -17, -226, 362, 327, -252, -126, -3,
           338, -392, -484, 24, -51, 227, -19, 31, 282, 125, 57, -99, 301, 254, -76, 389, 415, 465, -174, 355, 451, 364,
           95, -338, -443, -88, 279, 239, -300, -271, -487, 149, -391, 321, 356, -22, 71, 443, 298, -127, -494, 127,
           458, 166, 446, 0, -56, 8, -184, 380, 42, 198, -421, -264, -350, 70, -332, 36, -77, -250, 393, -256, -123,
           -369, 366, 178, -217, -67, -366, -489, -156, -138, -60, 13, 274, -330, 226, 389, -243, -308, -393, 164, 379,
           -321, -216, 178, 194, -234, -459, -459, 112, 125, 462, 114, 278, 396, 58, -283, -123, 182, 272, -478, -220,
           334, 249, 428, -212, 344, -434, -266, -184, 406, 365, -442, 285, -236, -473, -174, -247, 87, 208, 98, -481,
           208, -17, 298, -439, -477, -365, -287, 277, -214, 198, -54, 326, 264, 80, 484, -171, -146, 132, -33, -468,
           25, 108, 318, 422, -179, -484, -489, 385, -176, -484, 236, 90, 224, 190, 235, 345, -174, -259, -21, 388,
           -408, -416, -166, -108, -292, -241, -406, 139, 0, -395, -230, -379, -14, 315, -429, -320, 276, 399, -223,
           347, 30, 239, 143, -28, -369, 477, 364, 395, -145, -487, 320, 187, -164, -112, 111, -118, -289, -171, 444,
           -360, 269, 103, 371, -331, -195, -116, -218, 43, -371, 416, 308, -480, -65, 146, -169, 175, -157, 17, -11,
           468, -463, -16, -322, -38, 253, 478, 325, 251, 383, 33, 204, -473, -5, 375, -33, 140, 103, -258, -412, 458,
           206, -29, 2, 188, -21, -200, -88, -386, -4, -152, 472, 91, 358, -287, -306, 270, 247, -254, 114, 291, 90,
           -487, -479, -15, -384, 449, -349, 74, -400, -179, -110, -22, -210, -489, 386, -428, -446, 42, -458, 207,
           -420, -2, -195, 176, -280, 244, -396, 145, -411, 438, -138, -426, 214, 459, -222, 430, -140, -16, -68, 254,
           -188, 140, 421, 407, 54, 35, -430, 438, -79, -210, 447, 447, 167, -261, 414, -406, 334, -359, 403, 177, -2,
           -166, 55, 465, 91, -175, -72, 146, -404, 411, -19, 457, -458, 295, 167, 407, 495, 13, 366, -101]

assert solver.maxSatisfaction(big_one) == 12097786
