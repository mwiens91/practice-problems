# @leet start
import itertools


class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Find first and last rows and cols with 1s
        first_row = num_rows
        last_row = -1
        first_col = num_cols
        last_col = -1

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid[row][col] == 1:
                first_row = min(first_row, row)
                last_row = max(last_row, row)
                first_col = min(first_col, col)
                last_col = max(last_col, col)

        return (
            (last_row - first_row + 1) * (last_col - first_col + 1)
            if last_row != -1
            else 0
        )


# @leet end
