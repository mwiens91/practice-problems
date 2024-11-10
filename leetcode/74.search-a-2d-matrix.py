# @leet start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # We'll just do a binary search. It's easier to just convert the
        # matrix to a list and do a binary search on that, but let's try
        # an O(1) memory approach.
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # We'll act like we're just doing a binary search on a list of
        # length n, and have a function to translate list indices to
        # matrix indices
        n = num_rows * num_cols

        def list_idx_to_matrix_elem(idx: int) -> int:
            # Get row i and col j
            i = idx // num_cols
            j = idx % num_cols

            return matrix[i][j]

        # Do a binary search
        i = 0
        j = n - 1

        while i <= j:
            mid = (i + j) // 2
            mid_num = list_idx_to_matrix_elem(mid)

            if mid_num == target:
                return True
            elif mid_num < target:
                i = mid + 1
            else:
                # mid_num > target
                j = mid - 1

        return False


# @leet end
