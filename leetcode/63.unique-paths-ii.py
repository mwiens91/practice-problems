# @leet start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # This solution is a modified version of my Unique Paths I
        # solution
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Initialize the memo with a value which depends if the goal is
        # an obstacle or not
        memo: dict[tuple[int, int], int] = {
            (m - 1, n - 1): 0 if obstacleGrid[m - 1][n - 1] else 1
        }

        def num_unique_paths(row: int, col: int) -> int:
            # Lookup previous result
            if (row, col) in memo:
                return memo[(row, col)]

            # Compute result. For num ways we
            num_ways = 0

            if row < m - 1 and not obstacleGrid[row + 1][col]:
                num_ways += num_unique_paths(row + 1, col)

            if col < n - 1 and not obstacleGrid[row][col + 1]:
                num_ways += num_unique_paths(row, col + 1)

            memo[(row, col)] = num_ways

            return num_ways

        # Handle edge case where robot starts on obstacle
        if obstacleGrid[0][0]:
            return 0

        # Return the number of unique paths
        return num_unique_paths(0, 0)


# @leet end
