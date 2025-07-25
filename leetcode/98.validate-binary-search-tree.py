# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate_subtree(
            node: TreeNode | None,
            min_val: int | float = -math.inf,
            max_val: int | float = math.inf,
        ) -> bool:
            if node is None:
                return True

            if not min_val <= node.val <= max_val:
                return False

            return validate_subtree(
                node.left, min_val, node.val - 1
            ) and validate_subtree(node.right, node.val + 1, max_val)

        return validate_subtree(root)


# @leet end
