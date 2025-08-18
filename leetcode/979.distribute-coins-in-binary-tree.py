# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        # NOTE: Needed ChatGPT for a hint

        # For each node define its balance to be
        #
        # balance(node)
        # = node.val + balance(node.left) + balance(node.right) - 1
        #
        # where balance(null) = 0.
        #
        # For each node and each immediate child we need to move
        # |balance(child)| coins along the edge between them. We sum up
        # all of these moves to obtain the result.

        # Define function to return the balance of a given node and the
        # total number of moves required in its subtree.
        def balance(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return (0, 0)

            left_balance, left_moves = balance(node.left)
            right_balance, right_moves = balance(node.right)

            this_balance = node.val + left_balance + right_balance - 1
            total_moves = (
                left_moves + right_moves + abs(left_balance) + abs(right_balance)
            )

            return (this_balance, total_moves)

        return balance(root)[1]


# @leet end
