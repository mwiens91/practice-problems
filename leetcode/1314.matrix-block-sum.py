# @leet start
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        # Prefix sums
        for row in range(rows):
            for col in range(cols):
                if row > 0 and col > 0:
                    mat[row][col] += (
                        mat[row - 1][col] + mat[row][col - 1] - mat[row - 1][col - 1]
                    )
                elif row > 0:
                    mat[row][col] += mat[row - 1][col]
                elif col > 0:
                    mat[row][col] += mat[row][col - 1]

        def cell_val(row: int, col: int) -> int:
            low_row = max(0, row - k)
            high_row = min(rows - 1, row + k)
            low_col = max(0, col - k)
            high_col = min(cols - 1, col + k)

            res = mat[high_row][high_col]

            if low_row > 0 and low_col > 0:
                res += (
                    mat[low_row - 1][low_col - 1]
                    - mat[low_row - 1][high_col]
                    - mat[high_row][low_col - 1]
                )
            elif low_row > 0:
                res -= mat[low_row - 1][high_col]
            elif low_col > 0:
                res -= mat[high_row][low_col - 1]

            return res

        return [[cell_val(row, col) for col in range(cols)] for row in range(rows)]


# @leet end
