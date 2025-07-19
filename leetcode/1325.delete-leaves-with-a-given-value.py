# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        # This function returns True if we should replace the node we
        # call it on with None, which the parent caller does
        def should_replace_node(node: TreeNode | None) -> bool:
            if node is None:
                return True

            if should_replace_node(node.left):
                node.left = None

            if should_replace_node(node.right):
                node.right = None

            if node.val == target and node.left is None and node.right is None:
                return True

            return False

        return None if should_replace_node(root) else root


# @leet end
