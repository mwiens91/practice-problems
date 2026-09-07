// @leet start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let dp2 = [0, 0];
  let dp1 = [0, 0];

  for (let i = prices.length - 1; i >= 0; i--) {
    const curr = [0, 0];

    curr[0] = Math.max(dp1[1] - prices[i], dp1[0]);

    curr[1] = Math.max(dp2[0] + prices[i], dp1[1]);

    dp2 = dp1;
    dp1 = curr;
  }

  return dp1[0];
};
// @leet end
