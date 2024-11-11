# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        results: list[str] = []

        # Well define a recursive function to travel down all paths and
        # store results in the list above
        def recurse(node: TreeNode | None, path_str: str) -> None:
            # Add current value to the path string
            if node != root:
                path_str += "->"

            path_str += str(node.val)

            # If there are no leafs, add this to the results
            if node.left is None and node.right is None:
                results.append(path_str)

            # Visit any child leafs
            for child in [node.left, node.right]:
                if child is not None:
                    recurse(child, path_str)

        # Travel the paths
        recurse(root, "")

        return results


# @leet end
