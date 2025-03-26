# @leet start
import heapq


class Solution:
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        # Keep a heap with the k largest element we find in grid,
        # pushing only the largest limits[i] elements for each row
        # grid[i]. Note that since Python uses min heaps, we store the
        # summands as negative numbers
        summands_heap: list[int] = []

        for i, row in enumerate(grid):
            largest_from_row = heapq.nlargest(limits[i], row)

            # Push the elements to the heap
            while len(summands_heap) < k and largest_from_row:
                heapq.heappush(summands_heap, -largest_from_row.pop())

            while largest_from_row:
                # Here we are guaranteed the heap has size k
                heapq.heappushpop(summands_heap, -largest_from_row.pop())

        return -sum(summands_heap)


# @leet end
