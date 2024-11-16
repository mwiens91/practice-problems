# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Handle edge case
        if head is None or head.next is None:
            return head

        # Idea: swap every two adjacent nodes. node1 will point to the
        # first node in a pair as it originally occured and node2 will
        # point to the second node
        node1 = head
        node2 = head.next

        # Before iterating, make sure head points to the correct node
        # (after performing swaps)
        head = node2

        while True:
            # Swap
            node1.next = node2.next
            node2.next = node1

            # Get out if there isn't another pair
            if node1.next is None or node1.next.next is None:
                break

            # Get the next pair and make sure the current node1 (after
            # the swap, the seocnd element of the pair) points to the
            # next node2, as we did for the head above
            temp = node1

            node1 = node1.next
            node2 = node1.next

            temp.next = node2

        return head


# @leet end
