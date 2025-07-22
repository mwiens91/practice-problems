# @leet start
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node'
                 = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        def recurse(node: "Node") -> "Node":
            # Skip past null nodes and leaves
            if node is None or node.left is None and node.right is None:
                return node

            # Connect left node with right node
            if node.left is not None and node.right is not None:
                node.left.next = node.right

            # Try to find a next node for the rightmost child node
            rightmost_child = node.right if node.right is not None else node.left
            candidate_parent = node.next

            while candidate_parent is not None:
                if candidate_parent.left is not None:
                    rightmost_child.next = candidate_parent.left
                    break

                if candidate_parent.right is not None:
                    rightmost_child.next = candidate_parent.right
                    break

                candidate_parent = candidate_parent.next

            recurse(node.right)
            recurse(node.left)

            return node

        return recurse(root)


# @leet end
