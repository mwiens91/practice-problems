# @leet start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # This is using san's solution explanation here
        # https://stackoverflow.com/a/75129692. The idea is that we
        # start at the top right corner. If the target is less than the
        # cell value we move down a row; if the target is greater than
        # the cell value we move down a column. We either find the
        # target this way or end up in the bottom left. I'm not 100%
        # sure how I'd go about proving that this works, but if you
        # spend some time thinking about it you should be able to
        # convince yourself that the solution works.

        # First get the matrix dimensions and set our current cell
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        row = 0
        col = num_cols - 1

        # Now do the algorithm
        while row < num_rows and col >= 0:
            val = matrix[row][col]

            if val == target:
                return True

            if val < target:
                row += 1
            else:
                # val > target
                col -= 1

        return False


# @leet end
