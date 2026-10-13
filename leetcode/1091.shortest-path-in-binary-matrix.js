// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function (grid) {
  if (grid[0][0]) {
    return -1;
  }

  const DIRS = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];
  const SEEN = 2;
  const n = grid.length;

  let layer = 1;
  let prev = [0];
  grid[0][0] = SEEN;

  while (prev.length) {
    const curr = [];

    for (const cell of prev) {
      const i = Math.floor(cell / n);
      const j = cell % n;

      if (i === n - 1 && j === n - 1) {
        return layer;
      }

      for (const [di, dj] of DIRS) {
        const adjI = i + di;
        const adjJ = j + dj;

        if (
          adjI >= 0 &&
          adjI < n &&
          adjJ >= 0 &&
          adjJ < n &&
          !grid[adjI][adjJ]
        ) {
          grid[adjI][adjJ] = SEEN;
          curr.push(n * adjI + adjJ);
        }
      }
    }

    prev = curr;
    layer++;
  }

  return -1;
};
// @leet end
