# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        # Inorder traversal of a BST goes in sorted order
        min_difference = math.inf

        current = root
        prev = None
        stack: list[TreeNode] = []

        while current is not None or stack:
            # Explore left tree
            while current is not None:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()

            if prev is not None:
                min_difference = min(min_difference, abs(current.val - prev.val))

            prev = current

            # Explore right tree
            current = current.right

        return min_difference


# @leet end
