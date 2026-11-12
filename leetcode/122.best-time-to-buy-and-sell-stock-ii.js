// @leet start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let suffixMax = 0;
  let profit = 0;

  for (let i = prices.length - 1; i >= 0; i--) {
    if (prices[i] < suffixMax) {
      profit += suffixMax - prices[i];
      suffixMax = 0;
    }

    suffixMax = Math.max(suffixMax, prices[i]);
  }

  return profit;
};
// @leet end
