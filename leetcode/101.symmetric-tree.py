# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: ListNode | None) -> bool:
        # Push left and right children to two stacks and compare them
        left_stack = [root]
        right_stack = [root]

        while left_stack:
            left = left_stack.pop()
            right = right_stack.pop()

            if left is None and right is None:
                continue

            try:
                assert left.val == right.val
            except (AttributeError, AssertionError):
                return False

            # Add to stacks
            left_stack += [left.left, left.right]
            right_stack += [right.right, right.left]

        return True


# @leet end
