# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        # Define function to reverse a segment, and return the new first
        # node of the segment (which previously the final node)
        def reverse_segment(first_node, node_after_final_node, segment_length):
            prev = node_after_final_node
            curr = first_node

            for _ in range(segment_length):
                tmp = curr.next

                # Swap the next pointer for the current node
                curr.next = prev

                # Set up for next iteration
                prev = curr
                curr = tmp

            return prev if segment_length else curr

        # Get the node before the left node if we're not starting at the
        # head
        node_before_left_node = None
        left_node = head

        if left > 1:
            node_before_left_node = head

            for _ in range(left - 2):
                node_before_left_node = node_before_left_node.next

            left_node = node_before_left_node.next

        # Grab the node after the right node
        segment_length = right - left + 1

        node_after_right_node = left_node

        for _ in range(segment_length):
            node_after_right_node = node_after_right_node.next

        # Now use the above function to reverse the segment of the
        # linked list. How we do this depends on if the left node is the
        # original head node or not.
        if node_before_left_node is None:
            return reverse_segment(head, node_after_right_node, segment_length)

        node_before_left_node.next = reverse_segment(
            node_before_left_node.next, node_after_right_node, segment_length
        )

        return head


# @leet end
