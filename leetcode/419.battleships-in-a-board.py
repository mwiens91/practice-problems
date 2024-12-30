# @leet start
import itertools


class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        # Here we'll do a DFS on each battleship we find, and mark these
        # cells as processed. The number of DFSs we do is the number of
        # battleships.
        BATTLESHIP = "X"

        num_rows = len(board)
        num_cols = len(board[0])

        processed_set: set[tuple[int, int]] = set()

        def dfs(row: int, col: int) -> None:
            # Get out if we've already processed this cell
            if (row, col) in processed_set:
                return

            # Add to processed set
            processed_set.add((row, col))

            # Visit neighbours
            for adj_row, adj_col in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= adj_row < num_rows
                    and 0 <= adj_col < num_cols
                    and board[adj_row][adj_col] == BATTLESHIP
                    and (adj_row, adj_col) not in processed_set
                ):
                    dfs(adj_row, adj_col)

        battleship_count = 0

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if board[row][col] == BATTLESHIP and (row, col) not in processed_set:
                dfs(row, col)

                battleship_count += 1

        return battleship_count


# @leet end
