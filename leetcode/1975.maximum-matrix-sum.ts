// @leet start
function maxMatrixSum(matrix: number[][]): number {
  let absSum = 0;
  let absMin = Infinity;
  let oddNeg = false;

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      const val = matrix[i][j];
      const absVal = Math.abs(val);

      absSum += absVal;
      absMin = Math.min(absMin, absVal);

      if (val < 0) {
        oddNeg = !oddNeg;
      }
    }
  }

  return absSum - Number(oddNeg) * 2 * absMin;
}
// @leet end
