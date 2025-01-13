# @leet start
import itertools


class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Count number of operations we need
        num_operations = 0

        for row, col in itertools.product(range(1, num_rows), range(num_cols)):
            current_value = grid[row][col]
            above_value = grid[row - 1][col]

            operations_needed = max(0, above_value + 1 - current_value)

            grid[row][col] += operations_needed
            num_operations += operations_needed

        return num_operations


# @leet end
