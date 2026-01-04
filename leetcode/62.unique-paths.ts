// @leet start
function uniquePaths(m: number, n: number): number {
  const dp = Array.from({ length: m }, () =>
    Array.from({ length: n }, () => 0),
  );

  for (let i = 0; i < m; i++) {
    dp[i][0] = 1;

    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i][j - 1] + (i > 0 ? dp[i - 1][j] : 0);
    }
  }

  return dp[m - 1][n - 1];
}
// @leet end
