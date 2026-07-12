// @leet start
function maxIceCream(costs: number[], coins: number): number {
  const counts = Array.from({ length: 1e5 + 1 }, () => 0);

  for (const cost of costs) {
    counts[cost]++;
  }

  let res = 0;

  for (const [cost, count] of counts.entries()) {
    if (cost > coins) {
      break;
    }

    const numTake = Math.min(count, Math.floor(coins / cost));
    res += numTake;
    coins -= numTake * cost;
  }

  return res;
}
// @leet end
