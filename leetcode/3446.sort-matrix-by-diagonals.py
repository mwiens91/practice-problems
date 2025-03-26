# @leet start
class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        # We label each diagonal with the difference between the row and
        # column indices d = row_idx - col_idx. Get each diagonal's
        # elements, sort them in descending order if d >= 0 (else
        # ascending order), then insert them in that order.
        n = len(grid)

        for d in range(-(n - 1), n):
            # Get the diagonal indices
            row_range = range(d, n) if d >= 0 else range(0, n + d)
            diagonal_indices = [(i, i - d) for i in row_range]

            # Sort the elements of the diagonal
            diagonal_elements_sorted = sorted(
                (grid[row_idx][col_idx] for row_idx, col_idx in diagonal_indices),
                reverse=d >= 0,
            )

            # Re-insert them
            for i, (row_idx, col_idx) in enumerate(diagonal_indices):
                grid[row_idx][col_idx] = diagonal_elements_sorted[i]

        return grid


# @leet end
