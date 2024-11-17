# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: ListNode | None) -> int:
        # First handle edge case of null root
        if root is None:
            return 0

        # Next determine the depth of the tree
        depth = -1
        node = root

        while node is not None:
            depth += 1
            node = node.left

        # Next define a function to test if the nth node (0-indexed) of the
        # last level of the tree is null. We'll assume that 0 < n < 2^depth - 1.
        def nth_node_is_null(n: int) -> bool:
            # Get the node. There's a way to determine when to go left
            # or right down the tree by using the binary representation
            # of the node number (not n!). Suppose the depth of the tree
            # is 3 and we want to get to node 9. The binary
            # representation of 9 is 1001. Looking at the last three
            # digits 001, if we interpret 0 as "go left" and 1 as "go
            # right", then these digits tell us to go left twice and
            # then go right once, which takes us to the right node.
            LEFT = "0"

            # The node number is determined by adding to the number of
            # nodes in the previous levels (i.e., 2**depth - 1) the
            # 1-indexed position of the node in the last level (i.e, n +
            # 1).
            node_number = 2**depth + n

            # Get the directions to take. A depth of 0 causes the
            # [-depth:] slice to be equivalent to [0:], which is not
            # what we want, so we handle the 0-case separately.
            if depth > 0:
                directions = list(bin(node_number)[-depth:])
            else:
                directions = []

            # Get the node
            node = root

            for direction in directions:
                if direction == LEFT:
                    node = node.left
                else:
                    node = node.right

            # Return whether the node is null
            if node is None:
                return True

            return False

        # Now do a binary search to find the first null node of the last
        # level, where we label the nodes
        # 0, 1, 2, ... , n, ... , 2^depth - 1. The algorithm terminates
        # at with start pointing to the index of the first null node,
        # which is also the number of nodes in the last level (because
        # of 0-indexing).
        start = 0
        end = 2**depth - 1

        while start < end:
            mid = (start + end) // 2

            if nth_node_is_null(mid):
                end = mid
            else:
                start = mid + 1

        # In the case of all non-null nodes the algorithm terminates
        # with start pointing to the last index, so we need to check for
        # this separately.
        num_last_level_nodes = start

        if not nth_node_is_null(start):
            num_last_level_nodes += 1

        return 2**depth - 1 + num_last_level_nodes


# @leet end
