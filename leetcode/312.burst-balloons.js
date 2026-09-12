// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function (nums) {
  const dp = Array.from({ length: nums.length }, () =>
    Array(nums.length).fill(0),
  );

  // step is (subinterval size - 1)
  for (let step = 0; step < nums.length; step++) {
    for (let i = 0; i < nums.length - step; i++) {
      for (let k = i; k <= i + step; k++) {
        dp[i][i + step] = Math.max(
          dp[i][i + step],
          (k - i > 0 ? dp[i][k - 1] : 0) +
            (i + step - k > 0 ? dp[k + 1][i + step] : 0) +
            (i > 0 ? nums[i - 1] : 1) *
              (i + step < nums.length - 1 ? nums[i + step + 1] : 1) *
              nums[k],
        );
      }
    }
  }

  return dp[0][nums.length - 1];
};
// @leet end
