# @leet start
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get the length of the matrix
        n = len(matrix)

        # Define a function to rotate the edge of the m x m "inner
        # matrix", m = n, n - 2, n - 4, ..., 3 (or 2). An inner matrix
        # is the submatrix consisting of the m inner rows and columns.
        def rotate_edge(m: int) -> None:
            # Get the top left and bottom right row and column indices
            # of the inner matrix
            tl_idx = (n - m) // 2
            br_idx = n - tl_idx - 1

            # I figured this bit out on paper. It's not too hard to
            # derive for special cases (try m = 4) and then see that it
            # holds generally too (for m >= 2)
            for i in range(m - 1):
                (
                    matrix[tl_idx][tl_idx + i],
                    matrix[tl_idx + i][br_idx],
                    matrix[br_idx][br_idx - i],
                    matrix[br_idx - i][tl_idx],
                ) = (
                    matrix[br_idx - i][tl_idx],
                    matrix[tl_idx][tl_idx + i],
                    matrix[tl_idx + i][br_idx],
                    matrix[br_idx][br_idx - i],
                )

        # Rotate each inner edge
        m = n

        while m >= 2:
            rotate_edge(m)

            m -= 2


# @leet end
