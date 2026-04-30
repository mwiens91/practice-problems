# @leet start
class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[-1 for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]
        dp[0][0][0] = 0

        for row in range(rows):
            for col in range(cols):
                cell_score = grid[row][col]
                cell_cost = 1 if cell_score == 2 else cell_score

                for cost in range(k + 1):
                    if cost + cell_cost > k:
                        break

                    if row > 0 and dp[row - 1][col][cost] != -1:
                        dp[row][col][cost + cell_cost] = max(
                            dp[row][col][cost + cell_cost],
                            cell_score + dp[row - 1][col][cost],
                        )

                    if col > 0 and dp[row][col - 1][cost] != -1:
                        dp[row][col][cost + cell_cost] = max(
                            dp[row][col][cost + cell_cost],
                            cell_score + dp[row][col - 1][cost],
                        )

        return max(dp[rows - 1][cols - 1])


# @leet end
