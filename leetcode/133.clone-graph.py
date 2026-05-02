# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None

        val_to_clone = {node.val: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()
            clone = val_to_clone[curr.val]
            clone_neighbors = []

            for adj_node in curr.neighbors:
                if adj_node.val not in val_to_clone:
                    val_to_clone[adj_node.val] = Node(adj_node.val)
                    stack.append(adj_node)

                clone_neighbors.append(val_to_clone[adj_node.val])

            clone.neighbors = clone_neighbors

        return val_to_clone[node.val]


# @leet end
