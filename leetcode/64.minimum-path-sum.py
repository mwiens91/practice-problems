# @leet start
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # Get the number of rows and columns
        num_rows = len(grid)
        num_cols = len(grid[0])

        # For each "forward diagonal" of elements whose indices sum to
        # index sum, update these elements using the minimum path sum of
        # the previous elements. The ranges can look a little confusing
        # so to explain more simply here:
        #
        # index_sum takes on 1 -> (num_rows - 1) + (num_cols - 1)
        # row takes on 0 -> min(index_sum, num_rows - 1)
        # col takes on 0 -> min(index_sum, num_cols - 1)
        #
        # where row + col = index_sum and the above ranges are inclusive
        for index_sum in range(1, num_rows + num_cols - 1):
            for row in range(min(index_sum + 1, num_rows)):
                col = index_sum - row

                # Row is guaranteed to be in bounds by above logic, but
                # we need to check for the column here
                if col >= num_cols:
                    continue

                # Get indices (row, column) to the left and above this
                # element, if they exist
                parent_indices = []

                if row - 1 >= 0:
                    parent_indices.append((row - 1, col))

                if col - 1 >= 0:
                    parent_indices.append((row, col - 1))

                # Now get the corresponding values of these indices
                parent_vals = [
                    grid[parent_row][parent_col]
                    for parent_row, parent_col in parent_indices
                ]

                # Add the minimum parent path to this element
                grid[row][col] += min(parent_vals)

        return grid[num_rows - 1][num_cols - 1]


# @leet end
