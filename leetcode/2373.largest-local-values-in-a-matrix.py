# @leet start
import itertools


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)

        result = [[0] * (n - 2) for _ in range(n - 2)]

        for i, j in itertools.product(range(n - 2), range(n - 2)):
            result[i][j] = max(
                grid[1 + i + dr][1 + j + dc]
                for dr, dc in itertools.product((-1, 0, 1), (-1, 0, 1))
            )

        return result


# @leet end
