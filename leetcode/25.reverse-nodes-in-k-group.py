# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # Handle null head edge case, and deal with trivial case of
        # k == 1 (this is actually handled by logic below, but might as
        # well short circuit because we can)
        if k == 1 or head is None:
            return head

        # Get length of list
        length = 1
        node = head

        while node.next is not None:
            node = node.next
            length += 1

        # For each group of k we have the previous elements, the last
        # element of which we'll call prev_end; we also have the next
        # elements after the group of k, the first element of which
        # we'll call next_start (this will be defined in the loop below)
        prev_end = None

        # Go through and reverse nodes in each k group
        first_element = head

        for _ in range(length // k):
            # Point prev_end to the last element of this group. If this
            # is the first iteration (i.e, prev_end is None), set head
            # to point to the last element.
            last_element = first_element

            for _ in range(k - 1):
                last_element = last_element.next

            if prev_end is not None:
                prev_end.next = last_element
            else:
                head = last_element

            # Get the next_start node
            next_start = last_element.next

            # Now reverse the k elements
            prev = next_start
            node = first_element

            for _ in range(k):
                temp = node.next

                # Change next pointer for current node
                node.next = prev

                # Set up for next iteration
                prev = node
                node = temp

            # Set up variables for next group of k
            prev_end = first_element
            first_element = next_start

        return head


# @leet end
