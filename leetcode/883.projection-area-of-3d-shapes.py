# @leet start
import itertools


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Return the number of non-zero elements + row maxes + col
        # maxes. We can definitely do this more efficiently, but the
        # this is still asymptotically optimal.
        return (
            sum(
                1
                for i, j in itertools.product(range(num_rows), range(num_cols))
                if grid[i][j] > 0
            )
            + sum(max(row) for row in grid)
            + sum(max(grid[i][j] for i in range(num_rows)) for j in range(num_cols))
        )


# @leet end
