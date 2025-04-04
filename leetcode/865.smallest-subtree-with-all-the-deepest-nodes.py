# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:
        # NOTE: this problem is a duplicate of LC 1123. The solution for
        # that has comments.
        def find_depth_and_lca(node: TreeNode | None) -> tuple[int, TreeNode | None]:
            if node is None:
                return (0, None)

            left_depth, left_lca = find_depth_and_lca(node.left)
            right_depth, right_lca = find_depth_and_lca(node.right)

            if left_depth == right_depth:
                return (left_depth + 1, node)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)

            return (right_depth + 1, right_lca)

        _, lca_node = find_depth_and_lca(root)

        return lca_node


# @leet end
