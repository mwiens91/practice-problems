# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        edges: defaultdict[int, list[int]] = defaultdict(list)

        def build_edges(parent: TreeNode | None, child: TreeNode | None) -> None:
            if child is None:
                return

            if parent is not None:
                edges[parent.val].append(child.val)
                edges[child.val].append(parent.val)

            build_edges(child, child.left)
            build_edges(child, child.right)

        build_edges(None, root)

        # Get the node values at distance k from target
        prev: set[int] = set()
        current = {target.val}

        for _ in range(k):
            future: set[int] = set()

            for node in current:
                future.update(adj for adj in edges[node] if adj not in prev)

            prev = current
            current = future

        return list(current)


# @leet end
