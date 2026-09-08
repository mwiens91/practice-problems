// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var splitArray = function (nums, k) {
  const dp = Array(nums.length).fill(0);
  dp[nums.length - 1] = nums[nums.length - 1];

  for (let i = nums.length - 2; i >= 0; i--) {
    dp[i] = nums[i] + dp[i + 1];
  }

  for (let kPrime = 2; kPrime <= k; kPrime++) {
    for (let i = 0; i <= nums.length - kPrime; i++) {
      let sum = 0;
      dp[i] = Infinity;

      for (let j = i; j <= nums.length - kPrime; j++) {
        sum += nums[j];
        dp[i] = Math.min(dp[i], Math.max(sum, dp[j + 1]));
      }
    }
  }

  return dp[0];
};
// @leet end
