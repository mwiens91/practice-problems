# @leet start
import itertools


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # WATER = 0
        LAND = 1

        # Keep track of the maximum area seen so far and the land cells
        # we've already processed
        max_area = 0
        processed_land: set[tuple[int, int]] = set()

        num_rows = len(grid)
        num_cols = len(grid[0])

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid[row][col] == LAND and (row, col) not in processed_land:
                processed_land.add((row, col))

                # Find the area of this island
                land_stack = [(row, col)]
                area = 0

                while land_stack:
                    current_row, current_col = land_stack.pop()
                    area += 1

                    # Add adjacent land not already processed
                    for row_delta, col_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        adj_row = current_row + row_delta
                        adj_col = current_col + col_delta

                        if (
                            0 <= adj_row < num_rows
                            and 0 <= adj_col < num_cols
                            and grid[adj_row][adj_col] == LAND
                            and (adj_row, adj_col) not in processed_land
                        ):
                            land_stack.append((adj_row, adj_col))
                            processed_land.add((adj_row, adj_col))

                max_area = max(max_area, area)

        return max_area


# @leet end
