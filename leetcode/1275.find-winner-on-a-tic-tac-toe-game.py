# @leet start
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        A_MARK = "A"
        B_MARK = "B"

        # Populate board
        board = [[""] * 3 for _ in range(3)]

        for i, (row, col) in enumerate(moves):
            board[row][col] = A_MARK if i % 2 == 0 else B_MARK

        # Check victory: rows, cols, diagonals
        def get_winner(mark: str) -> str:
            return "A" if mark == A_MARK else "B"

        for row in range(3):
            if board[row][0] and len(set(board[row])) == 1:
                return get_winner(board[row][0])

        for col in range(3):
            if board[0][col] and len(set(board[row][col] for row in range(3))) == 1:
                return get_winner(board[0][col])

        if board[0][0] and len(set(board[i][i] for i in range(3))) == 1:
            return get_winner(board[0][0])

        if board[0][2] and len(set(board[i][2 - i] for i in range(3))) == 1:
            return get_winner(board[0][2])

        return "Pending" if len(moves) < 9 else "Draw"


# @leet end
