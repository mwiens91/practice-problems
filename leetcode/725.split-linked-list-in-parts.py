# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        # Get number of nodes in list
        length = 0
        node = head

        while node is not None:
            length += 1
            node = node.next

        # Split list into parts
        nodes_per_part = length // k
        extra = length % k

        result: list[ListNode | None] = []

        prev = None
        node = head

        for _ in range(k):
            result.append(node)
            count = 0

            # Assign nodes to part
            while count < nodes_per_part:
                count += 1
                prev = node
                node = node.next

            # Possibly assign an extra node
            if extra > 0:
                extra -= 1
                prev = node
                node = node.next

            # Set up head for next iteration and set the tail of those
            # part to None
            if prev is not None:
                prev.next = None

        return result


# @leet end
