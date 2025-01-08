# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        # We'll do a memoized solution. The None initialized in the
        # dictionary is for handling a possible null root.
        memo: dict[TreeNode | None, int] = {None: 0}

        def get_max_money(node: TreeNode) -> int:
            # Try getting memoized solution
            if node in memo:
                return memo[node]

            # Get children and grandchildren
            children = [child for child in [node.left, node.right] if child is not None]
            grandchildren = []

            for child in children:
                grandchildren += [
                    grandchild
                    for grandchild in [child.left, child.right]
                    if grandchild is not None
                ]

            # Get the maximum of stealing from this house and moving
            # directly to grandchildren, or not stealing from this house
            # and moving to children
            maximum_amount = max(
                node.val
                + sum(get_max_money(grandchild) for grandchild in grandchildren),
                sum(get_max_money(child) for child in children),
            )

            memo[node] = maximum_amount

            return maximum_amount

        return get_max_money(root)


# @leet end
