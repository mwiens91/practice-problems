// @leet start
function closedIsland(grid: number[][]): number {
  const DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ] as const;
  const LAND = 0;
  const MARKED = -1;
  const rows = grid.length;
  const cols = grid[0].length;

  const dfs = (startRow: number, startCol: number) => {
    grid[startRow][startCol] = MARKED;
    const stack: [number, number][] = [[startRow, startCol]];

    let valid = true;

    while (stack.length) {
      const [i, j] = stack.pop()!;
      valid &&= i !== 0 && i !== rows - 1 && j !== 0 && j !== cols - 1;

      for (const [di, dj] of DIRS) {
        const adjI = i + di;
        const adjJ = j + dj;

        if (
          adjI >= 0 &&
          adjI < rows &&
          adjJ >= 0 &&
          adjJ < cols &&
          grid[adjI][adjJ] === LAND
        ) {
          grid[adjI][adjJ] = MARKED;
          stack.push([adjI, adjJ]);
        }
      }
    }

    return Number(valid);
  };

  let result = 0;

  for (let i = 1; i < rows - 1; i++) {
    for (let j = 1; j < cols - 1; j++) {
      if (grid[i][j] === LAND) {
        result += dfs(i, j);
      }
    }
  }

  return result;
}
// @leet end
