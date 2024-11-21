# @leet start
import heapq


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Grab the third maximum by using a max heap on distinct
        # numbers. In order to use heapq (which gives tools for min
        # heaps) we need to negate the nums while they're in the heap.
        heap = [-x for x in set(nums)]

        heapq.heapify(heap)

        # If there is no third maximum, we're instructed to return the
        # maximum instead (why?)
        if len(heap) < 3:
            return -heapq.heappop(heap)

        # Return third maximum
        for _ in range(2):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


# @leet end
