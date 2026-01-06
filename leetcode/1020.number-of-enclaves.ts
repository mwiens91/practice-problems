// @leet start
function numEnclaves(grid: number[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;

  // Consumes adjacent 1 cells (marking them as 0 once visited) and
  // returns the number of cells of adjacent 1s and whether any the
  // cells touch the edge
  const dfs = (startRow: number, startCol: number): [number, boolean] => {
    let num = 0;
    let touchesEdge = false;

    const stack: [number, number][] = [[startRow, startCol]];
    grid[startRow][startCol] = 0;

    while (stack.length) {
      const [row, col] = stack.pop()!;

      num++;

      if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {
        touchesEdge = true;
      }

      for (const [deltaRow, deltaCol] of [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ]) {
        const newRow = row + deltaRow;
        const newCol = col + deltaCol;

        if (
          newRow >= 0 &&
          newRow < rows &&
          newCol >= 0 &&
          newCol < cols &&
          grid[newRow][newCol] == 1
        ) {
          grid[newRow][newCol] = 0;
          stack.push([newRow, newCol]);
        }
      }
    }

    return [num, touchesEdge];
  };

  let result = 0;

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (grid[row][col] == 1) {
        const [numCells, touchesEdge] = dfs(row, col);

        if (!touchesEdge) {
          result += numCells;
        }
      }
    }
  }

  return result;
}
// @leet end
