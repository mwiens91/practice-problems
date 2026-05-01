# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        smaller, larger = (p, q) if p.val < q.val else (q, p)

        while not smaller.val <= root.val <= larger.val:
            root = root.left if root.val > larger.val else root.right

        return root


# @leet end
