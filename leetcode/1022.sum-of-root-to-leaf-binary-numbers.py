# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        # NOTE: root is guaranteed to be non-null given problem
        # constraints
        def get_root_to_leaf_sum(node: TreeNode, path_val: int) -> int:
            # Update path value
            path_val = (path_val << 1) | node.val

            # Base case: leaf
            if node.left is None and node.right is None:
                return path_val

            # Collect root to leaf sums from children
            return (
                get_root_to_leaf_sum(node.left, path_val)
                if node.left is not None
                else 0
            ) + (
                get_root_to_leaf_sum(node.right, path_val)
                if node.right is not None
                else 0
            )

        return get_root_to_leaf_sum(root, 0)


# @leet end
