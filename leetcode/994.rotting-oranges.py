# @leet start
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        FRESH = 1
        ROTTING = 2

        rows = len(grid)
        cols = len(grid[0])

        level: list[tuple[int, int]] = []
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == ROTTING:
                    level.append((row, col))
                elif grid[row][col] == FRESH:
                    fresh_count += 1

        # Multi-source BFS
        time = 0

        while level:
            next_level: list[tuple[int, int]] = []

            for row, col in level:
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    adj_row = row + delta_row
                    adj_col = col + delta_col

                    if (
                        0 <= adj_row < rows
                        and 0 <= adj_col < cols
                        and grid[adj_row][adj_col] == FRESH
                    ):
                        next_level.append((adj_row, adj_col))
                        grid[adj_row][adj_col] = ROTTING
                        fresh_count -= 1

            level = next_level

            if level:
                time += 1

        return time if fresh_count == 0 else -1


# @leet end
