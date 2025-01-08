# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        # Get out if the root is None or root value is either x or y
        if root is None or root.val in {x, y}:
            return False

        # Find depths and parents of x and y simultaneously
        depth_x = None
        depth_y = None

        parent_x = None
        parent_y = None

        # Enqueue nodes into here along with their depth and parent
        queue = deque([(root, 0, None)])

        while queue:
            # Get a node
            node, depth, parent = queue.pop()

            if node is None:
                continue

            # Set the depth and parent of x and y values if we encounter
            # them
            if node.val == x:
                depth_x = depth
                parent_x = parent
            elif node.val == y:
                depth_y = depth
                parent_y = parent

            # If we've found both values, return the result
            if depth_x is not None and depth_y is not None:
                return depth_x == depth_y and parent_x != parent_y

            # Enqueue children
            for child in [node.left, node.right]:
                queue.appendleft((child, depth + 1, node.val))


# @leet end
