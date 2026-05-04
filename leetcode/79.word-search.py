# @leet start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        VISITED = "0"
        rows = len(board)
        cols = len(board[0])

        def backtrack(i: int, row: int, col: int) -> bool:
            if i == len(word) - 1:
                return True

            board[row][col] = VISITED

            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                adj_row = row + delta_row
                adj_col = col + delta_col

                if (
                    0 <= adj_row < rows
                    and 0 <= adj_col < cols
                    and board[adj_row][adj_col] == word[i + 1]
                    and backtrack(i + 1, adj_row, adj_col)
                ):
                    return True

            board[row][col] = word[i]

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and backtrack(0, row, col):
                    return True

        return False


# @leet end
