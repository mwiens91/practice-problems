# @leet start
import itertools


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        row_maxes = [max(row) for row in grid]
        col_maxes = [max(grid[i][j] for i in range(num_rows)) for j in range(num_cols)]

        return sum(
            min(row_maxes[i], col_maxes[j]) - grid[i][j]
            for i, j in itertools.product(range(num_rows), range(num_cols))
        )


# @leet end
