// @leet start
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var shortestPath = function (grid, k) {
  const DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const rows = grid.length;
  const cols = grid[0].length;

  const visitedState = Array.from({ length: rows }, () => Array(cols).fill(-1));
  visitedState[0][0] = k;

  let prev = [0];
  let steps = 0;

  while (prev.length) {
    const curr = [];

    for (const cell of prev) {
      const i = Math.floor(cell / cols);
      const j = cell % cols;

      if (i === rows - 1 && j === cols - 1) {
        return steps;
      }

      const remaining = visitedState[i][j];

      for (const [di, dj] of DIRS) {
        const adjI = i + di;
        const adjJ = j + dj;

        if (adjI < 0 || adjI >= rows || adjJ < 0 || adjJ >= cols) {
          continue;
        }

        const adjRemaining = remaining - (grid[adjI][adjJ] ? 1 : 0);

        if (visitedState[adjI][adjJ] < adjRemaining) {
          visitedState[adjI][adjJ] = adjRemaining;
          curr.push(adjI * cols + adjJ);
        }
      }
    }

    steps++;
    prev = curr;
  }

  return -1;
};
// @leet end
