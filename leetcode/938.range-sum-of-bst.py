# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        def get_subtree_range_sum(node: TreeNode | None) -> int:
            # Null node
            if node is None:
                return 0

            # Node val not in range
            if node.val > high:
                return get_subtree_range_sum(node.left)

            if node.val < low:
                return get_subtree_range_sum(node.right)

            # Node val in range
            result = node.val

            if node.val != low:
                result += get_subtree_range_sum(node.left)

            if node.val != high:
                result += get_subtree_range_sum(node.right)

            return result

        return get_subtree_range_sum(root)


# @leet end
