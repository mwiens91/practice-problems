# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Add to the result in the recursive function
        result = []

        # Recall: inorder traversal means that for a node we visit the
        # left subtree first, then the node itself, then the right
        # subtree
        def recurse(node: TreeNode | None) -> None:
            # Traverse left subtree
            if node.left is not None:
                recurse(node.left)

            # Add our value to the results
            result.append(node.val)

            # Traverse right subtree
            if node.right is not None:
                recurse(node.right)

        # Recurse on root
        if root is not None:
            recurse(root)

        return result


# @leet end
