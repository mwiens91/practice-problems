# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # Get out if head is null
        if head is None:
            return head

        # Find length of the list, we'll have tail point to the last
        # non-null element and use it later in this solution
        tail = head
        n = 1

        while tail.next is not None:
            tail = tail.next
            n += 1

        # Reassign k to its "effective k": k = a*n + b for some
        # non-negative integers a and b, b < n. We should remove the a*n
        # rotations since those just rotate the list back to its
        # original order
        k %= n

        # If k is now zero then we can return the original head now.
        # This allows us to have simpler logic below, too.
        if k == 0:
            return head

        # The n - k + 1th node will be our new head. First get the node
        # prior to the new head
        prior_node = head

        for _ in range(n - k - 1):
            prior_node = prior_node.next

        # Now sever the link connecting the node prior to new head and
        # the new head
        new_head = prior_node.next
        prior_node.next = None

        # Append the original head to the tail
        tail.next = head

        return new_head


# @leet end
