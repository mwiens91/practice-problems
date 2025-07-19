# @leet start
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)

        for row in matrix:
            if len(set(row)) < n:
                return False

        for col_idx in range(n):
            if len(set(row[col_idx] for row in matrix)) < n:
                return False

        return True


# @leet end
