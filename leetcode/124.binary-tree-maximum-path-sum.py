# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # We'll define two recursive functions. One replaces the value
        # of each node with the maximum of its child path sums. The
        # other finds the maximum path containing any root.
        def replace_value_with_best_path_sum(node: TreeNode) -> None:
            non_null_children = [
                child for child in [node.left, node.right] if child is not None
            ]

            for child in non_null_children:
                if child is not None:
                    replace_value_with_best_path_sum(child)

            # Take the best left or right path, or neither of them (just
            # use this node)
            if non_null_children:
                node.val += max(0, *[child.val for child in non_null_children])

        def get_maximum_path_sum(node: TreeNode) -> int:
            # Each node value already contains itself and the best of
            # its left and right paths. We try for each node to add its
            # other branch that is not included in the value (should it
            # exist and be positive) and return the best value of this
            # among all nodes.
            non_null_children = [
                child for child in [node.left, node.right] if child is not None
            ]

            best_path_with_node = node.val

            if len(non_null_children) == 2:
                best_path_with_node += max(0, min(node.left.val, node.right.val))

            if non_null_children:
                return max(
                    best_path_with_node,
                    *[get_maximum_path_sum(child) for child in non_null_children]
                )

            return best_path_with_node

        if root is None:
            return 0

        replace_value_with_best_path_sum(root)

        return get_maximum_path_sum(root)


# @leet end
