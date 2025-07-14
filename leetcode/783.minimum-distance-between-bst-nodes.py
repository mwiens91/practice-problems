# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        # NOTE: duplicate of LC 530
        min_difference = math.inf

        current = root
        prev = None
        stack: list[TreeNode] = []

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if prev is not None:
                min_difference = min(min_difference, abs(current.val - prev.val))

            prev = current

            current = current.right

        return min_difference


# @leet end
