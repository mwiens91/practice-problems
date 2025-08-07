# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        candidate_vals: list[int] = []
        nodes_to_visit = [root]

        while nodes_to_visit:
            node = nodes_to_visit.pop()

            if node is None:
                continue

            if node.val > root.val:
                candidate_vals.append(node.val)
            else:
                nodes_to_visit.extend([node.left, node.right])

        return min(candidate_vals, default=-1)


# @leet end
