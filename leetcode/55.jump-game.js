// @leet start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  const dp = Array(nums.length).fill(false);
  dp[nums.length - 1] = true;

  for (let i = nums.length - 2; i >= 0; i--) {
    for (let j = 1; j <= nums[i]; j++) {
      if (dp[i + j]) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[0];
};
// @leet end
