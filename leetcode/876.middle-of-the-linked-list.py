# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # Let's find out how long the list is, then return the middle,
        # rounding up
        count = 0

        tmp_head = head

        while tmp_head.next is not None:
            count += 1
            tmp_head = tmp_head.next

        # Now go to middle and return it
        to_middle = ceil(count / 2)

        for _ in range(to_middle):
            head = head.next

        return head


# @leet end
