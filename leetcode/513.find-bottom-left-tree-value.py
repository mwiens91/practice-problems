# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        # Stack contains two-tuples (node, depth)
        stack = [(root, 0)]

        result = root.val
        result_depth = 0

        while stack:
            node, depth = stack.pop()

            if node is None:
                continue

            if depth > result_depth:
                result = node.val
                result_depth = depth

            stack.extend([(node.right, depth + 1), (node.left, depth + 1)])

        return result


# @leet end
