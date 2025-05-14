# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        # Define function to get length of a list
        def get_length(node: ListNode) -> int:
            length = 0

            while node is not None:
                length += 1
                node = node.next

            return length

        # Move the longer list forward so that both lists have the same
        # length
        length_a = get_length(headA)
        length_b = get_length(headB)
        shorter, longer = (headA, headB) if length_a <= length_b else (headB, headA)

        for _ in range(abs(length_b - length_a)):
            longer = longer.next

        # Now find intersection
        while shorter is not None and shorter != longer:
            shorter = shorter.next
            longer = longer.next

        return shorter


# @leet end
