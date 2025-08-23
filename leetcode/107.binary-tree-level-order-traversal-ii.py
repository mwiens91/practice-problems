# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        # NOTE: this is just my solution to LC 102, but reversing the
        # list at the end
        result: list[list[int]] = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node is None:
                continue

            if len(result) > depth:
                result[depth].append(node.val)
            else:
                result.append([node.val])

            stack.extend([(node.right, depth + 1), (node.left, depth + 1)])

        return result[::-1]


# @leet end
