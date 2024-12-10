# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: ListNode | None, targetSum: int) -> list[list[int]]:
        # Store answers here
        answers = []

        # Use a recursive function to find all path sums
        def recurse(node, current_path, current_sum) -> None:
            # Add to path and sum
            current_path = current_path + [node.val]
            current_sum += node.val

            # Base case: we're at a leaf
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    answers.append(current_path)

                return

            # Recurse: visit non-null children
            for child in [node.left, node.right]:
                if child is not None:
                    recurse(child, current_path, current_sum)

        # Handle edge case of null root
        if root is None:
            return []

        # Recurse
        recurse(root, [], 0)

        return answers


# @leet end
