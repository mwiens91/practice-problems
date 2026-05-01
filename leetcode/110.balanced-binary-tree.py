# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
IMBALANCED = -2


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.helper(root) != IMBALANCED

    def helper(self, node: TreeNode | None) -> int:
        if not node:
            return -1

        left_height = self.helper(node.left)

        if left_height == IMBALANCED:
            return IMBALANCED

        right_height = self.helper(node.right)

        if right_height == IMBALANCED or abs(left_height - right_height) > 1:
            return IMBALANCED

        return 1 + max(left_height, right_height)


# @leet end
