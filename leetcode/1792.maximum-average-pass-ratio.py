# @leet start
import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # Let p and t be the number of passing students and the total
        # number of students in a class. Then the marginal gain in
        # passing ratio is given by (p + 1)/(t + 1) - p / t. We order a
        # heap by this passing ratio. Since Python's heapq library uses
        # min-heaps, we store the negative of the passing ratio.
        heap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapq.heapify(heap)

        # For each extra student, add them to the smallest available
        # non-perfect class
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            heapq.heappush(heap, ((p + 1) / (t + 1) - (p + 2) / (t + 2), p + 1, t + 1))

        return sum(p / t for _, p, t in heap) / len(heap)


# @leet end
