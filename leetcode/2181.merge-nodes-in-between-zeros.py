# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        # NOTE: Not the simplest solution. I misunderstood the expected
        # output initially and ended up modifying that solution to match
        # the correct expected output. *Probably* should just rewrite
        # this, but no time right now.
        new_head = head.next
        last_merged_node = None

        # Iterate over node sequence 0, ..., 0. We start each iteration
        # of this loop at a node with value 0.
        node = head

        while node.next is not None:
            # We'll put the sum of node values in the first non-zero
            # node and merge it into the new linked list
            node_to_merge = node.next

            # Get the sum of node values in between zeros
            val_sum = 0

            while node.next.val != 0:
                val_sum += node.next.val
                node = node.next

            # Set the node to merge's value to the sum of node values
            # and merge the node
            node_to_merge.val = val_sum

            if last_merged_node is not None:
                last_merged_node.next = node_to_merge

            last_merged_node = node_to_merge

            # Move node to the next zero value for next iteration
            node = node.next

        # Point the tail of the new linked list to a null node
        last_merged_node.next = None

        return new_head


# @leet end
