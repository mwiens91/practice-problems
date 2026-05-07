# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: Node | None) -> Node | None:
        self.helper(head)

        return head

    # Returns tail of flattened
    def helper(self, head: Node | None) -> Node | None:
        prev = head
        curr = head

        while curr:
            child_tail = self.helper(curr.child)

            if child_tail:
                child_tail.next = curr.next

                if curr.next:
                    curr.next.prev = child_tail

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

                prev = child_tail
                curr = child_tail.next
            else:
                prev = curr
                curr = curr.next

        return prev


# @leet end
