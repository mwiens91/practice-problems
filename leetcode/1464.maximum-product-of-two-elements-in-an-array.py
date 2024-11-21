# @leet start
import heapq


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Find the two largest elements. We're using a min heap so we
        # need to negate numbers while they're in the heap.
        heap = [-num for num in nums]
        heapq.heapify(heap)

        large_1 = -heapq.heappop(heap)
        large_2 = -heapq.heappop(heap)

        return (large_1 - 1) * (large_2 - 1)


# @leet end
