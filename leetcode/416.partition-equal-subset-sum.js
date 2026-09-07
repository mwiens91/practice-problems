// @leet start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
  const sum = nums.reduce((acc, x) => acc + x);

  if (sum % 2 !== 0) {
    return false;
  }

  const target = sum / 2;
  const possible = Array(target + 1).fill(false);
  possible[0] = true;

  for (const num of nums) {
    if (num <= target && possible[target - num]) {
      return true;
    }

    for (let i = target - 1; i >= num; i--) {
      possible[i] ||= possible[i - num];
    }
  }

  return possible[target];
};
// @leet end
