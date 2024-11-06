# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        # Deal with edge case of null head
        if head is None:
            return False

        # Idea: use two pointers, i and j. i moves 2 nodes each
        # iteration, j moves 1. If there is a cycle, i and j will meet;
        # else, i will reach None and we terminate. We start with i != j
        # so we can use this condition in the loop to check for a cycle.
        i = head.next
        j = head

        while True:
            # Test for end
            if i is None:
                return False

            # Test for cycle
            if i == j:
                return True

            # Move i two nodes up
            i = i.next

            if i is None:
                return False

            i = i.next

            # Move j one node up
            j = j.next


# @leet end
