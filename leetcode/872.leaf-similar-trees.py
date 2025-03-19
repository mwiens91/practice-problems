# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import zip_longest
from typing import Generator


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        # Write a generator function to yield leaves of a tree
        def get_leaf_value_iterator(
            node: TreeNode | None,
        ) -> Generator[int, None, None]:
            if node is not None:
                if node.left is None and node.right is None:
                    # At a leaf, so yield the value
                    yield node.val
                else:
                    # Recurse into the left and right subtrees
                    yield from get_leaf_value_iterator(node.left)
                    yield from get_leaf_value_iterator(node.right)

        # Ensure both leaf value sequences are the same
        tree_1_leaf_value_iter = get_leaf_value_iterator(root1)
        tree_2_leaf_value_iter = get_leaf_value_iterator(root2)

        return all(
            tree_1_leaf_val == tree_2_leaf_val
            for tree_1_leaf_val, tree_2_leaf_val in zip_longest(
                tree_1_leaf_value_iter, tree_2_leaf_value_iter
            )
        )


# @leet end
