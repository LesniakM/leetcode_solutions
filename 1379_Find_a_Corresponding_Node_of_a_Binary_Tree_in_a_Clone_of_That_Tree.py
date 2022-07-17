"""
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer
must be a reference to a node in the cloned tree.


Example 1:

Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. T
he target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Result:
Runtime: 862 ms, faster than 47.01% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 24 MB, less than 39.00% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.output_node = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned.val == target.val:
            return cloned

        self.output_node = None

        def go_deeper(o, c, t):
            if not o:
                return None

            if o == t:
                self.output_node = c
                return None

            go_deeper(o.left, c.left, t)
            go_deeper(o.right, c.right, t)

        go_deeper(original, cloned, target)

        return self.output_node


# Test tree 1
target_node_o = TreeNode(3, TreeNode(6), TreeNode(19))
target_node_c = TreeNode(3, TreeNode(6), TreeNode(19))
cloned_t = TreeNode(7, TreeNode(4), target_node_c)
original_t = TreeNode(7, TreeNode(4), target_node_o)

# Test tree 2
target_node_4321_o = TreeNode(4, right=TreeNode(3, right=TreeNode(2, right=TreeNode(1))))
target_node_4321_c = TreeNode(4, right=TreeNode(3, right=TreeNode(2, right=TreeNode(1))))
original_tree = TreeNode(8, right=TreeNode(7, right=TreeNode(6, right=TreeNode(5, right=target_node_4321_o))))
copied_tree = TreeNode(8, right=TreeNode(7, right=TreeNode(6, right=TreeNode(5, right=target_node_4321_c))))

solver = Solution()

assert solver.getTargetCopy(original_t, cloned_t, target_node_o) == target_node_c, "1 Not works"
assert solver.getTargetCopy(original_tree, copied_tree, target_node_4321_o) == target_node_4321_c, "2 Not works"
