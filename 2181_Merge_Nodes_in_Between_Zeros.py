"""
https://leetcode.com/problems/merge-nodes-in-between-zeros/
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.



Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation:
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Result:
Runtime: 2041 ms, faster than 99.93% of Python3 online submissions for Merge Nodes in Between Zeros.
Memory Usage: 69.7 MB, less than 96.52% of Python3 online submissions for Merge Nodes in Between Zeros.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        next_node = head.next
        sumed = 0

        while next_node:                         # As long as next node is not None...
            if next_node.val == 0:                 # If next node is 0...
                current_node = current_node.next     # Go to next pos
                current_node.val = sumed             # Update value
                sumed = 0                            # Reset counter
            else:                                  # Elif next node is not 0...
                sumed += next_node.val               # Accumulate the counter
            next_node = next_node.next             # Go to next node

        current_node.next = None                 # Cutout the rest when reached the bottom
        return head.next                         # Return ListNode line above, drop first node.


def node_vals(node_list):
    vals = []

    def dig_in_node(nodelist):
        vals.append(nodelist.val)
        if nodelist.next:
            dig_in_node(nodelist.next)

    dig_in_node(node_list)
    return vals


nodes = [0, 3, 1, 0, 4, 5, 2, 0]
c_node = ListNode(nodes.pop(-1))
for node in reversed(nodes):
    c_node = ListNode(node, c_node)

solver = Solution()

correct_answer = ListNode(4, ListNode(11))
proposed_answer = solver.mergeNodes(c_node)
print(node_vals(proposed_answer))

assert node_vals(proposed_answer) == node_vals(correct_answer)
