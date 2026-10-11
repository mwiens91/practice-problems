// @leet start
/**
 * @param {number[][]} heights
 * @return {number}
 */
var minimumEffortPath = function (heights) {
  const DIRS = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
  ];
  const rows = heights.length;
  const cols = heights[0].length;

  if (rows === 1 && cols === 1) {
    return 0;
  }

  const isDiffPossible = (maxDiff) => {
    const seen = Array(rows * cols - 1).fill(false);
    seen[0] = true;
    const stack = [0];

    while (stack.length) {
      const cell = stack.pop();

      if (cell === rows * cols - 1) {
        return true;
      }

      const i = Math.floor(cell / cols);
      const j = cell % cols;

      for (const [di, dj] of DIRS) {
        const adjI = i + di;
        const adjJ = j + dj;
        const adjCell = adjI * cols + adjJ;

        if (
          adjI >= 0 &&
          adjI < rows &&
          adjJ >= 0 &&
          adjJ < cols &&
          Math.abs(heights[i][j] - heights[adjI][adjJ]) <= maxDiff &&
          !seen[adjCell]
        ) {
          seen[adjCell] = true;
          stack.push(adjCell);
        }
      }
    }

    return false;
  };

  // Find lower and upper bound
  let left = Infinity;
  let right = -Infinity;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (j < cols - 1) {
        const diff = Math.abs(heights[i][j] - heights[i][j + 1]);
        left = Math.min(left, diff);
        right = Math.max(right, diff);
      }

      if (i < rows - 1) {
        const diff = Math.abs(heights[i][j] - heights[i + 1][j]);
        left = Math.min(left, diff);
        right = Math.max(right, diff);
      }
    }
  }

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (isDiffPossible(mid)) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
};
// @leet end
