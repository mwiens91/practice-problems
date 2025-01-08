# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            # Get nodes
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            # Make sure they're the same
            if p_node is None and q_node is None:
                continue

            try:
                assert p_node.val == q_node.val
            except (AttributeError, AssertionError):
                # Note: AttributeError comes up with exactly one of
                # p_node and q_node is None
                return False

            # Push children to the stack
            p_stack += [p_node.left, p_node.right]
            q_stack += [q_node.left, q_node.right]

        return True


# @leet end
