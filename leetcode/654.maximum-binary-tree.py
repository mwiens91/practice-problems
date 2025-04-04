# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        # Define a function to recursively construct the maximum binary
        # tree given an inclusive start index and exclusive end index of
        # nums
        def construct_max_binary_tree(start_idx: int, end_idx: int) -> TreeNode | None:
            # Base case: no numbers in subarray
            if start_idx >= end_idx:
                return None

            # Find the index of the maximum value
            max_idx = start_idx
            max_val = nums[start_idx]

            for i in range(start_idx + 1, end_idx):
                if nums[i] > max_val:
                    max_idx = i
                    max_val = nums[i]

            # Return the maximum binary tree using the given subarray
            return TreeNode(
                val=max_val,
                left=construct_max_binary_tree(start_idx, max_idx),
                right=construct_max_binary_tree(max_idx + 1, end_idx),
            )

        return construct_max_binary_tree(0, len(nums))


# @leet end
