# @leet start
from itertools import chain


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        if num_rows * num_cols != r * c:
            return mat

        output = [[0] * c for _ in range(r)]

        output_row = 0
        output_col = 0

        for num in chain.from_iterable(mat):
            if output_col >= c:
                output_row += 1
                output_col = 0

            output[output_row][output_col] = num
            output_col += 1

        return output


# @leet end
