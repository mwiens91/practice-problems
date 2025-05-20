# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Pull values of the next node into the current node until the
        # we're at the second to last node
        while node.next.next is not None:
            node.val = node.next.val
            node = node.next

        # Pull the last value and remove the last node
        node.val = node.next.val
        node.next = None


# @leet end
