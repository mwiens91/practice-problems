// @leet start
function numIslands(grid: string[][]): number {
  let result = 0;

  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[0].length; col++) {
      if (grid[row][col] === "1") {
        // Consume island
        result++;
        consumeIsland(row, col, grid);
      }
    }
  }

  return result;
}

function consumeIsland(startRow: number, startCol: number, grid: string[][]) {
  grid[startRow][startCol] = "0";

  const stack: [number, number][] = [[startRow, startCol]];

  while (stack.length) {
    const [row, col] = stack.pop()!;

    for (const [adjRow, adjCol] of [
      [row - 1, col],
      [row + 1, col],
      [row, col - 1],
      [row, col + 1],
    ]) {
      if (
        adjRow >= 0 &&
        adjRow < grid.length &&
        adjCol >= 0 &&
        adjCol < grid[0].length &&
        grid[adjRow][adjCol] === "1"
      ) {
        grid[adjRow][adjCol] = "0";
        stack.push([adjRow, adjCol]);
      }
    }
  }
}
// @leet end
