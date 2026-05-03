# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        in_idx_map = {k: i for i, k in enumerate(inorder)}

        def helper(
            pre_root_idx: int, in_left_idx: int, in_right_idx: int
        ) -> TreeNode | None:
            if in_left_idx > in_right_idx:
                return None

            val = preorder[pre_root_idx]
            in_root_idx = in_idx_map[val]
            k = in_root_idx - in_left_idx  # k = left tree size

            return TreeNode(
                val,
                helper(pre_root_idx + 1, in_left_idx, in_root_idx - 1),
                helper(pre_root_idx + k + 1, in_root_idx + 1, in_right_idx),
            )

        return helper(0, 0, len(inorder) - 1)


# @leet end
