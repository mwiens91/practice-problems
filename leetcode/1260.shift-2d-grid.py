# @leet start
from collections import deque
import itertools
from typing import Deque


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        # Get dimensions of grid
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Ensure k does not perform complete rotations of the array
        k %= num_rows * num_cols

        # If k is zero, we don't have to do any work, so return now
        if k == 0:
            return grid

        # We'll do this by modifying the passed in grid in place using
        # O(k) memory for a queue. First, put the final k numbers in
        # queue.
        queue: Deque[int] = deque()

        first_in_queue_row = num_rows - 1 - (k - 1) // num_cols
        first_in_queue_col = num_cols - 1 - (k - 1) % num_cols

        for row in range(first_in_queue_row, num_rows):
            col_range = (
                range(first_in_queue_col, num_cols)
                if row == first_in_queue_row
                else range(num_cols)
            )

            for col in col_range:
                queue.appendleft(grid[row][col])

        # Now go through the whole grid and rotate the numbers
        for row, col in itertools.product(range(num_rows), range(num_cols)):
            # Enqueue the current value then replace it with the last
            # value in the queue
            queue.appendleft(grid[row, col])

            grid[row][col] = queue.pop()

        return grid


# @leet end
