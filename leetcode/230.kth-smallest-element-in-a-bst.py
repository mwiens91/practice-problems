# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # In-order traversal goes in sorted order for a BST
        count = 0
        stack: list[TreeNode] = []
        current = root

        while True:
            # Go left
            while current is not None:
                stack.append(current)
                current = current.left

            # Process next node in-order
            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            # Go right
            current = current.right


# @leet end
