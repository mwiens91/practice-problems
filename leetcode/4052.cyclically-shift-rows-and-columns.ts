// @leet start
function cyclicShift(
  n: number,
  grid: number[][],
  rowShift: number[],
  colShift: number[],
): number[][] {
  const result = Array.from({ length: n }, () => Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const newJ = (j - rowShift[i] + n) % n;
      const newI = (i - colShift[newJ] + n) % n;

      result[newI][newJ] = grid[i][j];
    }
  }

  return result;
}
// @leet end
