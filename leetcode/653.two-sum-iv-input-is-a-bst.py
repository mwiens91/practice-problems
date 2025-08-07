# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        # NOTE: The real way to do this optimally is to use the
        # property that in-order traversal of a BST yields
        # values in sorted order. So we'd have two pointers and
        # set up a forward and reverse in-order iterator and
        # then do the usual two-pointer two-sum
        # approach. However, I'm not down to write a reverse
        # in-order iterator for this problem right now, so I'm
        # not going to do that. Instead, I'll use the second
        # most efficient approach, which doesn't make use of the
        # BST property at all.
        seen: set[int] = set()

        to_visit = [root]

        while to_visit:
            node = to_visit.pop()

            if node is None:
                continue

            if k - node.val in seen:
                return True

            seen.add(node.val)
            to_visit.extend([node.left, node.right])

        return False


# @leet end
