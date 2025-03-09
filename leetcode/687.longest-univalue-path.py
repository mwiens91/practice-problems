# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        # We'll define a function which takes in a node and calculates
        # the longest length left and right non-forking paths containing
        # descendants with the same value as the node. For the node, we
        # consider it as (1) a child of a subtree that we return the
        # maximum of the left or right non-forking path lengths to and
        # (2) as the root of its own subtree where we "fork" using both
        # left and right paths. For (2) we update a nonlocal variable
        # which keeps track of the subtree with the longest forking
        # path.
        longest_forking_path_length = 0

        def get_longest_non_forking_path(node: TreeNode) -> int:
            nonlocal longest_forking_path_length

            # Calculate the longest non-forking path lengths for the
            # left and right children. The first index is for the left
            # node, the second is for the right.
            children = [node.left, node.right]

            non_forking_path_lengths = [0, 0]

            for idx, child in enumerate(children):
                if child is not None:
                    # Get the longest non-forking path length of the
                    # child and also have it be considered the root of
                    # its own subtree, updating the longest forking path
                    # length
                    child_non_forking_path_length = get_longest_non_forking_path(child)

                    if child.val == node.val:
                        non_forking_path_lengths[idx] = (
                            1 + child_non_forking_path_length
                        )

            # Update the longest forking path length by considering this
            # node as the root of its own subtree
            longest_forking_path_length = max(
                longest_forking_path_length, sum(non_forking_path_lengths)
            )

            # Return the longest non-forking path length
            return max(non_forking_path_lengths)

        if root is not None:
            get_longest_non_forking_path(root)

        return longest_forking_path_length


# @leet end
