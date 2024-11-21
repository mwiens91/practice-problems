# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Deal with edge cases first: list is empty or the list just has
        # a bunch of null nodes
        if not list or not any(node is not None for node in lists):
            return None

        # We'll use a heap to keep track of the current minimum element
        # available. Heap will store tuples of (value, list_idx).
        heap: list[tuple[int, int]] = []

        # Populate the heap
        for i, node in enumerate(lists):
            if node is not None:
                # Put the value in the heap and move the node along to
                # the next value
                heap.append((node.val, i))

                lists[i] = node.next

        # Heapify the heap
        heapq.heapify(heap)

        # Pull the first value from the heap to start off our new merged
        # list, and cycle a new element from the list it came from
        # (we'll define a helper function for this)
        def cycle_list(list_idx: int) -> None:
            if (node := lists[list_idx]) is not None:
                heapq.heappush(heap, (node.val, list_idx))
                lists[list_idx] = node.next

        # Get the smallest value
        element_val, element_list_idx = heapq.heappop(heap)

        # Make head
        new_list_head = ListNode(val=element_val)
        new_list_tail = new_list_head

        # Cycle new element from list
        cycle_list(element_list_idx)

        # Do the (mostly) the same steps as above while the heap is
        # non-empty
        while heap:
            # Get smallest
            element_val, element_list_idx = heapq.heappop(heap)

            # Make node
            new_list_tail.next = ListNode(val=element_val)
            new_list_tail = new_list_tail.next

            # Cycle
            cycle_list(element_list_idx)

        return new_list_head


# @leet end
