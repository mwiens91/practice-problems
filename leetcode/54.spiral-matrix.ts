// @leet start
function spiralOrder(matrix: number[][]): number[] {
  const result: number[] = [];

  let startCol = 0;
  let endCol = matrix[0].length - 1;
  let startRow = 0;
  let endRow = matrix.length - 1;

  while (startCol <= endCol && startRow <= endRow) {
    for (let col = startCol; col <= endCol; col++) {
      result.push(matrix[startRow][col]);
    }

    for (let row = startRow + 1; row <= endRow; row++) {
      result.push(matrix[row][endCol]);
    }

    // If we're only 1D don't backtrack
    if (startCol === endCol || startRow === endRow) {
      break;
    }

    for (let col = endCol - 1; col >= startCol; col--) {
      result.push(matrix[endRow][col]);
    }

    for (let row = endRow - 1; row > startRow; row--) {
      result.push(matrix[row][startCol]);
    }

    startCol++;
    endCol--;
    startRow++;
    endRow--;
  }

  return result;
}
// @leet end
