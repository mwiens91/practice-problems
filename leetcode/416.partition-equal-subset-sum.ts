// @leet start
function canPartition(nums: number[]): boolean {
  // We could optimize with 1D DP, but I'm not doing that here
  const sum = nums.reduce((acc, curr) => acc + curr);

  if (sum % 2 === 1) {
    return false;
  }

  const target = sum / 2;
  const dp: boolean[][] = Array.from({ length: nums.length + 1 }, () =>
    new Array(target + 1).fill(false),
  );
  dp[0][0] = true;

  for (let i = 1; i <= nums.length; i++) {
    for (let j = 0; j <= target; j++) {
      dp[i][j] ||=
        dp[i - 1][j] || (j >= nums[i - 1] ? dp[i - 1][j - nums[i - 1]] : false);
    }
  }

  return dp[nums.length][target];
}
// @leet end
