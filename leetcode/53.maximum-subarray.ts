// @leet start
function maxSubArray(nums: number[]): number {
  let best = nums[0];
  let curr = 0;

  for (const num of nums) {
    curr = curr < 0 ? num : curr + num;
    best = Math.max(best, curr);
  }

  return best;
}
// @leet end
