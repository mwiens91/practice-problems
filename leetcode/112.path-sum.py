# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # We'll do a DFS here using the below function. Keep passing
        # down to children and taking the node's value of the current
        # target. Base case is when we hit None. It's thus true if
        # target is zero, false otherwise.
        def has_path_sum_recurse(node: TreeNode | None, target: int) -> bool:
            # Base case 
            if node is None:
                if target == 0:
                    return True
                else:
                    return False

            # Recurse on children. We cannot terminate at a null child
            # if a non-null child exists: makes the logic a little
            # annoying.
            child_target = target - node.val

            if node.left is not None and node.right is None:
                # Must travel down left
                return has_path_sum_recurse(node.left, child_target)

            if node.left is None and node.right is not None:
                # Must travel down right
                return has_path_sum_recurse(node.right, child_target)

            # Travel down both
            if has_path_sum_recurse(node.left, child_target):
                return True

            return has_path_sum_recurse(node.right, child_target)

        # Empty tree always false
        if root is None:
            return False

        # Recurse from root
        return has_path_sum_recurse(root, targetSum)
# @leet end
