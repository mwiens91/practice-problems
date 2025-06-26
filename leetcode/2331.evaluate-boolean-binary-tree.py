# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        def evaluate_tree(node: TreeNode) -> bool:
            match node.val:
                case 0 | 1:
                    return bool(node.val)
                case 2:
                    return evaluate_tree(node.left) or evaluate_tree(node.right)
                case _:
                    # 3
                    return evaluate_tree(node.left) and evaluate_tree(node.right)

        return evaluate_tree(root)


# @leet end
