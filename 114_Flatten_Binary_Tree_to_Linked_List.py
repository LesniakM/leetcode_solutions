"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in
the list and the left child pointer is always null.

The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Result:
Runtime: 48 ms, faster than 73.04% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.6 MB, less than 10.29% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""
from queue import LifoQueue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution:
class Solution:
    @staticmethod
    def flatten(root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        park = LifoQueue()

        def deep_dive(tree: TreeNode):
            if tree.right and tree.left:
                park.put(tree.right)
                tree.right = tree.left
                tree.left = None
                deep_dive(tree.right)
            elif tree.left:
                tree.right = tree.left
                tree.left = None
                deep_dive(tree.right)
            elif tree.right:
                deep_dive(tree.right)
            elif not park.empty():
                tree.right = park.get()
                deep_dive(tree.right)
        if root:
            deep_dive(root)


# Utility functions:
def print_out_tree(tree: TreeNode) -> None:
    if tree.left:
        print_out_tree(tree.left)
    print(tree.val, end=" ")
    if tree.right:
        print_out_tree(tree.right)


test_tree = TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(3)), TreeNode(5, None, TreeNode(6)))
test_tree2 = TreeNode(1, left=TreeNode(2))
test_tree3 = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3, left=None)))

solver = Solution()

print(print_out_tree(test_tree))
solver.flatten(test_tree)
print(print_out_tree(test_tree))
print()
print(print_out_tree(test_tree2))
solver.flatten(test_tree2)
print(print_out_tree(test_tree2))
print()
print(print_out_tree(test_tree3))
solver.flatten(test_tree3)
print(print_out_tree(test_tree3))
