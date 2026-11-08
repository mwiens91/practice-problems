// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countServers = function (grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  const rowCounts = Array(rows).fill(0);
  const colCounts = Array(cols).fill(0);

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      rowCounts[i] += grid[i][j];
      colCounts[j] += grid[i][j];
    }
  }

  let res = 0;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] && (rowCounts[i] > 1 || colCounts[j] > 1)) {
        res++;
      }
    }
  }

  return res;
};
// @leet end
