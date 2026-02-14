// @leet start
function dominantIndices(nums: number[]): number {
  let suffixSum = nums[nums.length - 1];
  let result = 0;

  for (let i = nums.length - 2; i >= 0; i--) {
    if (nums[i] > suffixSum / (nums.length - 1 - i)) {
      result++;
    }

    suffixSum += nums[i];
  }

  return result;
}
// @leet end
