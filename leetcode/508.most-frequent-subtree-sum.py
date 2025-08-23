# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        subtree_sum_freqs: defaultdict[int, int] = defaultdict(int)

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0

            subtree_sum = node.val + dfs(node.left) + dfs(node.right)
            subtree_sum_freqs[subtree_sum] += 1

            return subtree_sum

        dfs(root)

        max_freq = max(subtree_sum_freqs.values())

        return [
            subtree_sum
            for subtree_sum, freq in subtree_sum_freqs.items()
            if freq == max_freq
        ]


# @leet end
