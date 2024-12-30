# @leet start
from collections import deque
import itertools
from typing import Deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # This is a multi-source BFS problem. First enqueue all rotting
        # oranges. The queue contains a row, column, and time at which
        # the orange rotted.
        num_rows = len(grid)
        num_cols = len(grid[0])

        FRESH_ORANGE = 1
        ROTTEN_ORANGE = 2

        queue: Deque[tuple[int, int, int]] = deque()

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid[row][col] == ROTTEN_ORANGE:
                queue.appendleft((row, col, 0))

        # Next, in the loop we'll infect neighbours until there's
        # nothing left to infect
        time = 0

        while queue:
            # Unpack rotten orange
            row, col, time_rotted = queue.pop()

            # Set global time
            time = time_rotted

            # Infect neighbours
            for adj_row, adj_col in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= adj_row < num_rows
                    and 0 <= adj_col < num_cols
                    and grid[adj_row][adj_col] == FRESH_ORANGE
                ):
                    grid[adj_row][adj_col] = ROTTEN_ORANGE
                    queue.appendleft((adj_row, adj_col, time + 1))

        # Ensure there are no fresh oranges left
        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid[row][col] == FRESH_ORANGE:
                return -1

        return time


# @leet end
