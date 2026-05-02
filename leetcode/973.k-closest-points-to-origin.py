# @leet start
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [(x**2 + y**2, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(heap)

        res: list[list[int]] = []

        for _ in range(k):
            _, i = heapq.heappop(heap)
            res.append(points[i])

        return res


# @leet end
