# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder_generator(root: TreeNode | None) -> Generator[TreeNode, None, None]:
    current = root
    stack: list[TreeNode] = []

    while current is not None or stack:
        # Go down left as much as possible until we hit None
        while current is not None:
            stack.append(current)
            current = current.left

        # Pop the next smallest value node
        current = stack.pop()

        yield current

        # Traverse its right branch on the next iteration if it has one;
        # otherwise, we pop the nearest ancestor of this node we haven't
        # yet processed on the next iteration
        current = current.right


class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.gen = inorder_generator(root)
        self.gen_exhausted = False
        self.next_node: TreeNode | None = None

        self.cycle_in_next()

    def cycle_in_next(self) -> None:
        if not self.gen_exhausted:
            try:
                self.next_node = next(self.gen)
            except StopIteration:
                self.gen_exhausted = True

    def next(self) -> int:
        return_val = self.next_node.val
        self.cycle_in_next()

        return return_val

    def hasNext(self) -> bool:
        return not self.gen_exhausted


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @leet end
