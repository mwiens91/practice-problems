# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        # Recurse through the tree and sum up left leaves
        total = 0

        def recurse(node: TreeNode, on_left: bool = False) -> None:
            nonlocal total

            # If we're at a leaf and we're on the left, add the value to
            # the sum
            if node.left is None and node.right is None:
                if on_left:
                    total += node.val

                return

            # Visit children
            if node.left is not None:
                recurse(node.left, True)

            if node.right is not None:
                recurse(node.right, False)

        # Get the total
        if root is not None:
            recurse(root)

        return total


# @leet end
