# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        # Get the depth of the subtree rooted at a node. Also assert
        # along the way that each node is balanced. For the case of
        # comparing depths, we take null nodes as having a depth of -1.
        def get_subtree_depth_rooted_at_node(node: TreeNode | None) -> int:
            # Base cases: null node
            if node is None:
                return -1

            # Get depths of left and right subtrees
            left_subtree_depth = get_subtree_depth_rooted_at_node(node.left)
            right_subtree_depth = get_subtree_depth_rooted_at_node(node.right)

            # Assert left and right subtrees balanced
            assert abs(left_subtree_depth - right_subtree_depth) <= 1

            # Return the depth of this subtree
            return 1 + max(left_subtree_depth, right_subtree_depth)

        # If there's no assertion error when running above function on
        # root, it's balanced, otherwise it isn't.
        try:
            get_subtree_depth_rooted_at_node(root)
        except AssertionError:
            return False

        return True

# @leet end
