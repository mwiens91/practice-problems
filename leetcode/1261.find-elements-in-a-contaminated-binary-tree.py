# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode | None):
        self.elements: set[int] = set()
        self.extract_elements(root)

    def extract_elements(self, node: TreeNode | None, val: int = 0) -> None:
        if node is None:
            return

        self.elements.add(val)

        self.extract_elements(node.left, 2 * val + 1)
        self.extract_elements(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @leet end
