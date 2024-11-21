# @leet start
import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # We'll use a heap to find the maximum number of gifts. Since
        # Python provides methods to deal with a min heap only, we'll
        # negate the values while they're in the heap.
        heap = [-pile for pile in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            # Get the pile with the most gifts
            pile = -heapq.heappop(heap)

            # Take away some gifts and put the pile back
            pile = math.floor(math.sqrt(pile))

            heapq.heappush(heap, -pile)

        # Return the number of gifts remaining
        return -sum(heap)


# @leet end
