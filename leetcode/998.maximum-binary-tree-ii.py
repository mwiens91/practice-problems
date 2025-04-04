# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # From the given tree, get the list it was constructed from
        nums = []

        def build_original_nums(node: TreeNode | None) -> None:
            if node is None:
                return

            # Get the nums with an inorder traversal
            build_original_nums(node.left)

            nums.append(node.val)

            build_original_nums(node.right)

        build_original_nums(root)

        # Append the passed in value to the list and construct a new
        # tree using my solution to LC 654
        nums.append(val)

        def construct_max_binary_tree(start_idx: int, end_idx: int) -> TreeNode | None:
            if start_idx >= end_idx:
                return None

            max_idx = start_idx
            max_val = nums[start_idx]

            for i in range(start_idx + 1, end_idx):
                if nums[i] > max_val:
                    max_idx = i
                    max_val = nums[i]

            return TreeNode(
                val=max_val,
                left=construct_max_binary_tree(start_idx, max_idx),
                right=construct_max_binary_tree(max_idx + 1, end_idx),
            )

        return construct_max_binary_tree(0, len(nums))


# @leet end
