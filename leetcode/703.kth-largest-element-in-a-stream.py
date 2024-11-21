# @leet start
import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # Heap will be a min heap; we'll keep the k largest values in it
        self.heap = nums
        self.k = k
        self.current_size = len(nums)

        # Heapify and shrink to k-size
        heapq.heapify(self.heap)

        for _ in range(self.current_size - self.k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if self.current_size < self.k:
            heapq.heappush(self.heap, val)

            self.current_size += 1
        else:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @leet end
