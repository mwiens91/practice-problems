# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # Use recursion to find if path sum exists
        def recurse(node: TreeNode | None, current_sum: int) -> bool:
            # Base case: we're at a leaf
            if node.left is None and node.right is None:
                return current_sum + node.val == targetSum

            # Recursive steps
            for child in [node.left, node.right]:
                if child is not None:
                    # Base case will evaluate true at a leaf, so this is
                    # passing up the True value to the root
                    if recurse(child, current_sum + node.val):
                        return True

            return False

        # Handle edge case: root is None
        if root is None:
            return False

        return recurse(root, 0)


# @leet end
