# @leet start
import math


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(heights)
        cols = len(heights[0])
        seen = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int, limit: int):
            if r == rows - 1 and c == cols - 1:
                return True

            seen[r][c] = True

            for dr, dc in DIRS:
                adjR = r + dr
                adjC = c + dc

                if (
                    0 <= adjR < rows
                    and 0 <= adjC < cols
                    and not seen[adjR][adjC]
                    and abs(heights[r][c] - heights[adjR][adjC]) <= limit
                    and dfs(adjR, adjC, limit)
                ):
                    return True

            return False

        low = math.inf
        high = -math.inf

        for r in range(rows):
            for c in range(cols):
                low = min(low, heights[r][c])
                high = max(high, heights[r][c])

        left = 0
        right = high - low

        while left <= right:
            mid = left + (right - left) // 2

            if dfs(0, 0, mid):
                right = mid - 1
            else:
                left = mid + 1

            seen = [[False] * cols for _ in range(rows)]

        return left


# @leet end
