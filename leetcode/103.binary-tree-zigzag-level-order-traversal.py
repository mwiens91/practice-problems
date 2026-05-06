# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res: list[list[int]] = []
        level = [root] if root else []
        left = True

        while level:
            next_level: list[TreeNode] = []

            for node in level:
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            if left:
                res.append([node.val for node in level])
            else:
                res.append([node.val for node in reversed(level)])

            left = not left
            level = next_level

        return res


# @leet end
