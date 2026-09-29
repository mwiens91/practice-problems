// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFallingPathSum = function (grid) {
  const n = grid.length;

  for (let i = n - 1; i > 0; i--) {
    const prefixMins = [Infinity];

    for (let j = 0; j < n - 1; j++) {
      prefixMins.push(Math.min(prefixMins[prefixMins.length - 1], grid[i][j]));
    }

    let suffixMin = Infinity;

    for (let j = n - 1; j >= 0; j--) {
      grid[i - 1][j] += Math.min(prefixMins[j], suffixMin);
      suffixMin = Math.min(suffixMin, grid[i][j]);
    }
  }

  return Math.min(...grid[0]);
};
// @leet end
