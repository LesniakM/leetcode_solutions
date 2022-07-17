"""
https://leetcode.com/problems/defanging-an-ip-address/
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Result:
Runtime: 35 ms, faster than 82.05% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 13.8 MB, less than 95.00% of Python3 online submissions for Defanging an IP Address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
