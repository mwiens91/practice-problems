# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node'
    = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: ListNode | None) -> ListNode | None:
        # We'll have two recursive functions. The first sets a given
        # node's left child to point to its right child.
        def recurse_point_descendants(node: ListNode) -> None:
            # If we're at a leaf, get out
            if node.left is None:
                return

            # Set left to point to right
            node.left.next = node.right

            # Recurse on children
            for child in [node.left, node.right]:
                recurse_point_descendants(child)

        # The second sets right nodes of a subtree to point to left
        # nodes of a subtree to the right of the first subtree
        def recurse_point_adjacent(left: ListNode, right: ListNode) -> None:
            # If we're at a leaf, get out
            if left.left is None:
                return

            # Set left node's right child to point to right node's left
            # child
            left.right.next = right.left

            # Recurse
            recurse_point_adjacent(left.right, right.left)
            recurse_point_adjacent(left.left, left.right)
            recurse_point_adjacent(right.left, right.right)

            return

        # Get out if the root is null or the root has no children
        if root is None or root.left is None:
            return None

        # Connect the tree
        recurse_point_descendants(root)
        recurse_point_adjacent(root.left, root.right)

        return root


# @leet end
