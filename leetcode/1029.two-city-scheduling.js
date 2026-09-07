// @leet start
/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function (costs) {
  return costs
    .sort((a, b) => a[0] - a[1] - (b[0] - b[1]))
    .reduce((acc, curr, i) => acc + curr[i < costs.length / 2 ? 0 : 1], 0);
};
// @leet end
