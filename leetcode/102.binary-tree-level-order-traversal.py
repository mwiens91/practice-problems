# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        level = [root]
        res: list[list[int]] = []

        while level:
            level_values: list[int] = []
            next_level: list[TreeNode | None] = []

            for node in level:
                if not node:
                    continue

                level_values.append(node.val)
                next_level.extend([node.left, node.right])

            if level_values:
                res.append(level_values)

            level = next_level

        return res


# @leet end
