# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # Replace head until it has a non-val value
        while head and head.val == val:
            head = head.next

        # Go through the rest of the node and splice out val valued
        # nodes
        prev = head
        node = None if head is None else head.next

        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node

            node = node.next

        return head


# @leet end
