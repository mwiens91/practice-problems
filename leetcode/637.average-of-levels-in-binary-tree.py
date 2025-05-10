# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import statistics


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        # For each level of the tree, put all values into a list
        level_values: list[list[int]] = []

        def collect_values(node: TreeNode | None, level: int = 0) -> None:
            if node is None:
                return

            # Collect the value
            try:
                level_values[level].append(node.val)
            except IndexError:
                # Don't have any values of this level yet. Append a new
                # list with this value. We go through levels in order,
                # so the index of the list we are appending will always
                # be correct.
                level_values.append([node.val])

            # Visit children
            collect_values(node.left, level + 1)
            collect_values(node.right, level + 1)

        collect_values(root)

        return list(map(statistics.fmean, level_values))


# @leet end
