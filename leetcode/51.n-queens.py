# @leet start
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # We'll use brute force here. Terminology:
        #
        # ddr stands for diagonal down right
        # dur stands for diagonal up right
        #
        # The x-th ddr is the set of indices (i, j) such that j = x + i,
        # where x = -n + 1, ..., 0, ... n - 1.
        #
        # The y-th dur is the set of indices (i, j) such that i + j = y,
        # where y = 0, 1, ..., 2 * (n - 1) - 1, 2 * (n - 1)
        #

        # We'll have a bunch of sets which let us know what columns and
        # diagonals are occupied, and where the queens are. We don't
        # need to keep track of occupied rows.
        occupied_cols: set[int] = set()
        occupied_ddrs: set[int] = set()
        occupied_durs: set[int] = set()
        queen_cells: set[tuple[int, int]] = set()

        # Put our solutions here
        results: list[list[str]] = []

        # Helper function to record solution
        def record_solution() -> None:
            board = [["."] * n for _ in range(n)]

            for i, j in queen_cells:
                board[i][j] = "Q"

            results.append(["".join(row) for row in board])

        # Recursive function here. For each position try placing a queen
        # (if possible) or not placing one
        def recurse(row_idx: int = 0, col_idx: int = 0, curr_queens: int = 0) -> None:
            # Base case
            if curr_queens == n:
                record_solution()

                return

            # Get out if we're out of bounds row-wise (column-wise is
            # accounted for in logic below)
            if row_idx == n:
                return

            # Try placing a queen if possible
            if (
                col_idx not in occupied_cols
                and col_idx - row_idx not in occupied_ddrs
                and row_idx + col_idx not in occupied_durs
            ):
                occupied_cols.add(col_idx)
                occupied_ddrs.add(col_idx - row_idx)
                occupied_durs.add(row_idx + col_idx)
                queen_cells.add((row_idx, col_idx))

                recurse(row_idx + 1, 0, curr_queens + 1)

                occupied_cols.remove(col_idx)
                occupied_ddrs.remove(col_idx - row_idx)
                occupied_durs.remove(row_idx + col_idx)
                queen_cells.remove((row_idx, col_idx))

            # Try not placing a queen
            if col_idx == n - 1:
                recurse(row_idx + 1, 0, curr_queens)
            else:
                recurse(row_idx, col_idx + 1, curr_queens)

        # Recurse and return results
        recurse()

        return results


# @leet end
