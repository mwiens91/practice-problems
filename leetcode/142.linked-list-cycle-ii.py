# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        # Tortoise and hare algorithm. Use a slow pointer (moving 1 per
        # iteration and a fast pointer moving 2 per iteration).
        try:
            slow = head.next
            fast = head.next.next
        except AttributeError:
            return None

        while slow != fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return None

            if fast is None:
                return None

        # Slow and fast met in the cycle. Start a new pointer from the
        # head. The start of the cycle is where slow meets the new
        # pointer.
        new_slow = head

        while slow != new_slow:
            slow = slow.next
            new_slow = new_slow.next

        return slow


# @leet end
