# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        stack = [root]

        # We're going to get results in the order
        #
        # node -> right -> left
        #
        # We convert this to a postorder traversal by reversing these
        # results
        #
        # left -> right -> node
        while stack:
            current_node = stack.pop()

            # Skip over null nodes
            if current_node is None:
                continue

            # Push children to stack so that we process right before
            # left
            stack.extend([current_node.left, current_node.right])

            # Add this node's value to the result
            result.append(current_node.val)

        result.reverse()
        return result


# @leet end
