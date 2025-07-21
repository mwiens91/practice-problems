# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        node_dict: dict[int, TreeNode] = {}
        parent_ids_seen: set[int] = set()
        child_ids_seen: set[int] = set()

        for parent_id, child_id, is_left in descriptions:
            parent_ids_seen.add(parent_id)
            child_ids_seen.add(child_id)

            if parent_id not in node_dict:
                node_dict[parent_id] = TreeNode(parent_id)

            if child_id not in node_dict:
                node_dict[child_id] = TreeNode(child_id)

            # Add the child
            if is_left:
                node_dict[parent_id].left = node_dict[child_id]
            else:
                node_dict[parent_id].right = node_dict[child_id]

        # The root node ID is the only node which is listed as a parent
        # and never as a child
        return node_dict[next(iter(parent_ids_seen - child_ids_seen))]


# @leet end
