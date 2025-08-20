# @leet start
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        count = (
            sum(matrix[0]) + sum(matrix[i][0] for i in range(num_rows)) - matrix[0][0]
        )

        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][col] == 1:
                    matrix[row][col] = 1 + min(
                        matrix[row - 1][col - 1],
                        matrix[row - 1][col],
                        matrix[row][col - 1],
                    )

                    count += matrix[row][col]

        return count


# @leet end
