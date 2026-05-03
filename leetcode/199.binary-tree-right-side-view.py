# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res: list[int] = []
        level: list[TreeNode] = [root] if root else []

        while level:
            res.append(level[-1].val)
            next_level: list[TreeNode] = []

            for node in level:
                for child in (node.left, node.right):
                    if child:
                        next_level.append(child)

            level = next_level

        return res


# @leet end
