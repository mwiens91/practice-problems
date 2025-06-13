# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        stack = [root]

        while stack:
            current_node = stack.pop()

            # Skip over null nodes
            if current_node is None:
                continue

            # Push children to stack so that we process left before
            # right
            stack.extend([current_node.right, current_node.left])

            # Add this node's value to the result
            result.append(current_node.val)

        return result


# @leet end
