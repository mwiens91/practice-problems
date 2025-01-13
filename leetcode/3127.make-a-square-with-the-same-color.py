# @leet start
import itertools


class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        # Look at the four possible 2x2 submatrices by iterating over
        # their upper left corners
        for start_row, start_col in itertools.product(range(2), range(2)):
            b_counts = 0
            w_counts = 0

            for row, col in [
                (start_row + i, start_col + j)
                for i, j in itertools.product(range(2), range(2))
            ]:
                if grid[row][col] == "B":
                    b_counts += 1
                else:
                    w_counts += 1

            if b_counts >= 3 or w_counts >= 3:
                return True

        # Not possible for any of the four 2x2 submatrices
        return False


# @leet end
