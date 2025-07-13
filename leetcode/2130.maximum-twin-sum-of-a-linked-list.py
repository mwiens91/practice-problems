# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        # Get a pointer to the second half of the list
        second_half = head
        temp = head

        while temp is not None:
            temp = temp.next.next
            second_half = second_half.next

        # Reverse the second half of the list
        prev = None

        while second_half is not None:
            temp = second_half.next

            second_half.next = prev
            prev = second_half
            second_half = temp

        second_half = prev

        # Now find the largest twin sum
        max_twin_sum = 0

        while second_half is not None:
            max_twin_sum = max(max_twin_sum, head.val + second_half.val)

            head = head.next
            second_half = second_half.next

        return max_twin_sum


# @leet end
