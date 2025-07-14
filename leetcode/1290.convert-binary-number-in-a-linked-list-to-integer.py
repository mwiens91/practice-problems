# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        num = 0

        while head is not None:
            num <<= 1
            num |= head.val

            head = head.next

        return num


# @leet end
