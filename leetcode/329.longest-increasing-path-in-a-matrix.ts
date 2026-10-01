// @leet start
function longestIncreasingPath(matrix: number[][]): number {
  const UNKNOWN = -1;
  const DIRS = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
  ];
  const m = matrix.length;
  const n = matrix[0].length;
  const heights: number[][] = Array.from({ length: m }, () =>
    Array(n).fill(UNKNOWN),
  );

  const getAndSetHeight = (i: number, j: number) => {
    if (heights[i][j] === UNKNOWN) {
      let best = 0;

      for (const [di, dj] of DIRS) {
        const adjI = i + di;
        const adjJ = j + dj;

        if (
          adjI >= 0 &&
          adjI < m &&
          adjJ >= 0 &&
          adjJ < n &&
          matrix[i][j] < matrix[adjI][adjJ]
        ) {
          best = Math.max(best, 1 + getAndSetHeight(adjI, adjJ));
        }
      }

      heights[i][j] = best;
    }

    return heights[i][j];
  };

  let maxHeight = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      maxHeight = Math.max(maxHeight, getAndSetHeight(i, j));
    }
  }

  return 1 + maxHeight;
}
// @leet end
