# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result: list[list[int]] = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node is None:
                continue

            if len(result) > depth:
                result[depth].append(node.val)
            else:
                # This is okay because if we visit a new depth it's
                # guaranteed to be exactly one deeper than the
                # previously visited depth
                result.append([node.val])

            stack.extend([(node.right, depth + 1), (node.left, depth + 1)])

        return result


# @leet end
