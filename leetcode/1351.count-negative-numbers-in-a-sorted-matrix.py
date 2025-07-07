# @leet start
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Find the number of non-negative numbers per row, using the
        # fact that columns are (non-strictly) decreasing
        current_row = num_rows - 1
        num_negative = 0
        binary_search_start_col = 0

        while current_row >= 0:
            # Use binary search to find the last non-negative number in
            # the row
            left = binary_search_start_col
            right = num_cols - 1

            while left <= right:
                mid = (left + right) // 2

                if grid[current_row][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1

            if right == num_cols - 1:
                # No negative numbers in this or any above rows
                return num_negative

            num_negative += num_cols - 1 - right

            current_row -= 1
            binary_search_start_col = max(0, right)

        return num_negative


# @leet end
