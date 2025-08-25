# @leet start
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        result: list[int] = []

        num_rows = len(mat)
        num_cols = len(mat[0])
        num_diags = num_rows + num_cols - 1

        # For the diagonals we have row + col = i
        for i in range(num_diags):
            iter_fn = reversed if i % 2 == 0 else iter

            min_row = max(0, i - num_cols + 1)
            max_row = min(num_rows - 1, i)

            for row in iter_fn(range(min_row, max_row + 1)):
                result.append(mat[row][i - row])

        return result


# @leet end
