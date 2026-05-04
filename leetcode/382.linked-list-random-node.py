# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random


class Solution:

    def __init__(self, head: ListNode | None):
        self.vals: list[int] = []

        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @leet end
