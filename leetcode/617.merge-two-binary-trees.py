# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        def merge_subtrees(
            node1: TreeNode | None, node2: TreeNode | None
        ) -> TreeNode | None:
            # Base case: if one of the nodes is None, return the other
            # node (even if it is None)
            if node1 is None:
                return node2

            if node2 is None:
                return node1

            # Merge the node values and recurse on children
            return TreeNode(
                val=node1.val + node2.val,
                left=merge_subtrees(node1.left, node2.left),
                right=merge_subtrees(node1.right, node2.right),
            )

        return merge_subtrees(root1, root2)


# @leet end
