# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode | None) -> int:
        def get_tilt_sum_and_subtree_sum(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return (0, 0)

            left_tilt_sum, left_subtree_sum = get_tilt_sum_and_subtree_sum(node.left)
            right_tilt_sum, right_subtree_sum = get_tilt_sum_and_subtree_sum(node.right)

            node_tilt_sum = (
                abs(left_subtree_sum - right_subtree_sum)
                + left_tilt_sum
                + right_tilt_sum
            )
            node_subtree_sum = node.val + left_subtree_sum + right_subtree_sum

            return (node_tilt_sum, node_subtree_sum)

        return get_tilt_sum_and_subtree_sum(root)[0]


# @leet end
