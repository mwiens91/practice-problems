// @leet start
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
  const OBSTACLE = 1;
  const rows = obstacleGrid.length;
  const cols = obstacleGrid[0].length;

  let prev = Array(cols).fill(0);
  prev[0] = 1;

  for (let i = 0; i < rows; i++) {
    const curr = Array(cols).fill(0);

    for (let j = 0; j < cols; j++) {
      if (obstacleGrid[i][j] !== OBSTACLE) {
        curr[j] = prev[j] + (j > 0 ? curr[j - 1] : 0);
      }
    }

    prev = curr;
  }

  return prev[cols - 1];
};
// @leet end
