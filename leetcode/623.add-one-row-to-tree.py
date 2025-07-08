# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        # Deal with edge case
        if depth == 1:
            return TreeNode(val=val, left=root)

        # We'll iterate through nodes in a queue containing two-tuples
        # of the node and it's depth.
        queue: deque[tuple[TreeNode | None, int]] = deque([(root, 1)])

        while queue:
            node, node_depth = queue.popleft()

            if node is None:
                continue

            if node_depth < depth - 1:
                queue.extend(
                    [(node.left, node_depth + 1), (node.right, node_depth + 1)]
                )
            else:
                # Place new nodes
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)

        return root


# @leet end
