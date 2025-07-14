# @leet start
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val: int = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        val_to_node_dict: dict[int, Node] = {}
        original_node_stack = [node]
        seen_node_vals = set([node.val])

        def get_or_construct_cloned_node(val: int) -> Node:
            if val not in val_to_node_dict:
                val_to_node_dict[val] = Node(val)

            return val_to_node_dict[val]

        while original_node_stack:
            # Get current node and its clone. The clone may have been
            # constructed already with its value but we need to fill in
            # its neighbour list
            original_node = original_node_stack.pop()
            cloned_node = get_or_construct_cloned_node(original_node.val)

            for original_neighbor in original_node.neighbors:
                cloned_node.neighbors.append(
                    get_or_construct_cloned_node(original_neighbor.val)
                )

                if original_neighbor.val not in seen_node_vals:
                    original_node_stack.append(original_neighbor)
                    seen_node_vals.add(original_neighbor.val)

        return val_to_node_dict[1]


# @leet end
