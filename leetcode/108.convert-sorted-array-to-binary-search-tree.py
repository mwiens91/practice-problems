# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # Left and right indices are the inclusive indices used to build
        # a (sub)tree
        def make_balanced_bst_recursive(
            left_idx: int, right_idx: int
        ) -> TreeNode | None:
            if left_idx > right_idx:
                return None

            mid_idx = (left_idx + right_idx) // 2

            return TreeNode(
                val=nums[mid_idx],
                left=make_balanced_bst_recursive(
                    left_idx,
                    mid_idx - 1,
                ),
                right=make_balanced_bst_recursive(
                    mid_idx + 1,
                    right_idx,
                ),
            )

        return make_balanced_bst_recursive(0, len(nums) - 1)


# @leet end
