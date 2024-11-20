# @leet start
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize the matrix
        matrix = [[0] * n for _ in range(n)]

        # Insert all but the final element
        i = 0
        j = 0

        # Both mins and maxes are inclusive here
        min_i = 1  # starts at 1, not a typo
        max_i = n - 1
        min_j = 0
        max_j = n - 1

        count = 1
        final_count = n**2 - 1

        while count <= final_count:
            # Go right
            while j < max_j and count <= final_count:
                matrix[i][j] = count
                count += 1

                j += 1

            max_j -= 1

            # Go down
            while i < max_i and count <= final_count:
                matrix[i][j] = count
                count += 1

                i += 1

            max_i -= 1

            # Go right
            while j > min_j and count <= final_count:
                matrix[i][j] = count
                count += 1

                j -= 1

            min_j += 1

            # Go up
            while i > min_i and count <= final_count:
                matrix[i][j] = count
                count += 1

                i -= 1

            min_i += 1


        # Insert last element
        final_i = n // 2
        final_j = n // 2

        if n % 2 == 0:
            # For even n, the formula for the final column is different
            final_j -= 1

        matrix[final_i][final_j] = n ** 2

        return matrix


# @leet end
