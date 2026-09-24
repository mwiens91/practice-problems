# @leet start
import heapq


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        res = 0
        endpoints_heap: list[int] = []

        for start, end in intervals:
            while endpoints_heap and endpoints_heap[0] < start:
                heapq.heappop(endpoints_heap)

            res += len(endpoints_heap)
            heapq.heappush(endpoints_heap, end)

        return res


# @leet end
