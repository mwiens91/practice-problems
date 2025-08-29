# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        # Find root of trimmed BST
        while root is not None and not low <= root.val <= high:
            while root is not None and root.val < low:
                root = root.right

            while root is not None and root.val > high:
                root = root.left

        def trim_subtree(node: TreeNode | None) -> None:
            if node is None:
                return

            while node.left is not None and node.left.val < low:
                node.left = node.left.right

            while node.right is not None and node.right.val > high:
                node.right = node.right.left

            trim_subtree(node.left)
            trim_subtree(node.right)

        trim_subtree(root)

        return root


# @leet end
