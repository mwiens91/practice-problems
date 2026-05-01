# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        return self.helper(root)[1]

    # Return height of current and length of longest path seen
    def helper(self, root: TreeNode | None) -> tuple[int, int]:
        if not root:
            return (-1, 0)

        left_height, left_best = self.helper(root.left)
        right_height, right_best = self.helper(root.right)

        this_height = max(left_height, right_height) + 1
        this_best = max(left_best, right_best, left_height + right_height + 2)

        return (this_height, this_best)


# @leet end
