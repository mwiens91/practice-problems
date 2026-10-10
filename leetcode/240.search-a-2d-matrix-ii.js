// @leet start
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  let row = rows - 1;
  let col = 0;

  while (row >= 0 && col < cols) {
    if (matrix[row][col] === target) {
      return true;
    }

    if (matrix[row][col] > target) {
      row--;
    } else {
      col++;
    }
  }

  return false;
};
// @leet end
