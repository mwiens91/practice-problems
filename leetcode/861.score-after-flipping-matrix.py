# @leet start
class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Flip all rows that start with 0
        for row in grid:
            if row[0] == 0:
                for i in range(1, num_cols):  # no need to flip row[i]
                    row[i] ^= 1

        # Add to the score using the best result of flipping of not
        # flipping each column
        score = num_rows << (num_cols - 1)

        for col_idx in range(1, num_cols):
            col_sum = sum(grid[i][col_idx] for i in range(num_rows))
            score += max(col_sum, num_rows - col_sum) << (num_cols - 1 - col_idx)

        return score


# @leet end
