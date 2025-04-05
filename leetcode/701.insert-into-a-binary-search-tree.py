# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # If the root is null, return a new tree with the value as the
        # root
        if root is None:
            return TreeNode(val)

        # Insert the value in a new leaf node
        node = root

        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)

                    break

                node = node.left
            else:
                # val > node.val
                if node.right is None:
                    node.right = TreeNode(val)

                    break

                node = node.right

        return root


# @leet end
