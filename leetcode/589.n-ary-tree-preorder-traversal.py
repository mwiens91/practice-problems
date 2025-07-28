# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> list[int]:
        if root is None:
            return []

        result: list[int] = []
        stack = [root]

        while stack:
            node = stack.pop()

            result.append(node.val)

            if node.children:
                stack.extend(reversed(node.children))

        return result


# @leet end
