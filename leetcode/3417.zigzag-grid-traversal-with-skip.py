# @leet start
class Solution:
    def zigzagTraversal(self, grid: list[list[int]]) -> list[int]:
        result: list[int] = []

        num_rows = len(grid)
        num_cols = len(grid[0])

        row = 0
        col = 0
        moving_left_to_right = True

        while row < num_rows:
            while 0 <= col < num_cols:
                result.append(grid[row][col])
                col += 2 if moving_left_to_right else -2

            # Move down a row. For moving left to right: if we ended at
            # the second to last column, start at the last column of the
            # next row; otherwise we ended at the last column, so we
            # start at the second to last column of the next row. Moving
            # right to left follows similar logic.
            row += 1

            if col == num_cols:
                col = num_cols - 1
            elif col == num_cols + 1:
                col = num_cols - 2
            elif col == -1:
                col = 0
            else:
                # col == -2
                col = 1

            # Reverse direction of next iteration
            moving_left_to_right = not moving_left_to_right

        return result


# @leet end
