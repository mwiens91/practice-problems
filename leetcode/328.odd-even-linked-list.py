# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # Get length of list
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        # If length is <= 2, we don't need to do anything
        if length <= 2:
            return head

        # Now get a pointer to the last odd node
        last_odd_node = head

        # We need to move forward length - 1 elements to get to the
        # final node, which may or may not be the final odd node. If the
        # total length is odd, the final odd node is the last node; and
        # (length - 1) // 2 * 2 = length - 1. If the total length is
        # even, the final odd node is the second to last node; and
        # (length - 1) // 2 * 2 = length - 2.
        for _ in range((length - 1) // 2 * 2):
            last_odd_node = last_odd_node.next

        # Now we'll move each (originally) even node prior to the
        # (originally) last odd node to either the end of the list, or
        # to one before the end of the list, depending on if the length
        # is odd or even, respectively
        next_even_node_parent = head
        node_to_insert_after = last_odd_node

        while True:
            next_even_node = next_even_node_parent.next

            # Splice out the even node
            next_even_node_parent.next = next_even_node.next

            # Splice in the even node
            tail = node_to_insert_after.next
            node_to_insert_after.next = next_even_node
            next_even_node.next = tail

            # Move up the next even node parent, but get out of the loop
            # if we've reached the original last odd node
            next_even_node_parent = next_even_node_parent.next

            # Move up the node to insert after
            node_to_insert_after = node_to_insert_after.next

            if next_even_node_parent == last_odd_node:
                break

        return head


# @leet end
