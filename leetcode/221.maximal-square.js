// @leet start
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function (matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;
  let bestLength = 0;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (matrix[i][j] === "0") {
        matrix[i][j] = 0;
      } else {
        const leftLength = j > 0 ? matrix[i][j - 1] : 0;
        const upLength = i > 0 ? matrix[i - 1][j] : 0;
        const diagLength = i > 0 && j > 0 ? matrix[i - 1][j - 1] : 0;

        matrix[i][j] = 1 + Math.min(leftLength, upLength, diagLength);
        bestLength = Math.max(bestLength, matrix[i][j]);
      }
    }
  }

  return bestLength ** 2;
};
// @leet end
