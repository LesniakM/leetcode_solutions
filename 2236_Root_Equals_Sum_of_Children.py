"""
https://leetcode.com/problems/root-equals-sum-of-children/
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

Example 1:

Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.

Result:
<Results are very inaccurate for this problem>
Runtime: 35 ms, faster than 87.51% of Python3 online submissions for Root Equals Sum of Children.
Memory Usage: 13.7 MB MB, less than 93.36% of Python3 online submissions for Root Equals Sum of Children.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        return (root.left.val + root.right.val) == root.val


solver = Solution()
assert solver.checkTree(TreeNode(10, TreeNode(4), TreeNode(6))) is True, "1st"
assert solver.checkTree(TreeNode(5, TreeNode(3), TreeNode(1))) is False, "2nd"
