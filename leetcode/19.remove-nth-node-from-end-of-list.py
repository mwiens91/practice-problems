# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Do this in one pass using the hint: we'll have one pointer i
        # that is n + 1 nodes ahead of another pointer j. Once i reaches
        # the end, j will point to the n + 1-th node from the end and
        # we can remove the nth node from the end easily from there.
        i = head
        j = head

        # Just move i forward n nodes for now, we might need to remove
        # the head
        for _ in range(n):
            i = i.next

        # We need to remove the head
        if i.next is None:
            return head.next

        # Move once more so it's n + 1 nodes forward
        i = i.next

        # Now move i and j in step
        while i.next is not None:
            i = i.next
            j = j.next

        # Get rid of the node ahead of j
        j.next = j.next.next

        return head
# @leet end
