# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        def from_preorder(start: int, end: int) -> TreeNode | None:
            if start > end:
                return None

            node_val = preorder[start]

            # Find where right subtree starts in preorder
            start_right = start + 1

            while start_right <= end and preorder[start_right] < node_val:
                start_right += 1

            return TreeNode(
                node_val,
                from_preorder(start + 1, start_right - 1),
                from_preorder(start_right, end),
            )

        return from_preorder(0, len(preorder) - 1)


# @leet end
