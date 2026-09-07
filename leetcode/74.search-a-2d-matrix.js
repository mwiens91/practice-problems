// @leet start
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  const idxToVal = (i) => {
    const row = Math.floor(i / cols);
    const col = i % cols;

    return matrix[row][col];
  };

  let left = 0;
  let right = rows * cols - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (idxToVal(mid) >= target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left < rows * cols && idxToVal(left) === target;
};
// @leet end
