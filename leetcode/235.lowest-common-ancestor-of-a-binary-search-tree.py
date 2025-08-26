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
        small, big = sorted((p, q), key=lambda node: node.val)

        def get_lca(node: TreeNode) -> TreeNode:
            if small.val <= node.val <= big.val:
                # Found LCA
                return node

            # Small and big are in same subtree
            if small.val < node.val:
                return get_lca(node.left)

            return get_lca(node.right)

        return get_lca(root)


# @leet end
