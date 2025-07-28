# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> list[int]:
        if root is None:
            return []

        result: list[int] = []
        stack = [(root, False)]  # stack contains tuples (node, visited)

        while stack:
            node, visited = stack.pop()

            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))

                if node.children:
                    stack.extend([(child, False) for child in reversed(node.children)])

        return result


# @leet end
