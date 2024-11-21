# @leet start
import heapq
import math


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        # Put the piles in a max heap. Note that because heapq only
        # operates on min heaps, we need to negate the pile values while
        # they're in the heap.
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        # Get rid of as many stones as possible for each iteration
        for _ in range(k):
            pile = -heapq.heappop(heap)
            heapq.heappush(heap, -math.ceil(pile / 2))

        return -sum(heap)


# @leet end
