// @leet start
/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
var jobScheduling = function (startTime, endTime, profit) {
  const timeRanks = new Map(
    [...new Set([...startTime, ...endTime])]
      .sort((a, b) => a - b)
      .map((t, i) => [t, i]),
  );
  const jobsEndingAtTimeRank = Array.from({ length: timeRanks.size }, () => []);
  endTime.forEach((t, i) => jobsEndingAtTimeRank[timeRanks.get(t)].push(i));

  const dp = Array(timeRanks.size).fill(0);

  for (let i = 0; i < dp.length; i++) {
    dp[i] = dp[i - 1] ?? 0;

    for (const jobIdx of jobsEndingAtTimeRank[i]) {
      dp[i] = Math.max(
        dp[i],
        dp[timeRanks.get(startTime[jobIdx])] + profit[jobIdx],
      );
    }
  }

  return dp[dp.length - 1];
};
// @leet end
