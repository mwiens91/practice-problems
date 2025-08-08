# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        # Recall that in-order traversal of a BST yields sorted
        # order. Here we're going to do reverse sorted order.
        current = root
        stack: list[TreeNode] = []
        prev_val = 0

        while current is not None or stack:
            # Go right
            while current is not None:
                stack.append(current)
                current = current.right

            # Process next
            current = stack.pop()
            current.val += prev_val
            prev_val = current.val

            # Go left
            current = current.left

        return root


# @leet end
