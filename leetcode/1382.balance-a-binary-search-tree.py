# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        # NOTE: We can balance the tree in place using rotations, but
        # it's easier just to make a whole new tree

        # Get the sorted values of the tree using in-order traversal
        sorted_vals: list[int] = []

        current = root
        stack: list[TreeNode] = []

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            sorted_vals.append(current.val)

            current = current.right

        # Build a new BST with the same values that is balanced
        def build_balanced_bst(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            mid = (left + right) // 2

            return TreeNode(
                val=sorted_vals[mid],
                left=build_balanced_bst(left, mid - 1),
                right=build_balanced_bst(mid + 1, right),
            )

        return build_balanced_bst(0, len(sorted_vals) - 1)


# @leet end
