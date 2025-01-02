# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Remove duplicates as we encounter them
        prev = None
        node = head

        while node and node.next:
            # Remove duplicate child nodes
            keep_current_node = True

            while node.next and node.val == node.next.val:
                keep_current_node = False
                node.next = node.next.next

            # Keep current node if there were no duplicates; otherwise,
            # remove it
            if keep_current_node:
                prev = node
            else:
                # Set previous node next to the next available node if
                # there is a previous node. Otherwise, set the head to
                # the next available node.
                if prev is not None:
                    prev.next = node.next
                else:
                    head = node.next

            # Move to next node
            node = node.next

        return head


# @leet end
