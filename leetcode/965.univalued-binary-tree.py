# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        # Get the root value and assert that all values in the tree have
        # this value
        try:
            root_val = root.val
        except AttributeError:
            # Root is null
            return True

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                continue

            if node.val != root_val:
                return False

            queue.extend([node.left, node.right])

        return True


# @leet end
