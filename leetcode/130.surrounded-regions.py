# @leet start
import itertools


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Keep track of O cells we've already visited
        visited_Os: set[tuple[int, int]] = set()

        # Get dimensions of board
        num_rows = len(board)
        num_cols = len(board[0])

        # Define a function to get cells in a region
        def get_region_cells(
            current_cell: tuple[int, int], visited_set: set[tuple[int, int]]
        ) -> None:
            # Add this cell as seen
            visited_set.add(current_cell)

            # Visit adjacent cells
            current_row, current_col = current_cell

            for j, k in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_row = current_row + j
                new_col = current_col + k

                new_cell = (new_row, new_col)

                if (
                    0 <= new_row < num_rows
                    and 0 <= new_col < num_cols
                    and new_cell not in visited_set
                    and board[new_row][new_col] == "O"
                ):
                    get_region_cells(new_cell, visited_set)

        # Go through all regions, and capture any surrounded regions
        for row, col in itertools.product(range(num_rows), range(num_cols)):
            cell = (row, col)
            cell_value = board[row][col]

            if cell_value == "O" and cell not in visited_Os:
                # Get cells in the region
                region_cells: set[tuple[int, int]] = set()

                get_region_cells(cell, region_cells)

                # If any cells in the region are on the border, it isn't
                # surrounded
                surrounded = True

                for cell_row, cell_col in region_cells:
                    if cell_row in {0, num_rows - 1} or cell_col in {
                        0,
                        num_cols - 1,
                    }:
                        surrounded = False

                        break

                # If the region is surrounded, capture it. Otherwise,
                # add the region to the global visited set.
                if surrounded:
                    for cell_row, cell_col in region_cells:
                        board[cell_row][cell_col] = "X"
                else:
                    visited_Os.update(region_cells)


# @leet end
