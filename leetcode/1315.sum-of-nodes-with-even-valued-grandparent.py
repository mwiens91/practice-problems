# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        def get_sum(
            node: TreeNode | None, grandparent_even: bool, parent_even: bool
        ) -> int:
            if node is None:
                return 0

            is_even = node.val % 2 == 0

            return (node.val if grandparent_even else 0) + sum(
                get_sum(child, parent_even, is_even)
                for child in (node.left, node.right)
            )

        return get_sum(root, False, False)


# @leet end
