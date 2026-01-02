// @leet start
function countMaxOrSubsets(nums: number[]): number {
  const target = nums.reduce((acc, curr) => acc | curr);
  const dp: Array<number> = new Array(1 << nums.length);
  dp[0] = 0;

  let result = 0;
  let msb = 0;
  let nextPowerTwo = 2;

  // Loop over all subsets, using i as a bitmask for what indices to
  // include
  for (let i = 1; i < dp.length; i++) {
    if (i == nextPowerTwo) {
      msb++;
      nextPowerTwo <<= 1;
    }

    dp[i] = nums[msb] | dp[i & ~(1 << msb)];

    if (dp[i] == target) {
      result++;
    }
  }

  return result;
}
// @leet end
