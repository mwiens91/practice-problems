// @leet start
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
  const OBSTACLE = 1;
  const rows = obstacleGrid.length;
  const cols = obstacleGrid[0].length;

  const dp = Array(cols).fill(0);
  dp[0] = 1;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (obstacleGrid[i][j] === OBSTACLE) {
        dp[j] = 0;
      } else if (j > 0) {
        dp[j] += dp[j - 1];
      }
    }
  }

  return dp[cols - 1];
};
// @leet end
