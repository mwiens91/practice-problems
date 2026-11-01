// @leet start
function minMergedInteger(nums: number[]): number {
  let min = Infinity;

  for (let i = 0; i < nums.length; i += 2) {
    min = Math.min(
      min,
      nums[i] * Math.pow(10, Math.floor(Math.log10(nums[i + 1])) + 1) +
        nums[i + 1],
    );
  }

  return min;
}
// @leet end
