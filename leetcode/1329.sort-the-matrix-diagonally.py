# @leet start
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        # We index the diagonals with the difference
        # row - col = diff. We don't need to sort the 1-cell
        # diagonals, since those are already sorted.
        for diff in range(-num_cols + 2, num_rows - 1):
            rows = list(range(max(0, diff), min(num_rows, num_cols + diff)))
            cols = [row - diff for row in rows]

            for sorted_val, row, col in zip(
                sorted(mat[row][col] for row, col in zip(rows, cols)), rows, cols
            ):
                mat[row][col] = sorted_val

        return mat


# @leet end
