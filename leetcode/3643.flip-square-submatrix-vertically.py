# @leet start
class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        # Swap the x + ith row with the x + k - 1 - ith row for the
        # specified columns
        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i

            for col in range(y, y + k):
                grid[top_row][col], grid[bottom_row][col] = (
                    grid[bottom_row][col],
                    grid[top_row][col],
                )

        return grid


# @leet end
