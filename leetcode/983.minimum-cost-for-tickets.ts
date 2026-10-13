// @leet start
function mincostTickets(days: number[], costs: number[]): number {
  const dp = Array<number>(days.length + 1).fill(0);
  let sevenDayPtr = days.length - 1;
  let thirtyDayPtr = days.length - 1;

  for (let i = days.length - 1; i >= 0; i--) {
    while (days[sevenDayPtr] >= days[i] + 7) {
      sevenDayPtr--;
    }

    while (days[thirtyDayPtr] >= days[i] + 30) {
      thirtyDayPtr--;
    }

    dp[i] = Math.min(
      costs[0] + dp[i + 1],
      costs[1] + dp[sevenDayPtr + 1],
      costs[2] + dp[thirtyDayPtr + 1],
    );
  }

  return dp[0];
}
// @leet end
