// @leet start
/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
var countGoodStrings = function (low, high, zero, one) {
  const MOD = 1e9 + 7;
  const dp = Array(high).fill(0);

  for (let i = high - 1; i >= 0; i--) {
    const spaceRemaining = high - i;

    if (i >= low) {
      dp[i] = (dp[i] + 1) % MOD;
    }

    if (spaceRemaining >= zero) {
      dp[i] = (dp[i] + (spaceRemaining === zero ? 1 : dp[i + zero])) % MOD;
    }

    if (spaceRemaining >= one) {
      dp[i] = (dp[i] + (spaceRemaining === one ? 1 : dp[i + one])) % MOD;
    }
  }

  return dp[0];
};
// @leet end
