# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # Handle head is None
        if head is None:
            return None

        # Keep track of previous node
        prev_node = None

        while True:
            # Finished reversing
            if head.next is None:
                head.next = prev_node

                return head

            # Make head point to prev_node and redefine head and
            # prev_node for next iteration
            tmp = head.next
            head.next = prev_node

            prev_node = head
            head = tmp


# @leet end
