# @leet start
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int, int] = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        heap: list[tuple[int, int]] = []

        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappushpop(heap, (count, num))

        return [num for _, num in heap]


# @leet end
