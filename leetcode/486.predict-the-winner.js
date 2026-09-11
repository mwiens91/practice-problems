// @leet start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var predictTheWinner = function (nums) {
  const dp = [...nums];

  for (let delta = 1; delta < nums.length; delta++) {
    for (let i = 0; i < nums.length - delta; i++) {
      dp[i] = Math.max(nums[i] - dp[i + 1], nums[i + delta] - dp[i]);
    }
  }
  return dp[0] >= 0;
};
// @leet end
