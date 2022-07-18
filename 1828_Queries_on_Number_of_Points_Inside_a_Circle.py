"""
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle
centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle.
Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.



Example 1:


Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]
Explanation: The points and circles are shown above.
queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

Result:
Runtime: 1152 ms, faster than 94.76% of Python3 online submissions for Queries on Number of Points Inside a Circle.
Memory Usage: 14 MB, less than 99.25% of Python3 online submissions for Queries on Number of Points Inside a Circle.
"""
from timeit import timeit


class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        output = []
        for query in queries:
            points_inside = 0
            x, y, r = query[0], query[1], query[2]
            for point in points:
                dx = x - point[0]
                dy = y - point[1]
                if dx > r or dy > r or dx < -r or dy < -r:
                    continue

                if dx*dx + dy*dy <= r*r:
                    points_inside += 1
            output.append(points_inside)
        return output


solver = Solution()
assert solver.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]) == [3,2,2]

print(timeit((lambda: solver.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])), number=100000))

