# @leet start
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Python's heapq provides us with a min heap, so to get a max
        # heap we'll just negate all the values; it'll take a bit of
        # care, but it's okay.
        max_heap = [-x for x in stones]
        heap_size = len(max_heap)

        heapq.heapify(max_heap)

        # Play the stone game
        while heap_size >= 2:
            # larger >= smaller by the heap invariant
            larger = -heapq.heappop(max_heap)
            smaller = -heapq.heappop(max_heap)

            if larger > smaller:
                heapq.heappush(max_heap, smaller - larger)

                heap_size -= 1
            else:
                # larger == smaller
                heap_size -= 2

        # Return the result
        if heap_size == 1:
            return -max_heap[0]

        return 0


# @leet end
