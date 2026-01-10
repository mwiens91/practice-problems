// @leet start
function minimumDeleteSum(s1: string, s2: string): number {
  const dp = Array.from({ length: s1.length + 1 }, () =>
    Array.from({ length: s2.length + 1 }, () => 0),
  );

  // Initialize first row
  for (let j = 1; j <= s2.length; j++) {
    dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j - 1);
  }

  // General case
  for (let i = 1; i <= s1.length; i++) {
    dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i - 1);

    for (let j = 1; j <= s2.length; j++) {
      dp[i][j] =
        s1[i - 1] === s2[j - 1]
          ? dp[i - 1][j - 1]
          : Math.min(
              dp[i - 1][j] + s1.charCodeAt(i - 1),
              dp[i][j - 1] + s2.charCodeAt(j - 1),
            );
    }
  }

  return dp[s1.length][s2.length];
}

// @leet end
