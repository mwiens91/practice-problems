# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections.abc import Iterator


class Solution:
    def getAllElements(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> list[int]:
        result: list[int] = []

        def get_bst_iterator(root: TreeNode | None) -> Iterator[int]:
            current = root
            stack: list[TreeNode] = []

            while current is not None or stack:
                while current is not None:
                    stack.append(current)
                    current = current.left

                current = stack.pop()
                yield current.val

                current = current.right

        # NOTE: We could just heapq.merge here but I want to do this
        # manually
        it1 = get_bst_iterator(root1)
        it2 = get_bst_iterator(root2)

        current_1 = next(it1, None)
        current_2 = next(it2, None)

        while current_1 is not None or current_2 is not None:
            if current_2 is None or (current_1 is not None and current_1 <= current_2):
                result.append(current_1)
                current_1 = next(it1, None)
            else:
                result.append(current_2)
                current_2 = next(it2, None)

        return result


# @leet end
