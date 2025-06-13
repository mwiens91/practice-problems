# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Edge case: head is null
        if head is None:
            return head

        node = head

        # For each node, while the next node's value is the same as the
        # current value, splice out the next node. Then move to the next
        # node (after any splicing has finished).
        while node.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next

                continue

            node = node.next

        return head


# @leet end
