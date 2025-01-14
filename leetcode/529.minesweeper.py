# @leet start
import itertools


class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        # Useful macros
        UNREVEALED_MINE = "M"
        UNREVEALED_EMPTY = "E"
        REVEALED_EMPTY = "B"
        REVEALED_MINE = "X"

        # Handle the trivial case of clicking on a mine
        if board[click[0]][click[1]] == UNREVEALED_MINE:
            board[click[0]][click[1]] = REVEALED_MINE

            return board

        # Define function to detect how many mines are adjacent to a
        # given square
        num_rows = len(board)
        num_cols = len(board[0])

        def get_adjacent_cells(row: int, col: int) -> list[tuple[int, int]]:
            return [
                (row + delta_row, col + delta_col)
                for delta_row, delta_col in itertools.product(
                    range(-1, 2), range(-1, 2)
                )
                if (delta_row != 0 or delta_col != 0)  # don't include point itself
                and 0 <= row + delta_row < num_rows  # respect boundaries
                and 0 <= col + delta_col < num_cols
            ]

        def get_num_adjacent_mines(row: int, col: int) -> int:
            num_adjacent_mines = 0

            for adjacent_row, adjacent_col in get_adjacent_cells(row, col):
                num_adjacent_mines += int(
                    board[adjacent_row][adjacent_col] == UNREVEALED_MINE
                )

            return num_adjacent_mines

        # Now deal with clicking on an unrevealed empty square. Do a
        # depth-first search: process the current square, and then, if
        # the current square was empty, move on to the children.
        def dfs(row: int, col: int) -> None:
            # Process current square
            num_adjacent_mines = get_num_adjacent_mines(row, col)
            is_empty_square = not bool(num_adjacent_mines)

            board[row][col] = (
                REVEALED_EMPTY if is_empty_square else str(num_adjacent_mines)
            )

            # If the current square was empty, move on to the adjacent cells
            if is_empty_square:
                for adjacent_row, adjacent_col in get_adjacent_cells(row, col):
                    if board[adjacent_row][adjacent_col] == UNREVEALED_EMPTY:
                        dfs(adjacent_row, adjacent_col)

        # Process the click
        dfs(*click)

        return board


# @leet end
