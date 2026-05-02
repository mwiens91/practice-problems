# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.helper(root, -inf, inf)

    def helper(self, node: TreeNode | None, min_: int, max_: int) -> bool:
        if not node:
            return True

        if node.val <= min_ or node.val >= max_:
            return False

        return self.helper(node.left, min_, min(max_, node.val)) and self.helper(
            node.right, max(min_, node.val), max_
        )


# @leet end
