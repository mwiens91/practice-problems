# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        def get_string_repr(node: TreeNode | None) -> str:
            # If node is null, return an empty string
            if node is None:
                return ""

            # Use the string representations from children
            left = (
                f"({get_string_repr(node.left)})"
                if node.left is not None or node.right is not None
                else ""
            )
            right = f"({get_string_repr(node.right)})" if node.right is not None else ""

            return f"{node.val}{left}{right}"

        return get_string_repr(root)


# @leet end
