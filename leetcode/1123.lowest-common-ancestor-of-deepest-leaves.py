# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        # Define a depth first search function which for each node which
        # returns depth of the subtree rooted at the node and the lowest
        # common ancestor (LCA) containing the deepest nodes in the
        # subtree
        def find_depth_and_lca(node: TreeNode | None) -> tuple[int, TreeNode | None]:
            # Handle null node
            if node is None:
                return (0, None)

            # Get the depth and LCA of the left and right subtrees
            left_depth, left_lca = find_depth_and_lca(node.left)
            right_depth, right_lca = find_depth_and_lca(node.right)

            # If the left and right subtrees are equally deep, this node
            # is the LCA
            if left_depth == right_depth:
                return (left_depth + 1, node)

            # Whichever of the left or right subtrees is deeper, the
            # depth of this subtree is given by that and the LCA is
            # taken from the deeper branch
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)

            return (right_depth + 1, right_lca)

        _, lca_node = find_depth_and_lca(root)

        return lca_node


# @leet end
