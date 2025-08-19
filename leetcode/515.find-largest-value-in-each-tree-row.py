# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        max_per_row: list[int] = []
        stack = [(root, 0)]  # (node, depth)

        # In this loop we will either revisit depths or visit a new
        # depth exactly one depth deeper than the deepest previously
        # visited depth
        while stack:
            node, depth = stack.pop()

            if node is None:
                continue

            stack.extend([(node.left, depth + 1), (node.right, depth + 1)])

            if depth < len(max_per_row):
                max_per_row[depth] = max(max_per_row[depth], node.val)
            else:
                max_per_row.append(node.val)

        return max_per_row


# @leet end
