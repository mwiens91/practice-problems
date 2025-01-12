# @leet start
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # Sum each diagonal, including a possibly repeated middle
        # element for now
        n = len(mat)

        diagonal_sum = 0

        # Primary diagonal
        for row, col in zip(range(n), range(n)):
            diagonal_sum += mat[row][col]

        # Secondary diagonal
        for row, col in zip(range(n), range(n - 1, -1, -1)):
            diagonal_sum += mat[row][col]

        # For n odd: remove the middle element that we added twice
        if n % 2 == 1:
            middle_idx = (n - 1) // 2
            diagonal_sum -= mat[middle_idx][middle_idx]

        return diagonal_sum


# @leet end
