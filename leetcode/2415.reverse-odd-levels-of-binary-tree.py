# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        current_level = 0

        nodes_in_current_level = [root]

        while nodes_in_current_level[0] is not None:
            # If current level is odd, reverse all values in this level
            if current_level % 2 == 1:
                new_values = [node.val for node in reversed(nodes_in_current_level)]

                for node, new_value in zip(nodes_in_current_level, new_values):
                    node.val = new_value

            # Get nodes for next level
            nodes_in_next_level = []

            for node in nodes_in_current_level:
                nodes_in_next_level += [node.left, node.right]

            # Set up for next iteration
            nodes_in_current_level = nodes_in_next_level
            current_level += 1

        return root


# @leet end
