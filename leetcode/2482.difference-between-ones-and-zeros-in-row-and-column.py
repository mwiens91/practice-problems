# @leet start
import itertools


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        num_rows = len(grid)
        num_cols = len(grid[0])

        row_diffs = [2 * sum(row) - num_cols for row in grid]
        col_diffs = [
            2 * sum(grid[i][j] for i in range(num_rows)) - num_rows
            for j in range(num_cols)
        ]

        # I'm just going to modify the passed in grid, but we could make
        # a new 2D list if we didn't want to mutate it
        for i, j in itertools.product(range(num_rows), range(num_cols)):
            grid[i][j] = row_diffs[i] + col_diffs[j]

        return grid


# @leet end
