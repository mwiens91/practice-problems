# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first: TreeNode | None = None
        second: TreeNode | None = None

        stack: list[TreeNode] = []
        prev: TreeNode | None = None
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                    second = curr
                else:
                    second = curr
                    break

            prev = curr
            curr = curr.right

        first.val, second.val = second.val, first.val

        return root


# @leet end
