# @leet start


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        # Deal with None in input here rather than complicate below loop
        # logic
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # Invariant for below loop: list1.val <= list2.val
        if list1.val > list2.val:
            list1, list2 = list2, list1

        # Idea here is that we're going to merge list2 things into list1
        answer_head = list1

        while True:
            if list1.next is None:
                # Merge the rest of list2 onto list1
                list1.next = list2

                break

            if list2.val <= list1.next.val:
                # Splice current list2 node into list1's next position
                # while moving forward on list2
                temp = list1.next
                list1.next = list2
                list2 = list2.next
                list1.next.next = temp

                if list2 is None:
                    break
            else:
                # Move forward on list1
                list1 = list1.next

        return answer_head


# @leet end
