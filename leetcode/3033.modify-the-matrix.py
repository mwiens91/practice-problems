# @leet start
import itertools


class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        column_maxes = [
            max(matrix[row][col] for row in range(num_rows)) for col in range(num_cols)
        ]

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if matrix[row][col] == -1:
                matrix[row][col] = column_maxes[col]

        return matrix


# @leet end
