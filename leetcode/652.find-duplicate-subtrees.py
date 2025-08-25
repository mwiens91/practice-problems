# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        # Give each subtree a unique ID, mark down that this node
        # corresponds to that ID and return the ID
        id_dict: dict[tuple[int, int, int], int] = {}
        id_counter = 1
        id_to_subtrees: defaultdict[int, list[TreeNode]] = defaultdict(list)

        def get_subtree_id(node: TreeNode | None) -> int:
            nonlocal id_counter

            if node is None:
                return 0

            left = get_subtree_id(node.left)
            right = get_subtree_id(node.right)

            combo = (node.val, left, right)

            if combo not in id_dict:
                # Give this combo the next unused ID
                id_dict[combo] = id_counter
                id_counter += 1

            id = id_dict[combo]
            id_to_subtrees[id].append(node)

            return id

        get_subtree_id(root)

        return [nodes[0] for nodes in id_to_subtrees.values() if len(nodes) > 1]


# @leet end
