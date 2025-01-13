# @leet start
import itertools


class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        num_rows = len(grid)
        num_cols = len(grid[0])

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            # Test cell below
            try:
                assert grid[row][col] == grid[row + 1][col]
            except AssertionError:
                return False
            except IndexError:
                pass

            # Test cell to the right
            try:
                assert grid[row][col] != grid[row][col + 1]
            except AssertionError:
                return False
            except IndexError:
                pass

        return True


# @leet end
