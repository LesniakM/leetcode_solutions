"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

# Definition for a binary tree node.
from typing import Optional, Union, List
from queue import Queue


class TreeNode:
    def __init__(self, val: Union[int, str] = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int], in_start=0, in_end=None) -> Optional[TreeNode]:
        if in_end is None:
            in_end = len(preorder) - 1
        if in_start > in_end:
            return None

        node_val = preorder[self.pre_index]
        node_tree = TreeNode(node_val)
        self.pre_index += 1

        in_index = inorder.index(node_val)
        if in_start == in_end and (len(inorder[in_start:in_index - 1]) == len(inorder[in_index + 1:in_end])):
            return node_tree

        if in_start == in_index:
            node_tree.left = TreeNode("null")
        else:
            node_tree.left = self.buildTree(preorder, inorder, in_start, in_index - 1)

        if in_index == in_end:
            node_tree.right = TreeNode("null")
        else:
            node_tree.right = self.buildTree(preorder, inorder, in_index + 1, in_end)

        return node_tree


def return_tree_by_levels(tree_node: TreeNode):
    if tree_node is None:
        return
    q = Queue()
    q.put(tree_node)
    out = []
    while not q.empty():
        node = q.get()
        if node is None:
            continue
        out.append(node.val)
        q.put(node.left)
        q.put(node.right)
    while out[-1] == "null":
        out.pop(-1)
    else:
        return out


test_trees = [([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7]),
              ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, 'null', 'null', 15, 7]),
              ([-1], [-1], [-1]),
              ([1, 2], [2, 1], [1, 2]),
              ([2, 1, 3, 4, 5], [1, 2, 3, 4, 5], [2, 1, 3, 'null', 'null', 'null', 4, 'null', 5]),
              ([1, 2, 3], [1, 2, 3], [1, 'null', 2, 'null', 3])]

solver = Solution()

for tree in test_trees:
    answer = return_tree_by_levels(solver.buildTree(tree[0], tree[1]))
    solver.pre_index = 0
    assert answer == tree[2], f"Expected: {tree[2]}, got {answer}"
    print(answer)
