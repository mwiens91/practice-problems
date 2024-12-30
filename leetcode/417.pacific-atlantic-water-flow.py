# @leet start
from collections import deque
import itertools


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # We'll use BFS to find all cells which can reach a given ocean:
        # Pacific Ocean (left and top) or Atlantic Ocean (right and
        # bottom)
        num_rows = len(heights)
        num_cols = len(heights[0])

        # Call this function to find cells reachable from given points
        def find_reachable_cells(
            initial_points: list[tuple[int, int]]
        ) -> list[list[bool]]:
            # Initialize the output array
            reachable_matrix = [[False] * num_cols for _ in range(num_rows)]

            for row, col in initial_points:
                reachable_matrix[row][col] = True

            # Set up a queue we'll add neighbouring cells to that have a
            # height greater than or equal to the height of cell under
            # consideration
            queue = deque(initial_points)

            while queue:
                # Pop point from the queue and get its height
                row, col = queue.pop()
                height = heights[row][col]

                # Enqueue adjacent cells seen that have a height greater
                # than or equal to the current height and mark them as
                # reachable
                for adj_row, adj_col in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ]:
                    if (
                        0 <= adj_row < num_rows
                        and 0 <= adj_col < num_cols
                        and heights[adj_row][adj_col] >= height
                        and not reachable_matrix[adj_row][adj_col]
                    ):
                        queue.appendleft((adj_row, adj_col))
                        reachable_matrix[adj_row][adj_col] = True

            return reachable_matrix

        # Use the above function to find cells which can reach both
        # oceans
        pacific_ocean_cells = [(0, col) for col in range(num_cols)] + [
            (row, 0) for row in range(1, num_rows)
        ]
        atlantic_ocean_cells = [(num_rows - 1, col) for col in range(num_cols)] + [
            (row, num_cols - 1) for row in range(num_rows - 1)
        ]

        can_reach_pacific_matrix = find_reachable_cells(pacific_ocean_cells)
        can_reach_atlantic_matrix = find_reachable_cells(atlantic_ocean_cells)

        can_reach_both = []

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if (
                can_reach_pacific_matrix[row][col]
                and can_reach_atlantic_matrix[row][col]
            ):
                can_reach_both.append([row, col])

        return can_reach_both


# @leet end
