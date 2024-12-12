# @leet start
import itertools


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # Our input gives us characters of numbers in the matrix instead
        # of integers, which is really annoying to deal with. So we'll
        # just convert them here.
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for i, j in itertools.product(range(num_rows), range(num_cols)):
            matrix[i][j] = int(matrix[i][j])

        # Idea: for simplicity suppose the matrix is square. For a given
        # cell c, if we already know its neighbours can form squares of
        # side length n1, n2, n3, then c can form a square of
        # nc = 1 + min(n1, n2, n3), because in each direction right,
        # down, or diagonally (including cell c), there are guaranteed
        # to be at least nc 1s.
        #
        # Using this, we can start at the bottom right of the matrix,
        # and work our way to the top left.
        #
        # To make this work for non-square matrices, we first handle the
        # "excess" rows/cols until we are left with a square matrix.
        #
        # We can store the side lengths in the matrix itself, or in a
        # separate matrix. Here I've chosen to just use the matrix
        # itself as storage.

        # Use this function to compute the maximum side length for a
        # given cell and store its value in the matrix
        def compute_max_side_length(row: int, col: int) -> None:
            # Get out if the cell is 0
            if matrix[row][col] == 0:
                return

            # Get right, down, and diagonal max side lengths
            neighbour_cells = ((row, col + 1), (row + 1, col), (row + 1, col + 1))
            neighbour_vals = [0, 0, 0]

            for i, (neighbour_row, neighbour_col) in enumerate(neighbour_cells):
                try:
                    neighbour_vals[i] = matrix[neighbour_row][neighbour_col]
                except IndexError:
                    pass

            # Store the max side length for the cell
            matrix[row][col] = 1 + min(neighbour_vals)

        # Handle excess rows
        # TODO: find some way to generalize this to avoid repeated code
        if (num_excess_rows := num_rows - num_cols) > 0:
            # Go from bottom to top
            for row in range(num_rows - 1, num_rows - 1 - num_excess_rows, -1):
                # Go from right to left
                for col in range(num_cols - 1, -1, -1):
                    compute_max_side_length(row, col)

        # Handle excess columns similarly to above
        if (num_excess_cols := num_cols - num_rows) > 0:
            for col in range(num_cols - 1, num_cols - 1 - num_excess_cols, -1):
                for row in range(num_rows - 1, -1, -1):
                    compute_max_side_length(row, col)

        # Now handle the unprocessed cells which are in a square
        # submatrix of size n x n. We'll process the outer layer,
        # leaving us with n' x n' unprocessed cells with n' = n - 1
        # initially. We keep repeating until n' = 1.
        n = min(num_rows, num_cols)

        for n_prime in range(n, 0, -1):
            # Furthest row in reverse order
            for col in range(n_prime - 1, -1, -1):
                compute_max_side_length(n_prime - 1, col)

            # Furthest col in reverse order (don't include
            # diagonal—we've already used it)
            for row in range(n_prime - 2, -1, -1):
                compute_max_side_length(row, n_prime - 1)

        # Now find the largest side length
        largest_side_length = 0

        for i, j in itertools.product(range(num_rows), range(num_cols)):
            largest_side_length = max(largest_side_length, matrix[i][j])

        return largest_side_length**2


# @leet end
