// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  const DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const LAND = 1;
  const SEEN = -1;
  let best = 0;

  // Consume island and return total size
  const dfs = (i, j) => {
    grid[i][j] = SEEN;
    let count = 1;

    for (const [di, dj] of DIRS) {
      const newI = i + di;
      const newJ = j + dj;

      if (
        newI >= 0 &&
        newI < grid.length &&
        newJ >= 0 &&
        newJ < grid[0].length &&
        grid[newI][newJ] == LAND
      ) {
        count += dfs(newI, newJ);
      }
    }

    return count;
  };

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == LAND) {
        best = Math.max(best, dfs(i, j));
      }
    }
  }

  return best;
};
// @leet end
