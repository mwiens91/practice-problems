# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        # Prune and return whether one is in the subtree
        def prune_subtree(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return None

            node.left = prune_subtree(node.left)
            node.right = prune_subtree(node.right)

            return (
                node
                if node.left is not None or node.right is not None or node.val == 1
                else None
            )

        return prune_subtree(root)


# @leet end
