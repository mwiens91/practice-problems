// @leet start
/**
 * @param {number[][]} grid
 * @param {number[][]} moveCost
 * @return {number}
 */
var minPathCost = function (grid, moveCost) {
  const rows = grid.length;
  const cols = grid[0].length;

  for (let row = rows - 2; row >= 0; row--) {
    for (let col = 0; col < cols; col++) {
      grid[row][col] += moveCost[grid[row][col]].reduce(
        (acc, curr, i) => Math.min(acc, curr + grid[row + 1][i]),
        Infinity,
      );
    }
  }

  return Math.min(...grid[0]);
};
// @leet end
