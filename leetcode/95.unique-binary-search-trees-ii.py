# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import itertools


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        # Ranges for subtree values are exclusive, so (1, 3) for example
        # denotes a range containing 1, 2. This function generate a tree
        # given a root value, a range of values on the left, and a range
        # of values on the right.
        def generate_trees(
            root_val: int,
            left_tree_range: tuple[int, int],
            right_tree_range: tuple[int, int],
        ) -> list[TreeNode]:
            # Function to generate all left or right subtrees
            def generate_subtrees(left: bool) -> list[TreeNode | None]:
                # Get the left or right tree range depending on which
                # we're generating
                if left:
                    tree_range = left_tree_range
                else:
                    tree_range = right_tree_range

                # Return a null node if empty range
                if tree_range[0] == tree_range[1]:
                    return [None]

                subtrees = []

                for child_root_val in range(tree_range[0], tree_range[1]):
                    child_left_tree_range = (tree_range[0], child_root_val)
                    child_right_tree_range = (child_root_val + 1, tree_range[1])

                    subtrees += generate_trees(
                        child_root_val, child_left_tree_range, child_right_tree_range
                    )

                return subtrees

            # Make all combination of trees
            trees = []

            for left_subtree, right_subtree in itertools.product(
                generate_subtrees(left=True), generate_subtrees(left=False)
            ):
                trees.append(
                    TreeNode(val=root_val, left=left_subtree, right=right_subtree)
                )

            return trees

        # Now generate all trees from n
        all_trees = []

        for i in range(1, n + 1):
            all_trees += generate_trees(i, (1, i), (i + 1, n + 1))

        return all_trees


# @leet end
