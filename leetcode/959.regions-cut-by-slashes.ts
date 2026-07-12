// @leet start
function regionsBySlashes(grid: string[]): number {
  // Transform grid so that
  // / represented as 0 0 0 1
  //                  0 0 1 0
  //                  0 1 0 0
  //                  1 0 0 0
  // \ represented as 1 0 0 0
  //                  0 1 0 0
  //                  0 0 1 0
  //                  0 0 0 1
  // <space>  represented as 0 0 0 0
  //                         0 0 0 0
  //                         0 0 0 0
  //                         0 0 0 0
  const gridNew = Array.from({ length: 4 * grid.length }, () =>
    Array.from({ length: 4 * grid.length }, () => 0),
  );

  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[row].length; col++) {
      if (grid[row][col] === "/") {
        for (let i = 0; i < 4; i++) {
          gridNew[4 * row + 3 - i][4 * col + i] = 1;
        }
      } else if (grid[row][col] === "\\") {
        for (let i = 0; i < 4; i++) {
          gridNew[4 * row + i][4 * col + i] = 1;
        }
      }
    }
  }

  const n = gridNew.length;

  const dfs = (startRow: number, startCol: number) => {
    const stack: [number, number][] = [[startRow, startCol]];

    while (stack.length) {
      const [row, col] = stack.pop()!;

      for (const [dRow, dCol] of [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ]) {
        const nextRow = row + dRow;
        const nextCol = col + dCol;

        if (
          0 <= nextRow &&
          nextRow < n &&
          0 <= nextCol &&
          nextCol < n &&
          gridNew[nextRow][nextCol] !== 1
        ) {
          gridNew[nextRow][nextCol] = 1;

          stack.push([nextRow, nextCol]);
        }
      }
    }
  };

  let res = 0;

  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n; col++) {
      if (gridNew[row][col] !== 1) {
        res++;
        dfs(row, col);
      }
    }
  }

  return res;
}
// @leet end
