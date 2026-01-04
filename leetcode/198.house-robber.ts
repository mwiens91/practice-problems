// @leet start
function rob(nums: number[]): number {
  if (nums.length > 1) {
    nums[1] = Math.max(nums[1], nums[0]);
  }

  for (let i = 2; i < nums.length; i++) {
    nums[i] = Math.max(nums[i] + nums[i - 2], nums[i - 1]);
  }

  return nums[nums.length - 1];
}
// @leet end
