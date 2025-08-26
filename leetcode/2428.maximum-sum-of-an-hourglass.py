# @leet start
class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Iterate through the upper left starting points. Note that
        # there are various ways of preprocessing the matrix to bring
        # the constant time down, but from methods I've thought of none
        # will bring much if any performance improvement.
        max_sum = 0

        for row in range(num_rows - 2):
            for col in range(num_cols - 2):
                max_sum = max(
                    max_sum,
                    sum(sum(grid[row + j][col + i] for i in (0, 1, 2)) for j in (0, 2))
                    + grid[row + 1][col + 1],
                )

        return max_sum


# @leet end
