# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        original_stack = [original]
        cloned_stack = [cloned]

        # Go through nodes until we find target in the original tree,
        # and then return the corresponding node in the cloned tree.
        while True:
            original_node = original_stack.pop()
            cloned_node = cloned_stack.pop()

            if original_node is None:
                continue

            if original_node == target:
                return cloned_node

            original_stack.extend([original_node.left, original_node.right])
            cloned_stack.extend([cloned_node.left, cloned_node.right])


# @leet end
