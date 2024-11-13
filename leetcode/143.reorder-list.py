# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # First we find the length of the linked list n
        n = 1

        node = head

        while node.next is not None:
            node = node.next
            n += 1

        # Deal with edge cases n == 1, n == 2
        if n in {1, 2}:
            return

        # Next, we put a given number of nodes onto a stack
        stack = []

        num_tail_nodes_to_get = math.ceil(n / 2)

        node = head

        # Traverse head nodes until we reach the nodes we want on the
        # stack
        num_head_nodes_to_skip = n - num_tail_nodes_to_get

        for _ in range(num_head_nodes_to_skip):
            node = node.next

        # Put the nodes we want on the stack
        for _ in range(num_tail_nodes_to_get):
            stack.append(node)
            node = node.next

        # Now we merge the nodes in the stack into the list. The idea is
        # we put in the last node in the stack in front of our main node
        # (called node). Then we pop another node from the stack and set
        # its next value to None (it's now the final node in the linked
        # list). If this is the last node in the stack, we return (it's
        # already in it's correct place); otherwise, we repeat with this
        # node being the next element to insert. Note because we have
        # two consecutive stack pops when we initially run this, we need
        # the stack to have at least two elements, which requires
        # n >= 3.
        node = head
        last_tail_node = stack.pop()

        while True:
            # Splice
            temp = node.next
            node.next = last_tail_node
            last_tail_node.next = temp

            # Set the last tail node's next pointer to null
            last_tail_node = stack.pop()
            last_tail_node.next = None

            # Exit if the stack is empty, else move node ahead twice
            if not stack:
                return

            node = node.next.next


# @leet end
