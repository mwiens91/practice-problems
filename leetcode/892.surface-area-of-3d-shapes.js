// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var surfaceArea = function (grid) {
  const rows = grid.length;
  const cols = grid[0].length;

  let res = 0;

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const val = grid[row][col];

      res += row === 0 ? val : Math.max(0, val - grid[row - 1][col]);
      res += row === rows - 1 ? val : Math.max(0, val - grid[row + 1][col]);
      res += col === 0 ? val : Math.max(0, val - grid[row][col - 1]);
      res += col === cols - 1 ? val : Math.max(0, val - grid[row][col + 1]);

      if (val > 0) {
        res += 2;
      }
    }
  }

  return res;
};
// @leet end
