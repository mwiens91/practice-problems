# @leet start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        LAND = "1"

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def dfs(x: int, y: int) -> None:
            """Set all connected land to '-1'."""
            stack = [(x, y)]
            grid[x][y] = "-1"

            while stack:
                row, col = stack.pop()

                for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    adj_row = row + delta_row
                    adj_col = col + delta_col

                    if (
                        0 <= adj_row < rows
                        and 0 <= adj_col < cols
                        and grid[adj_row][adj_col] == LAND
                    ):
                        stack.append((adj_row, adj_col))
                        grid[adj_row][adj_col] = "-1"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND:
                    dfs(row, col)
                    count += 1

        return count


# @leet end
