# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if root is None:
            return []

        levels_list: list[list[int]] = []

        # Add level values from left to right
        def add_level_values(node: 'Node', level: int) -> None:
            # The logic below works because when we visit a level, it's
            # guaranteed we've processed a value of the previous level
            if level + 1 > len(levels_list):
                levels_list.append([node.val])
            else:
                levels_list[level].append(node.val)

            # Recurse into children
            if node.children is None:
                return

            for child in node.children:
                add_level_values(child, level + 1)

        add_level_values(root, 0)

        return levels_list


# @leet end
