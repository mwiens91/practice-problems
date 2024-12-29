# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: ListNode | None) -> ListNode | None:
        # For each node, we'll swap left and right children, starting
        # from the root to the leaves
        def invert_tree(node: ListNode | None) -> None:
            # Get out if null node
            if node is None:
                return

            # Swap left and right children
            node.left, node.right = node.right, node.left

            # Recurse
            invert_tree(node.left)
            invert_tree(node.right)

        invert_tree(root)

        return root


# @leet end
