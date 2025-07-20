# @leet start
import itertools


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        # WATER = 0
        LAND = 1

        num_rows = len(grid2)
        num_cols = len(grid2[0])

        # We'll iterate over grid2, and keep track of land we've seen
        # already in a set
        visited: set[tuple[int, int]] = set()

        # Define a function to consume an island, which will return
        # whether the island is a sub-island
        def is_subisland(start: tuple[int, int]) -> bool:
            subisland_result = grid1[start[0]][start[1]] == LAND
            visited.add(start)
            stack = [start]

            while stack:
                row, col = stack.pop()

                for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row = row + delta_row
                    new_col = col + delta_col

                    if (
                        0 <= new_row < num_rows
                        and 0 <= new_col < num_cols
                        and grid2[new_row][new_col] == LAND
                        and (new_row, new_col) not in visited
                    ):
                        subisland_result &= grid1[new_row][new_col] == LAND
                        visited.add((new_row, new_col))
                        stack.append((new_row, new_col))

            return subisland_result

        subisland_count = 0

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if grid2[row][col] == LAND and (row, col) not in visited:
                if is_subisland((row, col)):
                    subisland_count += 1

        return subisland_count


# @leet end
