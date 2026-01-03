// @leet start
function coinChange(coins: number[], amount: number): number {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for (const coin of coins) {
    for (let subAmount = coin; subAmount <= amount; subAmount++) {
      dp[subAmount] = Math.min(dp[subAmount], 1 + dp[subAmount - coin]);
    }
  }

  return dp[amount] < Infinity ? dp[amount] : -1;
}
// @leet end
