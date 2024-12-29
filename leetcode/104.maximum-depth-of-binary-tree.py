# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: ListNode | None) -> int:
        # Use depth-first search to find maximum depth
        max_depth = 0

        def dfs(node: ListNode | None, current_depth: int = 1) -> None:
            nonlocal max_depth

            # Base case: reached null node, update maximum depth
            if node is None:
                # We need to update using the parent node's depth which,
                # is the null node's depth minus 1
                max_depth = max(max_depth, current_depth - 1)

                return

            # Keep recursing
            for child in (node.left, node.right):
                dfs(child, current_depth + 1)

        # Find maximum depth
        dfs(root)

        return max_depth


# @leet end
