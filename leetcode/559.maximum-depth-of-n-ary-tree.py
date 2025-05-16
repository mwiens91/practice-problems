# @leet start
# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        # The contraints indicate root could possibly be None, even
        # though the typing the problem template came with contradicts
        # that. Test for it to be safe.
        if root is None:
            return 0

        def get_max_depth(node: Node) -> int:
            # If node.children is None or empty, the current node's depth (1)
            if not node.children:
                return 1

            return 1 + max(map(get_max_depth, node.children))

        return get_max_depth(root)


# @leet end
