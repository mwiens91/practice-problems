# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root or root.val == key:
            return self.remove(root)

        prev: TreeNode | None = None
        curr = root

        while curr and curr.val != key:
            prev = curr
            curr = curr.left if key < curr.val else curr.right

        if prev.left == curr:
            prev.left = self.remove(prev.left)
        else:
            prev.right = self.remove(prev.right)

        return root

    def remove(self, node: TreeNode | None) -> TreeNode | None:
        if not node:
            return None

        if not node.left:
            return node.right

        if not node.right:
            return node.left

        prev = node
        curr = node.left

        while curr and curr.right:
            prev = curr
            curr = curr.right

        node.val = curr.val

        if prev == node:
            prev.left = curr.left
        else:
            prev.right = curr.left

        return node


# @leet end
