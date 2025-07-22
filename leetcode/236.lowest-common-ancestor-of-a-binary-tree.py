# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # NOTE: used ChatGPT for hints

        # This function returns None if neither p nor q exist in the
        # subtree, p if only p exists in the subtree, q if only q exists
        # in the subtree, and the LCA if both p and q exist in the
        # subtree
        def get_lca(node: TreeNode | None) -> TreeNode | None:
            if node is None or node == p or node == q:
                return node

            left = get_lca(node.left)
            right = get_lca(node.right)

            if left is not None and right is not None:
                # Found LCA
                return node

            return left if left is not None else right

        return get_lca(root)


# @leet end
