// @leet start
/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
var change = function (amount, coins) {
  const dp = Array(amount + 1).fill(0);
  dp[0] = 1;

  for (let i = 0; i < coins.length; i++) {
    const val = coins[i];

    for (let j = val; j <= amount; j++) {
      dp[j] += dp[j - val];
    }
  }

  return dp[amount];
};
// @leet end
