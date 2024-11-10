# @leet start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Define a recursive function to traverse the boundary of the
        # matrix
        def traverse_boundary(ul_i: int, ul_j: int, br_i: int, br_j: int) -> list[int]:
            """Traverse boundary of matrix.

            (ul_i, ul_j) is the index of the upper left of our
            submatrix. (br_i, br_j) is the index of the bottom right of
            our submatrix.
            """
            # Get submatrix size
            n = br_i - ul_i + 1
            m = br_j - ul_j + 1

            # Traverse boundary
            i = ul_i
            j = ul_j

            elems = []

            for j in range(ul_j, br_j + 1):
                elems.append(matrix[ul_i][j])

            for i in range(ul_i + 1, br_i + 1):
                elems.append(matrix[i][br_j])

            if n > 1:
                for j in range(br_j - 1, ul_j - 1, -1):
                    elems.append(matrix[br_i][j])

            if m > 1:
                for i in range(br_i - 1, ul_i, -1):
                    elems.append(matrix[i][ul_j])

            # Special case: if submatrix size is 1x1, the one element
            # will not be picked up since ul_{ij} = br_{ij}. Add it here
            # instead
            if (n, m) == (1, 1):
                elems.append(matrix[ul_i][ul_j])

            # For the base case (no inner numbers), just return the
            # elements, otherwise recurse
            if n <= 2 or m <= 2:
                return elems

            return elems + traverse_boundary(ul_i + 1, ul_j + 1, br_i - 1, br_j - 1)

        # Return the answer
        return traverse_boundary(0, 0, len(matrix) - 1, len(matrix[0]) - 1)


# @leet end
