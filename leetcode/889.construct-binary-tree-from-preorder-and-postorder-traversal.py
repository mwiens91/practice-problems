# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        post_idxs = {k: i for i, k in enumerate(postorder)}

        def build(
            pre_left: int, pre_right, post_left: int, post_right: int
        ) -> TreeNode | None:
            if pre_left > pre_right:
                return None

            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])

            left_post_root = post_idxs[preorder[pre_left + 1]]
            k = left_post_root - post_left + 1

            return TreeNode(
                preorder[pre_left],
                build(pre_left + 1, pre_left + k, post_left, left_post_root),
                build(pre_left + 1 + k, pre_right, left_post_root + 1, post_right - 1),
            )

        return build(0, len(preorder) - 1, 0, len(preorder) - 1)


# @leet end
