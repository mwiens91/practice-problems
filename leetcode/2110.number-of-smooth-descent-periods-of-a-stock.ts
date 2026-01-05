// @leet start
function getDescentPeriods(prices: number[]): number {
  let result = 0;
  let left = 0;

  while (left < prices.length) {
    let end = left + 1; // exclusive

    while (end < prices.length && prices[end - 1] - prices[end] === 1) {
      end++;
    }

    const size = end - left;
    result += (size * (size + 1)) / 2;
    left = end;
  }

  return result;
}
// @leet end
