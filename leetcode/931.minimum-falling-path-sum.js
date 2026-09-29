// @leet start
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function (matrix) {
  const n = matrix.length;

  for (let i = n - 2; i >= 0; i--) {
    for (let j = 0; j < n; j++) {
      matrix[i][j] += Math.min(
        j > 0 ? matrix[i + 1][j - 1] : Infinity,
        matrix[i + 1][j],
        j < n - 1 ? matrix[i + 1][j + 1] : Infinity,
      );
    }
  }

  return Math.min(...matrix[0]);
};
// @leet end
