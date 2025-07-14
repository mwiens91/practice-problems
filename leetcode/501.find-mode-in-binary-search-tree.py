# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        # Use inorder traversal to find the modes
        current_val: int | None = None
        current_freq = 0

        highest_freq = 0
        modes: list[int] = []

        node = root
        stack: list[TreeNode] = []

        while node is not None or stack:
            # Left tree
            while node is not None:
                stack.append(node)
                node = node.left

            # Middle node: update current frequency and modes
            node = stack.pop()

            if node.val == current_val:
                current_freq += 1
            else:
                current_val = node.val
                current_freq = 1

            if current_freq == highest_freq:
                modes.append(node.val)
            elif current_freq > highest_freq:
                modes = [node.val]
                highest_freq = current_freq

            # Right tree
            node = node.right

        return modes


# @leet end
