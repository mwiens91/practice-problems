# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        n1 = 0

        while l1 is not None:
            n1 = n1 * 10 + l1.val
            l1 = l1.next

        n2 = 0

        while l2 is not None:
            n2 = n2 * 10 + l2.val
            l2 = l2.next

        sum_digits = list(map(int, str(n1 + n2)))

        result_head = ListNode(val=sum_digits[0])
        result_tail = result_head

        for num in sum_digits[1:]:
            result_tail.next = ListNode(val=num)
            result_tail = result_tail.next

        return result_head


# @leet end
