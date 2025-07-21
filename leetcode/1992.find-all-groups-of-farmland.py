# @leet start
import itertools


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        # NOTE: there are definitely more efficient ways to handle
        # marking nodes as visited than shoving every cell in a visted
        # set (we can use the fact that all farm groups are
        # rectangles). Not implemented here though
        FARM = 1

        num_rows = len(land)
        num_cols = len(land[0])

        visited: set[tuple[int, int]] = set()
        result: list[list[int]] = []

        # (start_row, start_col) is the top left corner of the farm
        # group
        def consume_farm_group(start_row: int, start_col: int) -> None:
            end_row = start_row

            while end_row < num_rows - 1 and land[end_row + 1][start_col] == FARM:
                end_row += 1

            end_col = start_col

            while end_col < num_cols - 1 and land[end_row][end_col + 1] == FARM:
                end_col += 1

            visited.update(
                (row, col)
                for row, col in itertools.product(
                    range(start_row, end_row + 1), range(start_col, end_col + 1)
                )
            )
            result.append([start_row, start_col, end_row, end_col])

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if land[row][col] == FARM and (row, col) not in visited:
                consume_farm_group(row, col)

        return result


# @leet end
