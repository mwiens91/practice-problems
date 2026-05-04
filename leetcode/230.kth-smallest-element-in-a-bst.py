# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = -1

        def inorder(root: TreeNode | None) -> bool:
            nonlocal k, res

            if not root:
                return False

            if inorder(root.left):
                return True

            k -= 1

            if k == 0:
                res = root.val

                return True

            return inorder(root.right)

        inorder(root)

        return res


# @leet end
