# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode | None] = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node is None:
                continue

            # If we encounter a new depth it will always be
            # one deeper than the previous max depth
            if depth >= len(result):
                result.append(node.val)

            stack.extend([(node.left, depth + 1), (node.right, depth + 1)])

        return result


# @leet end
