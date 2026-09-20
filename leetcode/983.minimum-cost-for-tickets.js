// @leet start
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function (days, costs) {
  const maxDay = days[days.length - 1];
  const nextIdxAfterDay = Array(maxDay + 1).fill(0);

  for (let i = days.length - 1; i > 0; i--) {
    for (let j = days[i]; j > days[i - 1]; j--) {
      nextIdxAfterDay[j] = i;
    }
  }

  // Reusing days for a DP array
  for (let i = days.length - 1; i >= 0; i--) {
    days[i] = Math.min(
      costs[0] +
        (days[i] + 1 <= maxDay ? days[nextIdxAfterDay[days[i] + 1]] : 0),
      costs[1] +
        (days[i] + 7 <= maxDay ? days[nextIdxAfterDay[days[i] + 7]] : 0),
      costs[2] +
        (days[i] + 30 <= maxDay ? days[nextIdxAfterDay[days[i] + 30]] : 0),
    );
  }

  return days[0];
};
// @leet end
