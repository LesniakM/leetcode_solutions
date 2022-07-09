"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Result:
Runtime: 77 ms, faster than 82.96% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 86.52% of Python3 online submissions for Add Two Numbers.
"""

from typing import Optional


# Definition for singly-linked list. Directly for leetcode.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = list(self.unpack_node_list(l1))[::-1]
        nums2 = list(self.unpack_node_list(l2))[::-1]
        number1 = self.accumulate_values(nums1)
        number2 = self.accumulate_values(nums2)
        result = number1 + number2
        output_node = self.pack_nodes(result)
        return output_node

    @staticmethod
    def unpack_node_list(node: ListNode) -> list[int]:
        next_node = node.next
        current_node = node
        while next_node is not None:
            yield current_node.val
            current_node = current_node.next
            next_node = current_node.next
        yield current_node.val

    @staticmethod
    def accumulate_values(number: list[int]) -> int:
        total = 0
        for num in number:
            total *= 10
            total += num
        return total

    @staticmethod
    def pack_nodes(number: int) -> ListNode:
        nums = [int(char) for char in str(number)]
        current_node = ListNode(nums[0])
        for num in nums[1:]:
            current_node = ListNode(num, current_node)
        return current_node


solver = Solution()

list_node_1 = solver.pack_nodes(342)
list_node_2 = solver.pack_nodes(465)

list_node_3 = solver.pack_nodes(65)
list_node_4 = solver.pack_nodes(945)

assert list(solver.unpack_node_list(solver.addTwoNumbers(list_node_1, list_node_2))) == [7, 0, 8]
assert list(solver.unpack_node_list(solver.addTwoNumbers(list_node_3, list_node_4))) == [0, 1, 0, 1]

