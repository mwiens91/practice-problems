# @leet start
class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        def has_won(tile: str) -> bool:
            return (
                any(
                    all(board[row][col] == tile for col in range(3)) for row in range(3)
                )
                or any(
                    all(board[row][col] == tile for row in range(3)) for col in range(3)
                )
                or all(board[i][i] == tile for i in range(3))
                or all(board[i][2 - i] == tile for i in range(3))
            )

        P1 = "X"
        P2 = "O"

        diff = 0

        for row in board:
            for tile in row:
                if tile == P1:
                    diff += 1
                elif tile == P2:
                    diff -= 1

        p1_won = has_won(P1)
        p2_won = has_won(P2)

        return (
            (p1_won and not p2_won and diff == 1)
            or (p2_won and not p1_won and diff == 0)
            or (not p1_won and not p2_won and 0 <= diff <= 1)
        )


# @leet end
