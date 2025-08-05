# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        # In-order traversal on a BST yields sorted order. So we'll
        # build up the new tree using that.
        new_root: TreeNode | None = None
        new_leaf: TreeNode | None = None

        current = root
        stack: list[TreeNode] = []

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            # Pop the next node in order and put it in the new tree
            current = stack.pop()

            if new_root is None:
                new_root = TreeNode(current.val)
                new_leaf = new_root
            else:
                new_leaf.right = TreeNode(current.val)
                new_leaf = new_leaf.right

            current = current.right

        return new_root


# @leet end
