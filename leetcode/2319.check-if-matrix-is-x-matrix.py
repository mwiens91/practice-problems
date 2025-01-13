# @leet start
import itertools


class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)

        for row, col in itertools.product(range(n), range(n)):
            if row in {col, n - 1 - col}:
                # Diagonals need to be non-zero
                if grid[row][col] == 0:
                    return False
            else:
                # All non-diagonal elements need to be zero
                if grid[row][col] != 0:
                    return False

        return True


# @leet end
