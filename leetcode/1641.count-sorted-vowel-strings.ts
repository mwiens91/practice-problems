// @leet start
function countVowelStrings(n: number): number {
  const NUM_VOWEL = 5;
  const dp: number[][] = Array.from({ length: n + 1 }, () =>
    Array.from({ length: NUM_VOWEL }, () => 0),
  );

  for (let j = 0; j < NUM_VOWEL; j++) {
    dp[0][j] = 1;
  }

  for (let i = 1; i <= n; i++) {
    dp[i][0] = 1;

    for (let j = 1; j < NUM_VOWEL; j++) {
      dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
    }
  }

  return dp[n][NUM_VOWEL - 1];
}
// @leet end
