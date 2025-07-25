# @leet start
class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        num_rows = len(grid)
        num_cols = len(grid[0])

        return [
            max(len(str(grid[row][col])) for row in range(num_rows))
            for col in range(num_cols)
        ]


# @leet end
