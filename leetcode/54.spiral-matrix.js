// @leet start
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const result = [];

  let minRow = 0;
  let maxRow = matrix.length - 1;
  let minCol = 0;
  let maxCol = matrix[0].length - 1;

  while (minRow <= maxRow && minCol <= maxCol) {
    for (let j = minCol; j <= maxCol; j++) {
      result.push(matrix[minRow][j]);
    }

    for (let i = minRow + 1; i <= maxRow; i++) {
      result.push(matrix[i][maxCol]);
    }

    if (minRow < maxRow) {
      for (let j = maxCol - 1; j >= minCol; j--) {
        result.push(matrix[maxRow][j]);
      }
    }

    if (minCol < maxCol) {
      for (let i = maxRow - 1; i > minRow; i--) {
        result.push(matrix[i][minCol]);
      }
    }

    minRow++;
    maxRow--;
    minCol++;
    maxCol--;
  }

  return result;
};
// @leet end
