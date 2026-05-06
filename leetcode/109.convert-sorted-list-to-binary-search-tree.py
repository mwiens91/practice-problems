# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        curr = head

        def build(length: int) -> TreeNode | None:
            nonlocal curr

            if length == 0:
                return None

            left_length = length // 2
            left = build(left_length)

            root = TreeNode(curr.val)
            curr = curr.next

            right = build(length - left_length - 1)

            root.left = left
            root.right = right

            return root

        return build(n)


# @leet end
