# @leet start
import itertools
import math


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        # Get list of lists (row, col) of cells which are empty, and
        # list of tuples (row, col, num_excess) of cells which have
        # excess stones
        empty_cells: list[tuple[int, int]] = []
        excess_cells: list[tuple[int, int, int]] = []

        for row, col in itertools.product(range(3), range(3)):
            num_stones = grid[row][col]

            if not num_stones:
                empty_cells.append((row, col))
            elif num_stones > 1:
                excess_cells.append((row, col, num_stones - 1))

        # Bruteforce by going through each permutation of empty cells,
        # and filling them with the same arrangement of excess cells
        minimum_number_of_moves = math.inf

        for empty_cell_permutation in itertools.permutations(empty_cells):
            this_number_of_moves = 0
            empty_cell_idx = 0

            for source_row, source_col, num_excess in excess_cells:
                # For each excess stone, put it in an empty cell
                for _ in range(num_excess):
                    dest_row, dest_col = empty_cell_permutation[empty_cell_idx]

                    this_number_of_moves += abs(dest_row - source_row) + abs(
                        dest_col - source_col
                    )

                    empty_cell_idx += 1

            minimum_number_of_moves = min(minimum_number_of_moves, this_number_of_moves)

        return minimum_number_of_moves


# @leet end
