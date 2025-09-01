# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
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

        # Get maximum distance from start node
        visited = {start}

        def get_max_distance(node: int) -> int:
            max_distance = 0

            for adj_node in [adj for adj in edges[node] if adj not in visited]:
                if adj_node not in visited:
                    visited.add(adj_node)
                    max_distance = max(max_distance, 1 + get_max_distance(adj_node))

            return max_distance

        return get_max_distance(start)


# @leet end
