// @leet start
function maxProfit(prices: number[]): number {
  let result = 0;
  let minPrice = prices[0];

  for (const price of prices) {
    result = Math.max(result, price - minPrice);
    minPrice = Math.min(minPrice, price);
  }

  return result;
}
// @leet end
