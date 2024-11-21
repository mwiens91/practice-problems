# @leet start
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # min_heap is is a min heap of points. Each point is represented
        # by a tuple where the first element is proportional to the
        # distance, and the second element is a list [x, y] containing
        # the coordinates of the point.
        min_heap: list[tuple[int, list[int]]] = [
            (x**2 + y**2, [x, y]) for x, y in points
        ]

        heapq.heapify(min_heap)

        # Get the k cloesest points
        results: list[list[int]] = []

        for _ in range(k):
            results.append(heapq.heappop(min_heap)[1])

        return results


# @leet end
