# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Use a depth-first search and, from the bottom up, merge each
        # nodes left subtree into its right, stacking the left onto the
        # right
        def recurse(node: TreeNode) -> None:
            # Depth first
            for child in (node.left, node.right):
                if child is not None:
                    recurse(child)

            # Merge left subtree into right
            if node.left is not None:
                old_right = node.right

                node.right = node.left
                node.left = None

                # Get to the deepest child of what was is now the right
                # node, and attach the old right to it
                deepest_child = node.right

                while deepest_child.right is not None:
                    deepest_child = deepest_child.right

                deepest_child.right = old_right

        # Recurse on the root if it isn't null
        if root is not None:
            recurse(root)


# @leet end
