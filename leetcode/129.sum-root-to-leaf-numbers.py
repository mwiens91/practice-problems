# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: ListNode | None) -> int:
        # Idea, do a depth first search and add each root to leaf number
        # to the total sum
        total_sum = 0

        def recurse(node: ListNode, num_str: str) -> None:
            nonlocal total_sum

            # Base case: at a leaf
            if node.left is None and node.right is None:
                total_sum += int(num_str + str(node.val))

                return

            # Add current value to num string and recurse
            num_str += str(node.val)

            for child in (node.left, node.right):
                if child is not None:
                    recurse(child, num_str)

        recurse(root, "")

        return total_sum


# @leet end
