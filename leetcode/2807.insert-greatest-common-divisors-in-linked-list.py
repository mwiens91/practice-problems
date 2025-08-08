# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode | None) -> ListNode | None:
        this_node = head
        next_node = head.next

        while next_node is not None:
            this_node.next = ListNode(
                val=math.gcd(this_node.val, next_node.val), next=next_node
            )

            this_node = next_node
            next_node = next_node.next

        return head


# @leet end
