# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1, head)
        tail = head

        while tail and tail.next:
            if tail.val <= tail.next.val:
                tail = tail.next
            else:
                # Insert
                curr = dummy

                while curr.next.val < tail.next.val:
                    curr = curr.next

                temp = tail.next
                tail.next = tail.next.next

                temp.next = curr.next
                curr.next = temp

        return dummy.next


# @leet end
