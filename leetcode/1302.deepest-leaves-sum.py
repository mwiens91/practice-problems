# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        # Find the sum of nodes at the maximum depth (these must be leaves)
        max_depth = 0
        max_depth_val_sum = 0

        def find_deepest_leaves_sum(node: TreeNode | None, depth: int = 0) -> None:
            nonlocal max_depth, max_depth_val_sum

            if node is None:
                return

            # Visit children
            for child in [node.left, node.right]:
                find_deepest_leaves_sum(child, depth + 1)

            # Update maximum depth and maximum depth value sum
            if depth > max_depth:
                max_depth = depth
                max_depth_val_sum = node.val
            elif depth == max_depth:
                max_depth_val_sum += node.val

        find_deepest_leaves_sum(root)

        return max_depth_val_sum


# @leet end
