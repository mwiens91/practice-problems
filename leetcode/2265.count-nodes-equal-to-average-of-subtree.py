# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Return a three-tuple containing
        # - the number of nodes in the subtree equal to their respective
        # subtree's average
        # - the number of nodes in the subtree
        # - the sum of node values in the subtree
        def recurse(node: TreeNode | None) -> tuple[int, int, int]:
            if node is None:
                return (0, 0, 0)

            left_equal, left_n, left_sum = recurse(node.left)
            right_equal, right_n, right_sum = recurse(node.right)

            this_n = left_n + right_n + 1
            this_sum = left_sum + right_sum + node.val
            this_equal = (
                left_equal + right_equal + (1 if node.val == this_sum // this_n else 0)
            )

            return (this_equal, this_n, this_sum)

        return recurse(root)[0]


# @leet end
