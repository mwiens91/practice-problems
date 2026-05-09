# @leet start
from collections import deque


class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        start_row = 0
        end_row = len(grid) - 1
        start_col = 0
        end_col = len(grid[0]) - 1

        while start_row < end_row and start_col < end_col:
            circumference = 2 * (end_row - start_row + end_col - start_col)
            rotations = k % circumference
            total_steps = circumference + rotations if rotations > 0 else 0

            row = start_row
            col = start_col
            steps = 0
            queue: deque[int] = deque()

            while steps < total_steps:
                queue.append(grid[row][col])

                if len(queue) > rotations:
                    grid[row][col] = queue.popleft()

                steps += 1

                if col == start_col and row < end_row:
                    row += 1
                elif row == end_row and col < end_col:
                    col += 1
                elif col == end_col and row > start_row:
                    row -= 1
                else:
                    col -= 1

            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        return grid


# @leet end
