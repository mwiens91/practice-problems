# @leet start
class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        # NOTE: could do this in O(1) memory with bitmasks
        row_increments = [0] * m
        col_increments = [0] * n

        for row_idx, col_idx in indices:
            row_increments[row_idx] += 1
            col_increments[col_idx] += 1

        # Find the number of odd numbers in a given column, considering
        # *only* row increments
        base_col_odd_count = sum(1 for row_inc in row_increments if row_inc % 2 == 1)

        # Now go through each column and flip the base column odd counts
        # if the odd column
        total_odd_count = 0

        for col_inc in col_increments:
            total_odd_count += (
                m - base_col_odd_count if col_inc % 2 == 1 else base_col_odd_count
            )

        return total_odd_count


# @leet end
