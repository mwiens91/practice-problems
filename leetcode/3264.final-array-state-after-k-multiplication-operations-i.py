# @leet start
import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        if multiplier == 1:
            return nums

        # Perform the k operations
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, idx = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, idx))

        # Put the results back in passed in list
        for num, idx in heap:
            nums[idx] = num

        return nums


# @leet end
