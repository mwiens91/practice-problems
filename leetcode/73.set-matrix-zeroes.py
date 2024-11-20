# @leet start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get the dimensions of the matrix
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Use this macro later
        REPLACE_WITH_ZERO_LATER = None

        # Define sets so we don't do a given row or column multiple times
        processed_rows = set()
        processed_cols = set()

        # Go through all elements, and if a row or column has a 0,
        # (*) replace all its non-zero elements with the macro defined
        # above. We'll do (*) with a helper function.
        def process_zero(row_idx: int, col_idx: int) -> None:
            if row_idx not in processed_rows:
                # Replace non-zeros
                for j in range(num_cols):
                    if matrix[row_idx][j] != 0:
                        matrix[row_idx][j] = REPLACE_WITH_ZERO_LATER

                # Mark this row as seen
                processed_rows.add(row_idx)

            if col_idx not in processed_cols:
                for i in range(num_rows):
                    if matrix[i][col_idx] != 0:
                        matrix[j][col_idx] = REPLACE_WITH_ZERO_LATER

                processed_cols.add(col_idx)

        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    process_zero(i, j)

        # Now we go through the matrix again, and replace all entries
        # with the macro with 0
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == REPLACE_WITH_ZERO_LATER:
                    matrix[i][j] = 0


# @leet end
