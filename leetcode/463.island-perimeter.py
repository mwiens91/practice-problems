# @leet start
import itertools


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # Handy macros
        LAND = 1

        # Get dimensions of grid
        num_rows = len(grid)
        num_cols = len(grid[0])

        # First, we'll find any cell that is part of the island
        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid[row][col] == LAND:
                break

        # Now define a depth-first search function that we can run on
        # the island cell we found, which keeps track of the perimeter
        perimeter = 0

        seen_set: set[tuple[int, int]] = set()

        def dfs(row: int, col: int) -> None:
            nonlocal perimeter

            # Add the cell to the seen set
            seen_set.add((row, col))

            # Get adjacent land cells
            adjacent_land = []

            for adj_row, adj_col in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= adj_row < num_rows
                    and 0 <= adj_col < num_cols
                    and grid[adj_row][adj_col] == LAND
                ):
                    adjacent_land.append((adj_row, adj_col))

            # Add water to the perimeter
            perimeter += 4 - len(adjacent_land)

            # Recurse on adjacent land
            for cell in adjacent_land:
                if cell not in seen_set:
                    dfs(*cell)

        # Get the perimeter starting from the first cell we found
        dfs(row, col)  # pylint: disable=undefined-loop-variable

        return perimeter


# @leet end
