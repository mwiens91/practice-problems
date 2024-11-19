# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # Deal with n == 1 separately so we don't have to complicate the
        # below logic
        if head.next is None:
            return True

        # We're going to an O(1) memory, O(n) time solution that
        # modifies the input. First we'll find either the middle node
        # (for an odd length linked list) or the "right-middle" node
        # (for an even length linked list).
        slow_ptr = head
        fast_ptr = head

        n = 0

        while fast_ptr is not None:
            # Move up the fast pointer twice and the slow pointer once
            # per iteration until we can't move the fast pointer twice
            fast_ptr = fast_ptr.next
            n += 1

            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
                n += 1
            else:
                break

            slow_ptr = slow_ptr.next

        # Now, using the middle node, we're going to want the node to
        # the right of the middle for n odd, or the "right-middle" for n
        # even. We'll use this after the next step.
        right_middle_ptr = slow_ptr

        if n % 2:
            # Odd length
            right_middle_ptr = right_middle_ptr.next

        # Next, we're going to reverse the first n // 2 elements
        prev_node = None
        node = head
        next_node = head.next

        # We want to point the next member backwards n // 2 times
        # exactly. We'll do it once here and n // 2 - 1 times in the
        # loop below.
        node.next = prev_node

        for _ in range(n // 2 - 1):
            # Set up for next swap
            prev_node = node
            node = next_node
            next_node = next_node.next

            # Swap node
            node.next = prev_node

        # Node now points to the left of the middle for n odd or to the
        # "left-middle" for n even (with a reversed sub-list)
        left_middle_ptr = node

        # Now we have two pointers at the middle with lists that point
        # outwards (wrt to the original list), so all we need to do is
        # move along on both and compare values
        while left_middle_ptr is not None:
            # Compare
            if left_middle_ptr.val != right_middle_ptr.val:
                return False

            # Set up for next iteration
            left_middle_ptr = left_middle_ptr.next
            right_middle_ptr = right_middle_ptr.next

        return True


# @leet end
