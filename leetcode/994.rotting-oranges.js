// @leet start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  const FRESH = 1;
  const ROTTEN = 2;
  const DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  const rows = grid.length;
  const cols = grid[0].length;
  let currRot = [];

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === ROTTEN) {
        currRot.push([i, j]);
      }
    }
  }

  // # of minutes we infect oranges
  let steps = 0;

  while (currRot.length) {
    const nextRot = [];

    // Infect neighbouring oranges
    for (const [rotX, rotY] of currRot) {
      for (const [dx, dy] of DIRS) {
        const adjX = rotX + dx;
        const adjY = rotY + dy;

        if (
          0 <= adjX &&
          adjX < rows &&
          0 <= adjY &&
          adjY < cols &&
          grid[adjX][adjY] === FRESH
        ) {
          grid[adjX][adjY] = ROTTEN;
          nextRot.push([adjX, adjY]);
        }
      }
    }

    if (nextRot.length) {
      steps++;
    }

    currRot = nextRot;
  }

  // Return -1 if any fresh remaining
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === FRESH) {
        return -1;
      }
    }
  }

  return steps;
};
// @leet end
