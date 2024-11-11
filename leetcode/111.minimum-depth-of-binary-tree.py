# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        # We'll find the minimum depth recursively
        best_depth = math.inf

        def recurse(node: TreeNode | None, current_depth: int) -> None:
            nonlocal best_depth

            # Base case: we're at a leaf
            if node.left is None and node.right is None:
                best_depth = min(best_depth, current_depth)

            # Recurse
            for child in (node.left, node.right):
                if child is not None:
                    recurse(child, current_depth + 1)

        # Handle edge case of null root
        if root is None:
            return 0

        # Perform recursion and return the minimum depth
        recurse(root, 1)

        return best_depth


# @leet end
