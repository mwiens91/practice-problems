# @leet start
import itertools


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])

        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[i][j] for i in range(num_rows)) for j in range(num_cols)]

        return sum(
            1
            for i, j in itertools.product(range(num_rows), range(num_cols))
            if mat[i][j] == row_sums[i] == col_sums[j] == 1
        )


# @leet end
