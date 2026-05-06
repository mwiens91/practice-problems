# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        level = [root] if root else []
        level_sum = -root.val if root else -1

        while level:
            next_level: list[TreeNode] = []
            next_level_sum = 0

            for node in level:
                node.val += level_sum

                children = [nd for nd in (node.left, node.right) if nd]
                children_sum = sum(nd.val for nd in children)
                next_level_sum += children_sum

                for nd in children:
                    nd.val = -children_sum

                next_level.extend(children)

            level = next_level
            level_sum = next_level_sum

        return root


# @leet end
