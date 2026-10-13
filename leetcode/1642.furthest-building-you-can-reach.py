# @leet start
import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        ladder_heap = []
        bricks_used = 0

        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]

            if diff > 0:
                if len(ladder_heap) < ladders:
                    heapq.heappush(ladder_heap, diff)
                else:
                    bricks_used += heapq.heappushpop(ladder_heap, diff)

                if bricks_used > bricks:
                    return i - 1

        return len(heights) - 1


# @leet end
