# @leet start
class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        # Sort all rows, and then the answer is obtained by summing the
        # column maxes
        for row in grid:
            row.sort()

        num_rows = len(grid)
        num_cols = len(grid[0])

        return sum(max(grid[i][j] for i in range(num_rows)) for j in range(num_cols))


# @leet end
