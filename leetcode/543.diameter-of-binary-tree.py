# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        # This is a slightly simpler version of LeetCode 687. I'm going
        # to use a stripped down solution of what I did there, with less
        # explanation.
        longest_path = 0

        def get_longest_left_or_right_path(node: TreeNode) -> int:
            # Return longest left or right path and update longest path
            # using current node as part of a path containing both left
            # and right subtree paths
            nonlocal longest_path

            children = [node.left, node.right]
            child_path_lengths = [0, 0]

            for i, child in enumerate(children):
                if child is not None:
                    child_path_lengths[i] = 1 + get_longest_left_or_right_path(child)

            # Use current node as part of path containing left and right
            # paths
            longest_path = max(longest_path, sum(child_path_lengths))

            # Return maximum of left or right paths
            return max(child_path_lengths)

        if root is not None:
            get_longest_left_or_right_path(longest_path)

        return longest_path


# @leet end
