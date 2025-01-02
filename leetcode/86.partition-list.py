# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # We'll have two pointers. One pointer will point to the last
        # node that we've seen that is less than x. We will splice in
        # new nodes that we see that are less than x after this pointer
        # and reset this pointer to the new node we splice in. The other
        # pointer will point to the current node we're looking at.
        last_node_less_than_x = None
        current_node = head

        # First, skip to the last node less than x at the front of the
        # list
        while current_node and current_node.val < x:
            last_node_less_than_x = current_node
            current_node = current_node.next

        # Now move nodes less than x in front of the "less than x"
        # pointer
        prev_node = last_node_less_than_x

        while current_node:
            next_node = current_node.next

            if current_node.val < x:
                # We're going to splice out the current node
                prev_node.next = next_node

                if last_node_less_than_x is None:
                    # Set the current node to be the head
                    current_node.next = head
                    head = current_node

                    last_node_less_than_x = current_node
                else:
                    # Splice in the current node
                    current_node.next = last_node_less_than_x.next
                    last_node_less_than_x.next = current_node

                    # Move up the last node less than x pointer
                    last_node_less_than_x = last_node_less_than_x.next
            else:
                # If we spliced the current node in, we keep the
                # previous node the same; when we don't splice, we set
                # it to the current node
                prev_node = current_node

            current_node = next_node

        return head


# @leet end
