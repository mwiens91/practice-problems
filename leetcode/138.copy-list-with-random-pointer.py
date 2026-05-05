# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return None

        copy_map = {None: None, head: Node(head.val)}
        curr = head

        # Invariant: curr always has a copy of it made but its copy does
        # not have next and random attributes set
        while curr:
            copy = copy_map[curr]

            if curr.next not in copy_map:
                copy_map[curr.next] = Node(curr.next.val)

            if curr.random not in copy_map:
                copy_map[curr.random] = Node(curr.random.val)

            copy.next = copy_map[curr.next]
            copy.random = copy_map[curr.random]

            curr = curr.next

        return copy_map[head]


# @leet end
