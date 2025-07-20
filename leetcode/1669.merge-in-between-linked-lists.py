# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        # Get the node after which we insert list 2
        node = list1

        for _ in range(a - 1):
            node = node.next

        entry_node = node

        # Get the node to insert to the end of list 2
        for _ in range(b - a + 2):
            node = node.next

        tail_node = node

        # Splice list 2 into list 1
        entry_node.next = list2

        node = list2

        while node.next is not None:
            node = node.next

        node.next = tail_node

        return list1


# @leet end
