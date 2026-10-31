// @leet start
/**
 * @param {number} n
 * @param {number[]} cuts
 * @return {number}
 */
var minCost = function (n, cuts) {
  cuts = [0, ...cuts.sort((a, b) => a - b), n];
  dp = Array.from({ length: cuts.length }, () => Array(cuts.length).fill(0));

  for (let gap = 2; gap < cuts.length; gap++) {
    for (let i = 0; i < cuts.length - gap; i++) {
      const j = i + gap;
      dp[i][j] = Infinity;

      for (let k = i + 1; k < j; k++) {
        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
      }

      dp[i][j] += cuts[j] - cuts[i];
    }
  }

  return dp[0][cuts.length - 1];
};
// @leet end
