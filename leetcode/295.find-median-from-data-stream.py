# @leet start
import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap: list[int] = []
        self.min_heap: list[int] = []

    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] + self.min_heap[0]) / 2

        if len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0]

        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @leet end
