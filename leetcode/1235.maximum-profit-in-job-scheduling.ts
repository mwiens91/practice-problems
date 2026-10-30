// @leet start
function jobScheduling(
  startTime: number[],
  endTime: number[],
  profit: number[],
): number {
  const bestProfits = [0];
  const bestProfitTimes = [1];

  const order = Array.from(
    { length: endTime.length },
    (_, i) => i,
  ).sort((a, b) => endTime[a] - endTime[b]);

  for (const i of order) {
    const start = startTime[i];

    // Binary search to find highest recorded time <= start
    let left = 0;
    let right = bestProfitTimes.length - 1;

    while (left <= right) {
      const mid = left + Math.floor((right - left) / 2);

      if (bestProfitTimes[mid] <= start) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    const bestProfit = bestProfits[right] + profit[i];

    if (bestProfit > bestProfits[bestProfits.length - 1]) {
      if (endTime[i] === bestProfitTimes[bestProfitTimes.length - 1]) {
        bestProfits[bestProfits.length - 1] = bestProfit;
      } else {
        bestProfits.push(bestProfit);
        bestProfitTimes.push(endTime[i]);
      }
    }
  }

  return bestProfits[bestProfits.length - 1];
}
// @leet end
