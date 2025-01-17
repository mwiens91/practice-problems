# @leet start
import heapq


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Put tuples (num, index) in a heap
        heap: list[tuple[int, int]] = []

        for idx, num in enumerate(arr):
            heapq.heappush(heap, (num, idx))

        # Replace each element of the original array with its rank
        rank = 0
        prev_num = None

        while heap:
            # Get the number and its index from the heap
            num, idx = heapq.heappop(heap)

            # Increase the rank counter if this element is greater than
            # the previous element (because we're operating on a heap,
            # all we need to check is that the elements are different
            # for the inequality to hold)
            if num != prev_num:
                rank += 1

            # Replace the number with its rank in the original array
            arr[idx] = rank

            # Set up for next iteration
            prev_num = num

        return arr


# @leet end
