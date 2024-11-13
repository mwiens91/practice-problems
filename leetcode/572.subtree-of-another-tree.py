# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # Not sure if there's an optimization here, but we're going to
        # traverse from the root and for each node look if it's the
        # subroot of the subtree.
        def is_subroot(
            tree_node: TreeNode | None, subtree_node: TreeNode | None = subRoot
        ) -> bool:
            # If both are None we're good
            if tree_node is None and subtree_node is None:
                return True

            # Now check that the vals match, wrap it in a try in case
            # one of the nodes is None
            try:
                if tree_node.val != subtree_node.val:
                    # Not the same
                    return False
            except AttributeError:
                # One was None, the other wasn't
                return False

            # Now look at left and right subtrees
            if is_subroot(tree_node.left, subtree_node.left) and is_subroot(
                tree_node.right, subtree_node.right
            ):
                # Both subtrees are the same
                return True

            # Subtrees not the same
            return False

        # Now traverse the tree
        stack = [root]

        while stack:
            node = stack.pop()

            if is_subroot(node):
                return True

            if node is not None:
                stack += [node.left, node.right]

        # No luck
        return False


# @leet end
