# @leet start
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        counts: dict[tuple[int, ...], int] = {}

        for row in grid:
            row_t = tuple(row)
            counts[row_t] = counts.get(row_t, 0) + 1

        rows = len(grid)
        cols = len(grid[0])

        res = 0

        for j in range(cols):
            res += counts.get(tuple(grid[i][j] for i in range(rows)), 0)

        return res


# @leet end
