// @leet start
function minCost(n: number, cuts: number[]): number {
  cuts.sort((a, b) => a - b);
  const boundaries = [0, ...cuts, n];
  const dp: number[][] = Array.from({ length: boundaries.length }, () =>
    Array.from({ length: boundaries.length }, () => 0),
  );

  for (let diff = 2; diff < dp.length; diff++) {
    for (let i = 0; i < dp.length - diff; i++) {
      const j = i + diff;
      let min = Infinity;

      for (let k = i + 1; k < j; k++) {
        min = Math.min(min, dp[i][k] + dp[k][j]);
      }

      dp[i][j] = boundaries[j] - boundaries[i] + min;
    }
  }

  return dp[0][dp.length - 1];
}
// @leet end
