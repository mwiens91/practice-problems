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
        # Get the integer result
        result = 0

        for list_node in [l1, l2]:
            ten_exponent = 0

            while list_node:
                result += list_node.val * 10**ten_exponent

                ten_exponent += 1
                list_node = list_node.next

        # Put the result in a linked list
        result_list_head = ListNode(result % 10)
        result_list_tail = result_list_head

        result //= 10

        while result:
            result_list_tail.next = ListNode(result % 10)

            result_list_tail = result_list_tail.next
            result //= 10

        return result_list_head


# @leet end
