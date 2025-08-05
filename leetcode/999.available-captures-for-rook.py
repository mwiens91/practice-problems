# @leet start
from typing import Iterable


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        BOARD_LENGTH = 8
        ROOK = "R"
        ALLY_BISHOP = "B"
        ENEMY_PAWN = "p"

        # Find row and column of rook
        for row, row_list in enumerate(board):
            try:
                rook_col = row_list.index(ROOK)
                rook_row = row

                break
            except ValueError:
                pass

        # Find and return number of enemy pawns we are attacking
        def is_attacking(row_range: Iterable[int], col_range: Iterable[int]) -> bool:
            for row in row_range:
                for col in col_range:
                    if board[row][col] == ALLY_BISHOP:
                        return False

                    if board[row][col] == ENEMY_PAWN:
                        return True

            return False

        return sum(
            [
                is_attacking(range(rook_row - 1, -1, -1), [rook_col]),
                is_attacking(range(rook_row + 1, BOARD_LENGTH), [rook_col]),
                is_attacking([rook_row], range(rook_col - 1, -1, -1)),
                is_attacking([rook_row], range(rook_col + 1, BOARD_LENGTH)),
            ]
        )


# @leet end
